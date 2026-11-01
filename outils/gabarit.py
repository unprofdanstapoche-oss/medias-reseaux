"""Gabarit des carrousels Un Prof dans ta Poche (1080x1920, navy/turquoise/or, Poppins).

Usage : python3 outils/gabarit.py semaine.json
semaine.json = liste de posts :
  {"date": "2026-11-09", "nom": "lundi-3e-maths", "tag": "3e · MATHS",
   "slides": ["<h1>…</h1><p>…</p>", "<h2>…</h2><div class='box'>…</div>", …]}
Chaque slide est le contenu HTML central ; en-tête (tag, n/total) et pied (marque, « Glisse → »)
sont ajoutés automatiquement. Dernière slide : pied « 👇 En commentaire ! ».
Classes : h1 (accroche), h2 (titre or), p, .box (encadré), .gold, .teal, .small, .strike (calcul faux en rouge), sup.
Sortie : <date>/<nom>-<n>.jpg à la racine du dépôt.
"""
import asyncio, json, pathlib, sys
from playwright.async_api import async_playwright
from PIL import Image

RACINE = pathlib.Path(__file__).resolve().parent.parent
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;font-family:'Poppins',sans-serif;background:#0f2a4a;color:#fff;
 display:flex;flex-direction:column;padding:110px 90px;position:relative;overflow:hidden}
.blob{position:absolute;border-radius:50%;filter:blur(2px);opacity:.18}
.b1{width:700px;height:700px;background:#1fb5a8;top:-250px;right:-250px}
.b2{width:500px;height:500px;background:#f2b632;bottom:-200px;left:-200px}
.tag{display:inline-block;align-self:flex-start;background:#1fb5a8;color:#0f2a4a;font-weight:700;
 font-size:38px;padding:14px 34px;border-radius:60px;letter-spacing:1px}
.num{position:absolute;top:110px;right:90px;font-size:36px;color:#9fc6d8;font-weight:500}
h1{font-size:118px;line-height:1.05;font-weight:700;margin-top:120px}
h2{font-size:78px;line-height:1.1;font-weight:700;margin-top:90px;color:#f2b632}
p{font-size:52px;line-height:1.45;margin-top:50px;font-weight:400}
.gold{color:#f2b632}.teal{color:#5fd8cc}
.box{margin-top:60px;background:rgba(255,255,255,.08);border:4px solid #1fb5a8;border-radius:36px;
 padding:56px 50px;font-size:66px;font-weight:600;text-align:center;line-height:1.5}
.box.warn{border-color:#f26b5b}
.small{font-size:44px;color:#c9dbe6}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:36px;color:#9fc6d8}
.foot b{color:#fff}
.swipe{font-size:44px;color:#f2b632;font-weight:600}
sup{font-size:.6em}
.strike{color:#ff8a7a}
"""

def page(body, tag, n, total):
    s = '<span class="swipe">Glisse →</span>' if n < total else '<span class="swipe">👇 En commentaire !</span>'
    return f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="blob b1"></div><div class="blob b2"></div>
<span class="tag">{tag}</span><span class="num">{n}/{total}</span>
{body}
<div class="foot"><span><b>Un Prof dans ta Poche</b><br>@1profdanstapoche</span>{s}</div>
</body></html>"""

async def main(fichier):
    posts = json.load(open(fichier, encoding="utf-8"))
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for post in posts:
            dossier = RACINE / post["date"]; dossier.mkdir(exist_ok=True)
            total = len(post["slides"])
            for i, body in enumerate(post["slides"], 1):
                await pg.set_content(page(body, post["tag"], i, total), wait_until="networkidle")
                png = dossier / f"{post['nom']}-{i}.png"
                await pg.screenshot(path=str(png))
                Image.open(png).convert("RGB").save(png.with_suffix(".jpg"), quality=85)
                png.unlink()
                print(png.with_suffix(".jpg"))
        await b.close()

asyncio.run(main(sys.argv[1]))
