"""Construit la page récap d'un pack Facebook (à publier avec l'outil Artifact).

Usage : python3 outils/facebook/recap.py facebook/AAAA-MM.json <hash_commit> <dossier_sortie> "<Mois AAAA>"
Sortie : <dossier_sortie>/index.html + <dossier_sortie>/img/*.jpg (à passer dans `files`).
"""
import datetime, html, json, pathlib, shutil, sys

RACINE = pathlib.Path(__file__).resolve().parents[2]
JOURS = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
MOIS = ['', 'janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.']
TYPES = {'pub': ('Ta pub', 'pub'), 'outil': ('Coulisse de prof', 'coulisse'), 'existant': ('Coulisse de prof', 'coulisse'),
         'citation': ('Phrase de la semaine', 'phrase')}

CSS = """
/* Layout : une colonne de fiches (visuel + légende), lisible au pouce sur téléphone */
:root{--bg:#fbf7ee;--surface:#ffffff;--fg:#1d2b44;--muted:#56657a;--blue:#1f5fa8;--teal:#1d9e93;--sun:#f2b632;--line:#e6dfcf;
 --display:'Lora',Georgia,serif;--body:'Poppins',system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#13202f;--surface:#1b2b3e;--fg:#eef1f5;--muted:#a7b3c2;--blue:#7fb2ee;--teal:#4fd1c3;--sun:#f5c55a;--line:#2b3d53;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#13202f;--surface:#1b2b3e;--fg:#eef1f5;--muted:#a7b3c2;--blue:#7fb2ee;--teal:#4fd1c3;--sun:#f5c55a;--line:#2b3d53;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font:16px/1.55 var(--body);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 48px}
.wrap{max-width:980px;margin:0 auto;display:flex;flex-direction:column;gap:28px}
.band{height:8px;border-radius:4px;background:linear-gradient(90deg,var(--blue) 0 33%,var(--teal) 33% 66%,var(--sun) 66%)}
h1{font:700 clamp(30px,6vw,46px)/1.1 var(--display);color:var(--blue);text-wrap:balance;margin:0}
.lead{color:var(--muted);margin:8px 0 0;max-width:62ch}
.how{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:18px 20px}
.how h2{font:600 15px var(--body);letter-spacing:.06em;text-transform:uppercase;color:var(--teal);margin:0 0 8px}
.how ol{margin:0;padding-left:20px;display:grid;gap:4px}
.post{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:22px;align-items:start;padding-bottom:28px;border-bottom:1px solid var(--line)}
.post img{width:100%;height:auto;border-radius:10px;box-shadow:0 6px 20px rgb(0 0 0 / .08)}
.meta{min-width:0;display:flex;flex-direction:column;gap:12px}
.when{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0}
.day{font:700 24px var(--display)}
.chip{font-size:13px;font-weight:600;padding:4px 12px;border-radius:999px;letter-spacing:.02em}
.chip.pub{background:var(--sun);color:#1d2b44}.chip.coulisse{background:var(--blue);color:var(--bg)}.chip.phrase{background:var(--teal);color:var(--bg)}.chip.done{background:var(--line);color:var(--fg)}
.cap{margin:0;white-space:pre-wrap;word-wrap:break-word;font:15px/1.55 var(--body);background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px;max-height:340px;overflow:auto}
.actions{display:flex;flex-wrap:wrap;gap:10px}
button,.actions a{font:600 15px var(--body);border-radius:10px;padding:10px 16px;cursor:pointer;text-decoration:none}
button{background:var(--blue);color:var(--bg);border:0}
.actions a{color:var(--blue);border:2px solid var(--blue)}
button:focus-visible,.actions a:focus-visible{outline:3px solid var(--sun);outline-offset:2px}
button.ok{background:var(--teal)}
@media (max-width:640px){.post{grid-template-columns:1fr}.post img{max-width:420px}}
"""

JS = """document.addEventListener('click',async e=>{const b=e.target.closest('button[data-copy]');if(!b)return;
 const el=document.getElementById(b.dataset.copy);const t=el.textContent;
 try{await navigator.clipboard.writeText(t);b.textContent='Légende copiée ✓';b.classList.add('ok');setTimeout(()=>{b.textContent='Copier la légende';b.classList.remove('ok')},2000)}
 catch(_){const r=document.createRange();r.selectNodeContents(el);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Texte sélectionné : copie-le'}});"""

def main(fichier, h, sortie, mois):
    posts = json.load(open(fichier, encoding="utf-8"))
    out = pathlib.Path(sortie); (out / "img").mkdir(parents=True, exist_ok=True)
    for f in (out / "img").glob("*.jpg"): f.unlink()
    cards = []
    for i, p in enumerate(posts):
        d = datetime.date.fromisoformat(p['date']); f = f"{p['date']}-{p['nom']}.jpg"
        shutil.copy(RACINE / "facebook" / p['date'] / f"{p['nom']}.jpg", out / "img" / f)
        lab, cls = TYPES[p['type']]
        raw = f"https://raw.githubusercontent.com/unprofdanstapoche-oss/medias-reseaux/{h}/facebook/{p['date']}/{p['nom']}.jpg"
        cards.append(f'''<article class="post"><img src="img/{f}" alt="Visuel du {JOURS[d.weekday()]} {d.day} {MOIS[d.month]}" loading="lazy" width="1080" height="1350">
 <div class="meta"><p class="when"><span class="day">{JOURS[d.weekday()].capitalize()} {d.day} {MOIS[d.month]}</span><span class="chip {cls}">{lab}</span>{'<span class="chip done">✓ Déjà publié le 2 nov.</span>' if p.get('publie') else ''}</p>
 <pre class="cap" id="cap{i}">{html.escape(p['legende'])}</pre>
 <div class="actions"><button type="button" data-copy="cap{i}">Copier la légende</button><a href="{raw}" target="_blank" rel="noopener">Ouvrir l'image</a></div></div></article>''')
    page = f'''<title>Pack Facebook {mois.split()[0].lower()}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:wght@600;700&family=Poppins:wght@400;500;600&display=swap">
<style>{CSS}</style>
<div class="wrap"><div class="band"></div>
<header><h1>Pack Facebook · {mois}</h1>
<p class="lead">{len(posts)} publications pour ta page Un Prof dans ta Poche : ta pub le mercredi, une coulisse de prof le samedi et la phrase de la semaine le dimanche.</p></header>
<section class="how"><h2>Programmer dans Meta Business Suite</h2>
<ol><li>Ouvre l'image, puis enregistre-la (appui long sur téléphone).</li><li>Copie la légende avec le bouton.</li>
<li>Dans Meta Business Suite : « Créer une publication », coche seulement ta page Facebook, ajoute l'image, colle la légende.</li>
<li>Choisis « Programmer » à la date indiquée (vers 12 h le mercredi, 10 h le week-end, 18 h pour un rappel du vendredi).</li></ol></section>
{"".join(cards)}</div>
<script>{JS}</script>'''
    (out / "index.html").write_text(page, encoding="utf-8")
    print(json.dumps({f"img/{x.name}": f"img/{x.name}" for x in sorted((out / 'img').glob('*.jpg'))}, ensure_ascii=False))

if __name__ == "__main__":
    main(*sys.argv[1:5])
