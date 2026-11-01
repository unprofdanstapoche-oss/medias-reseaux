"""Gabarit Facebook Un Prof dans ta Poche (1080x1350, fond crème, bleu/turquoise/jaune du logo, Lora + Poppins).

Usage : python3 outils/facebook/gabarit_fb.py facebook/<mois>.json
Chaque post : {"date": "AAAA-MM-JJ", "nom": "...", "type": "pub|outil|citation", ...champs du type..., "legende": "..."}
  outil    : tag, titre (HTML, <span> = or), sous_titre, illustration (HTML/SVG), points (liste HTML)
  pub      : tag, titre, sous_titre, points (liste HTML, coches), appel (texte de l'encadré jaune)
  citation : citation, auteur, note
Sortie : facebook/<date>/<nom>.jpg
"""
import asyncio, json, pathlib, sys
from playwright.async_api import async_playwright
from PIL import Image

RACINE = pathlib.Path(__file__).resolve().parents[2]

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#fbf7ee;font-family:'Poppins',sans-serif;color:#1d2b44;
 position:relative;overflow:hidden;padding:80px 80px 70px}
.band{position:absolute;left:0;right:0;top:0;height:22px;background:linear-gradient(90deg,#1f5fa8 0 33%,#1fb5a8 33% 66%,#f2b632 66%)}
.dot{position:absolute;border-radius:50%}
.d1{width:420px;height:420px;background:#1fb5a8;opacity:.10;right:-140px;top:-120px}
.d2{width:300px;height:300px;background:#f2b632;opacity:.16;left:-110px;bottom:120px}
.tag{display:inline-block;background:#1f5fa8;color:#fff;font-weight:600;font-size:30px;padding:12px 30px;border-radius:40px}
.tag.jaune{background:#f2b632;color:#1d2b44}
h1{font-family:'Lora',serif;font-weight:700;font-size:80px;line-height:1.05;margin-top:34px;color:#1f5fa8}
h1 span{color:#d39a14}
.sub{font-size:34px;margin-top:18px;color:#2f6f6a;font-weight:500;line-height:1.35}
.illu{margin-top:36px;height:330px;display:flex;align-items:center;justify-content:center}
ul{list-style:none;margin-top:30px}
li{font-size:33px;line-height:1.3;padding:9px 0 9px 60px;position:relative}
li::before{content:"";position:absolute;left:8px;top:15px;width:28px;height:28px;border-radius:50%;
 background:radial-gradient(circle at 35% 35%,#ffe9a8,#e0a526 60%,#a8740c)}
li b{color:#1f5fa8}
ul.check li::before{content:"✓";background:#1fb5a8;color:#fff;font-weight:700;font-size:20px;text-align:center;line-height:28px}
.appel{margin-top:40px;background:#f2b632;border-radius:28px;padding:26px 36px;font-size:34px;font-weight:600;text-align:center;line-height:1.35}
.contact{display:block;margin-top:10px;font-size:30px;font-weight:700;color:#1f5fa8;white-space:nowrap}
.contact small{display:block;font-size:24px;font-weight:600;color:#1d2b44}
.quote{font-family:'Lora',serif;font-style:italic;font-weight:600;font-size:66px;line-height:1.25;color:#1f5fa8;margin-top:40px}
.qmark{font-family:'Lora',serif;font-size:260px;line-height:.6;color:#1fb5a8;opacity:.5;margin-top:70px;height:120px}
.auteur{font-size:36px;margin-top:40px;color:#2f6f6a;font-weight:600}
.note{font-size:32px;margin-top:60px;line-height:1.45;color:#3d4d63}
.foot{position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end;
 border-top:3px solid #1fb5a8;padding-top:22px;font-size:26px;color:#3d4d63}
.foot b{font-size:32px;color:#1f5fa8;display:block}
.foot span:first-child{white-space:nowrap}
.foot .site{font-weight:600;color:#1d2b44;text-align:right;font-size:25px}
"""

CONTACT = '<span class="contact">📞 07 56 92 56 73<small>✉️ unprofdanstapoche@gmail.com</small></span>'

FOOT = """<div class="foot"><span><b>Un Prof dans ta Poche</b>Cours à domicile : Tonnay‑Charente, Rochefort<br>Visio partout dans le monde</span>
<span class="site">unprofdanstapoche.com</span></div>"""

def corps(p):
    t = p["type"]
    if t == "outil":
        pts = "".join(f"<li>{x}</li>" for x in p["points"])
        return (f'<span class="tag">{p["tag"]}</span><h1>{p["titre"]}</h1><p class="sub">{p["sous_titre"]}</p>'
                f'<div class="illu">{p["illustration"]}</div><ul>{pts}</ul>')
    if t == "pub":
        pts = "".join(f"<li>{x}</li>" for x in p["points"])
        return (f'<span class="tag jaune">{p["tag"]}</span><h1>{p["titre"]}</h1><p class="sub">{p["sous_titre"]}</p>'
                f'<ul class="check" style="margin-top:44px">{pts}</ul><div class="appel">{p["appel"]}{CONTACT}</div>')
    if t == "citation":
        return (f'<span class="tag">🌱 La phrase de la semaine</span><div class="qmark">“</div>'
                f'<p class="quote">{p["citation"]}</p><p class="auteur">— {p["auteur"]}</p><p class="note">{p["note"]}</p>')
    raise ValueError(t)

def page(p):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="band"></div><div class="dot d1"></div><div class="dot d2"></div>{corps(p)}{FOOT}</body></html>')

async def main(fichier):
    posts = json.load(open(fichier, encoding="utf-8"))
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for p in posts:
            d = RACINE / "facebook" / p["date"]; d.mkdir(parents=True, exist_ok=True)
            await pg.set_content(page(p), wait_until="networkidle"); await pg.wait_for_timeout(150)
            png = d / f'{p["nom"]}.png'
            await pg.screenshot(path=str(png))
            Image.open(png).convert("RGB").save(png.with_suffix(".jpg"), quality=90); png.unlink()
            print(png.with_suffix(".jpg"))
        await b.close()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
