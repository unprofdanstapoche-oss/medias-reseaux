"""Contenu du pack Facebook de décembre 2026 -> facebook/2026-12.json (+ 2026-12-a-rendre.json)"""
import json, pathlib

GRAD = ('<defs><radialGradient id="gg" cx="35%" cy="35%"><stop offset="0" stop-color="#ffe9a8"/>'
        '<stop offset=".6" stop-color="#e0a526"/><stop offset="1" stop-color="#a8740c"/></radialGradient></defs>')

def svg_soroban():
    """Soroban : 1 perle du haut = 5, 4 perles du bas = 1 chacune. Affiche 2 0 2 6."""
    chiffres = [2, 0, 2, 6]
    s = '<svg width="900" height="330" xmlns="http://www.w3.org/2000/svg">'
    s += ('<rect x="150" y="10" width="600" height="300" rx="20" fill="#8a5a2b"/>'
          '<rect x="172" y="30" width="556" height="260" rx="10" fill="#fbf1dc"/>'
          '<rect x="172" y="105" width="556" height="12" fill="#8a5a2b"/>')
    for i, c in enumerate(chiffres):
        x = 250 + i * 133
        s += f'<line x1="{x}" y1="30" x2="{x}" y2="290" stroke="#6b4a2a" stroke-width="5"/>'
        # perle du haut (5) : contre la barre si active
        yh = 85 if c >= 5 else 52
        s += f'<ellipse cx="{x}" cy="{yh}" rx="46" ry="19" fill="#1f5fa8"/>'
        n = c % 5
        for k in range(4):
            if k < n:   # actives : collées sous la barre
                y = 138 + k * 38
            else:       # inactives : en bas
                y = 276 - (3 - k) * 38
            s += f'<ellipse cx="{x}" cy="{y}" rx="46" ry="17" fill="{"#f2b632" if k < n else "#1fb5a8"}"/>'
    s += ('<text x="80" y="90" font-family="Poppins" font-weight="700" font-size="30" fill="#1f5fa8" text-anchor="middle">= 5</text>'
          '<text x="80" y="200" font-family="Poppins" font-weight="700" font-size="30" fill="#d39a14" text-anchor="middle">= 1</text>')
    s += '<text x="830" y="175" font-family="Lora" font-weight="700" font-size="54" fill="#1f5fa8" text-anchor="middle">2026</text>'
    return s + '</svg>'

def svg_timbres():
    """Timbres Montessori : vert = 1, bleu = 10, rouge = 100 (vert = 1 000)."""
    s = '<svg width="900" height="330" xmlns="http://www.w3.org/2000/svg">'
    groupes = [("#d6453d", "100", 2), ("#1f5fa8", "10", 3), ("#2e9e4f", "1", 4)]
    x = 20
    for col, val, nb in groupes:
        for k in range(nb):
            xx = x + (k % 2) * 105
            yy = 20 + (k // 2) * 105
            s += (f'<rect x="{xx}" y="{yy}" width="92" height="92" rx="10" fill="{col}"/>'
                  f'<text x="{xx+46}" y="{yy+60}" font-family="Poppins" font-weight="700" font-size="{34 if len(val) < 3 else 30}" '
                  f'fill="#fff" text-anchor="middle">{val}</text>')
        x += 230
    s += ('<text x="760" y="140" font-family="Poppins" font-weight="700" font-size="44" fill="#1d2b44" text-anchor="middle">=</text>'
          '<rect x="700" y="170" width="140" height="80" rx="14" fill="#fff" stroke="#f2b632" stroke-width="5"/>'
          '<text x="770" y="226" font-family="Lora" font-weight="700" font-size="50" fill="#1f5fa8" text-anchor="middle">234</text>')
    return s + '</svg>'

def svg_numworks():
    s = '<svg width="900" height="330" xmlns="http://www.w3.org/2000/svg">'
    # calculatrice
    s += ('<rect x="300" y="5" width="300" height="320" rx="28" fill="#fff" stroke="#1d2b44" stroke-width="5"/>'
          '<rect x="325" y="28" width="250" height="140" rx="8" fill="#1d2b44"/>')
    # courbe sur l'écran
    s += ('<line x1="335" y1="140" x2="565" y2="140" stroke="#56657a" stroke-width="2"/>'
          '<line x1="450" y1="38" x2="450" y2="160" stroke="#56657a" stroke-width="2"/>'
          '<path d="M345 50 Q450 230 555 50" stroke="#f2b632" stroke-width="5" fill="none"/>')
    # touches
    for r in range(3):
        for c in range(4):
            col = "#f07a2f" if (r == 0 and c == 3) else "#e6dfcf"
            s += f'<rect x="{332 + c*60}" y="{188 + r*44}" width="48" height="32" rx="8" fill="{col}"/>'
    # étiquettes
    s += ('<rect x="20" y="60" width="240" height="70" rx="14" fill="#1f5fa8"/>'
          '<text x="140" y="106" font-family="Poppins" font-weight="700" font-size="30" fill="#fff" text-anchor="middle">Python</text>'
          '<rect x="20" y="180" width="240" height="70" rx="14" fill="#1fb5a8"/>'
          '<text x="140" y="226" font-family="Poppins" font-weight="700" font-size="30" fill="#fff" text-anchor="middle">Graphiques</text>'
          '<rect x="640" y="120" width="240" height="70" rx="14" fill="#f2b632"/>'
          '<text x="760" y="166" font-family="Poppins" font-weight="700" font-size="28" fill="#1d2b44" text-anchor="middle">Mode examen</text>')
    return s + '</svg>'

def svg_barrettes():
    """Barrettes de perles colorées Montessori de 1 à 9 (code couleur classique)."""
    cols = ["#d6453d", "#2e9e4f", "#f08bb4", "#f2d23a", "#7cc6ec", "#9b6cc9", "#ffffff", "#8a5a2b", "#1f3f8a"]
    s = '<svg width="900" height="330" xmlns="http://www.w3.org/2000/svg">'
    r, pas = 13, 30
    for n in range(1, 10):
        y = 18 + (n - 1) * 35
        larg = n * pas
        x0 = 450 - larg / 2
        s += f'<line x1="{x0-4}" y1="{y+r}" x2="{x0+larg+4}" y2="{y+r}" stroke="#6b4a2a" stroke-width="3"/>'
        for i in range(n):
            s += f'<circle cx="{x0 + i*pas + pas/2}" cy="{y+r}" r="{r}" fill="{cols[n-1]}" stroke="#56657a" stroke-width="{2 if n == 7 else 1}"/>'
        s += f'<text x="{x0 - 30}" y="{y+r+9}" font-family="Poppins" font-weight="700" font-size="24" fill="#1f5fa8" text-anchor="middle">{n}</text>'
    return s + '</svg>'

APPEL = "💬 Écrivez-moi en message privé !"
SIGNATURE = ("\n\n📍 Cours à domicile autour de Tonnay-Charente, Rochefort, Saint-Hippolyte et alentours, ou en visio.\n"
             "💬 Une question ? Écrivez-moi en message privé !\n📞 07 56 92 56 73 · ✉️ unprofdanstapoche@gmail.com\n👉 unprofdanstapoche.com")
SIGN_ATELIERS = "\n\n📩 Inscriptions en message privé ou au 07 56 92 56 73 !\n✉️ unprofdanstapoche@gmail.com\n👉 unprofdanstapoche.com"

posts = [
 # ---------- Mercredis : ta pub ----------
 {"date": "2026-12-02", "nom": "pub-visio-partout", "type": "pub", "tag": "📣 Cours en visio",
  "titre": "Loin de chez nous ?<br><span>Je viens à l'écran</span>", "sous_titre": "Pour les familles éloignées ou installées à l'étranger",
  "points": ["Des cours <b>en visio</b>, où que vous soyez",
             "Le <b>programme français</b> de l'Éducation nationale",
             "La même méthode <b>bienveillante</b> qu'à domicile",
             "Maths et physique-chimie, <b>du CP à la Terminale</b>"],
  "appel": APPEL,
  "legende": "🌍 Vous vivez loin de la Charente-Maritime, ou même à l'étranger ?\n\n"
             "Bonne nouvelle : mes cours se font aussi en visio ! Votre enfant garde un lien avec le programme français, "
             "avec une enseignante qui prend le temps de comprendre où ça coince. 💻\n\n"
             "On travaille ensemble à l'écran, pas à pas, avec la même bienveillance qu'à la maison. "
             "Seule chose à prévoir : une bonne connexion… et l'envie d'avancer ! 💪" + SIGNATURE},
 {"date": "2026-12-09", "nom": "pub-ateliers-epreuve-anticipee", "type": "pub", "tag": "📣 Les ateliers du dimanche",
  "titre": "Épreuve anticipée<br>de maths : <span>on s'y met !</span>", "sous_titre": "Pour les élèves de 1re, en visio le dimanche",
  "points": ["Le dimanche de <b>18 h à 19 h</b>, sur <b>Google Meet</b>",
             "On revoit <b>l'essentiel</b>, sans stress",
             "On s'entraîne sur des <b>sujets types</b>",
             "<b>7,80 €</b> la séance d'1 h : petit budget !"],
  "appel": "📩 Inscriptions en message privé !",
  "legende": "📣 Votre enfant est en 1re ? L'épreuve anticipée de maths, ça se prépare tranquillement, dès maintenant !\n\n"
             "Chaque dimanche de 18 h à 19 h, je propose un atelier en visio sur Google Meet, en petit groupe. "
             "Au programme : on revoit l'essentiel, on s'entraîne sur des sujets types et on gagne en méthode. 📐\n\n"
             "Petit budget pour petit coef : 7,80 € la séance d'une heure. "
             "Pas besoin d'adorer les maths pour venir, juste l'envie de progresser ! 💪" + SIGN_ATELIERS},
 {"date": "2026-12-16", "nom": "pub-stages-vacances", "type": "pub", "tag": "📣 Pendant les vacances",
  "titre": "Les vacances,<br>pour <span>consolider</span>", "sous_titre": "Des stages pendant les vacances scolaires",
  "points": ["On revoit les notions <b>qui coincent</b>",
             "On repart avec <b>de la méthode</b>",
             "On reprend <b>confiance</b> avant la rentrée",
             "À domicile ou <b>en visio</b>"],
  "appel": "📅 Infos et disponibilités en message privé !",
  "legende": "🎄 Les vacances de Noël approchent ! Un moment pour souffler… et pourquoi pas pour consolider en douceur ?\n\n"
             "Je propose des stages pendant les vacances scolaires : quelques séances pour reprendre une notion qui coince, "
             "retrouver de la méthode et repartir confiant à la rentrée. ✨\n\n"
             "Tout se fait à votre rythme, à domicile ou en visio, en gardant du temps pour profiter des fêtes ! "
             "Écrivez-moi pour connaître mes disponibilités. 😊" + SIGNATURE},
 {"date": "2026-12-23", "nom": "pub-bulletin-trimestre", "type": "pub", "tag": "📣 Parents, pas de panique",
  "titre": "Le bulletin<br>du <span>1er trimestre</span>…", "sous_titre": "…n'est qu'un point de départ !",
  "points": ["On lit le bulletin <b>ensemble</b>, sans dramatiser",
             "On repère <b>les notions à reprendre</b>",
             "On fixe des <b>petits objectifs</b> atteignables",
             "On démarre le 2e trimestre <b>en confiance</b>"],
  "appel": APPEL,
  "legende": "📄 Le bulletin du 1er trimestre est arrivé et les maths ou la physique-chimie vous inquiètent ?\n\n"
             "Pas de panique : un bulletin, ce n'est pas un verdict, c'est une photo à un moment donné. 📸\n\n"
             "Ensemble, on repère les notions à reprendre, on se fixe de petits objectifs atteignables, "
             "et on aborde le 2e trimestre avec méthode et confiance. Chaque progrès compte, et ça se voit vite ! 💪\n\n"
             "Joyeuses fêtes à toutes les familles 🎄" + SIGNATURE},
 {"date": "2026-12-30", "nom": "pub-ateliers-cap-bacpro", "type": "pub", "tag": "📣 Les ateliers du dimanche",
  "titre": "CAP, bac pro :<br>les maths <span>en confiance</span>", "sous_titre": "Des ateliers en visio, en petit groupe",
  "points": ["<b>10 h – 11 h</b> : on prépare le <b>CAP</b>",
             "<b>13 h – 14 h</b> : on prépare l'épreuve du <b>bac pro</b>",
             "On s'entraîne sur des <b>sujets types</b>",
             "Sur <b>Google Meet</b> · <b>7,80 €</b> la séance d'1 h"],
  "appel": "📩 Infos et inscriptions en MP !",
  "legende": "✨ Nouvelle année, nouvelles bonnes habitudes ! Votre enfant prépare un CAP ou un bac pro ?\n\n"
             "Les ateliers maths du dimanche sont faits pour lui : en visio sur Google Meet, en petit groupe, "
             "on revoit l'essentiel et on s'entraîne sur des sujets types. 💻\n\n"
             "🕙 10 h – 11 h : on prépare le CAP\n🕐 13 h – 14 h : on prépare l'épreuve du bac pro\n\n"
             "Petit budget pour petit coef : 7,80 € la séance d'une heure. Belle fin d'année à tous ! 🎉" + SIGN_ATELIERS},
 # ---------- Samedis : coulisse de prof ----------
 {"date": "2026-12-05", "nom": "coulisse-soroban", "type": "outil", "tag": "✨ Coulisse de prof",
  "titre": "Le <span>soroban</span>", "sous_titre": "Le boulier japonais qui muscle le calcul mental",
  "illustration": svg_soroban(),
  "points": ["Chaque tige est un rang : <b>unités, dizaines…</b>",
             "La perle du haut vaut <b>5</b>, celles du bas <b>1</b>.",
             "On calcule <b>avec les doigts</b>… puis dans sa tête !"],
  "legende": "✨ Coulisse de prof : le soroban\n\n"
             "Le soroban, c'est le boulier japonais. Sur chaque tige, une perle en haut qui vaut 5 et quatre perles en bas "
             "qui valent 1 chacune. Et chaque tige correspond à un rang : unités, dizaines, centaines… 🧮\n\n"
             "En faisant glisser les perles, l'enfant voit vraiment ce qui se passe quand on ajoute, qu'on retire "
             "ou qu'on fait une retenue. Petit à petit, il imagine le boulier dans sa tête : "
             "c'est un formidable entraînement au calcul mental !" + SIGNATURE},
 {"date": "2026-12-12", "nom": "coulisse-timbres", "type": "outil", "tag": "✨ Coulisse de prof",
  "titre": "Les <span>timbres</span><br>Montessori", "sous_titre": "Des petits carrés de couleur pour poser les opérations",
  "illustration": svg_timbres(),
  "points": ["Vert = <b>unité</b>, bleu = <b>dizaine</b>, rouge = <b>centaine</b>.",
             "On échange <b>10 timbres</b> contre 1 du rang supérieur.",
             "Le pont idéal <b>vers le calcul posé</b>."],
  "legende": "✨ Coulisse de prof : les timbres Montessori\n\n"
             "Après les perles dorées, place aux timbres ! Ce sont de petits carrés de couleur : "
             "vert pour les unités, bleu pour les dizaines, rouge pour les centaines. 🟩🟦🟥\n\n"
             "Avec eux, l'enfant pose additions, soustractions, multiplications et divisions. "
             "Quand il a 10 timbres verts, il les échange contre 1 bleu : la retenue n'est plus un mystère ! "
             "C'est l'étape idéale entre la manipulation et le calcul sur papier.\n\n"
             "Je les utilise du CP au CM2, toujours par le jeu. 🎲" + SIGNATURE},
 {"date": "2026-12-19", "nom": "coulisse-numworks", "type": "outil", "tag": "✨ Coulisse de prof",
  "titre": "La calculatrice<br><span>Numworks</span>", "sous_titre": "Une alliée du lycée… si on sait s'en servir !",
  "illustration": svg_numworks(),
  "points": ["Tracer une <b>courbe</b> pour vérifier un calcul.",
             "Écrire ses premiers <b>programmes en Python</b>.",
             "Savoir activer le <b>mode examen</b> le jour J."],
  "legende": "✨ Coulisse de prof : la calculatrice Numworks\n\n"
             "Au lycée, la calculatrice devient un vrai outil de travail. Encore faut-il savoir s'en servir ! 🧮\n\n"
             "En séance, j'apprends aux élèves à tracer une courbe pour vérifier un résultat, "
             "à écrire de petits programmes en Python, et à activer le mode examen pour être serein le jour de l'épreuve.\n\n"
             "Objectif : que la calculatrice aide à comprendre, et ne remplace jamais la réflexion. 💡\n\n"
             "Bonnes vacances à tous ! 🎄" + SIGNATURE},
 {"date": "2026-12-26", "nom": "coulisse-barrettes-couleur", "type": "outil", "tag": "✨ Coulisse de prof",
  "titre": "Les barrettes<br>de <span>perles colorées</span>", "sous_titre": "Une couleur pour chaque nombre, de 1 à 9",
  "illustration": svg_barrettes(),
  "points": ["Chaque nombre a <b>sa couleur</b> et sa longueur.",
             "On <b>compare</b>, on assemble, on compose 10.",
             "Le nombre devient <b>visible et concret</b>."],
  "legende": "✨ Coulisse de prof : les barrettes de perles colorées\n\n"
             "Rouge pour 1, vert pour 2, rose pour 3, jaune pour 4… jusqu'au bleu foncé pour 9 ! "
             "Dans le matériel Montessori, chaque nombre a sa barrette, avec sa couleur et sa longueur. 🌈\n\n"
             "L'enfant voit tout de suite que 7 est plus long que 4, il assemble 6 et 4 pour faire 10, "
             "il prépare les tables de multiplication… Le nombre n'est plus un simple symbole : "
             "il se touche et se compare.\n\n"
             "Un joli matériel, comme des guirlandes de fêtes, pour apprendre en s'amusant ! ✨" + SIGNATURE},
 # ---------- Dimanches : phrase de la semaine ----------
 {"date": "2026-12-06", "nom": "phrase-montaigne", "type": "citation",
  "citation": "« Plutôt la tête bien faite que bien pleine. »", "auteur": "Montaigne, Essais",
  "note": "Comprendre plutôt qu'empiler : c'est ce qui reste pour la vie.<br><b>Bonne semaine à tous ! 💛</b>",
  "legende": "🌱 La phrase de la semaine\n\n« Plutôt la tête bien faite que bien pleine. » – Montaigne, Essais\n\n"
             "Apprendre par cœur une formule, c'est bien. Comprendre d'où elle vient et savoir s'en servir, c'est mieux ! "
             "C'est ce que je cherche à chaque séance : donner du sens, pour que les connaissances restent. 🧠\n\n"
             "Belle semaine à tous 💛" + SIGNATURE},
 {"date": "2026-12-13", "nom": "phrase-capable", "type": "citation",
  "citation": "« Tu en es capable. Il te faut juste le temps de le découvrir. »", "auteur": "Séverine, Un Prof dans ta Poche",
  "note": "Chacun avance à son rythme : l'important, c'est d'avancer.<br><b>Bonne semaine à tous ! 💛</b>",
  "legende": "🌱 La phrase de la semaine\n\nTu en es capable. Il te faut juste le temps de le découvrir.\n\n"
             "Je le dis souvent à mes élèves : on n'apprend pas tous à la même vitesse, et ce n'est pas grave. "
             "Ce qui compte, c'est d'y croire et de continuer, un petit pas après l'autre. 💪\n\n"
             "Belle semaine à tous 💛" + SIGNATURE},
 {"date": "2026-12-20", "nom": "phrase-la-fontaine", "type": "citation",
  "citation": "« Rien ne sert de courir ; il faut partir à point. »", "auteur": "Jean de La Fontaine, Le Lièvre et la Tortue",
  "note": "Un peu chaque jour vaut mieux qu'une nuit de révisions.<br><b>Bonnes vacances à tous ! 🎄</b>",
  "legende": "🌱 La phrase de la semaine\n\n« Rien ne sert de courir ; il faut partir à point. » – Jean de La Fontaine\n\n"
             "La tortue l'emporte grâce à sa régularité ! En maths aussi : un peu chaque jour vaut mieux "
             "que tout réviser la veille du contrôle. 🐢\n\n"
             "Les vacances commencent : profitez-en bien pour vous reposer. "
             "Et si l'envie vous prend, dix minutes de révision suffisent pour garder le rythme ! 🎄" + SIGNATURE},
 {"date": "2026-12-27", "nom": "phrase-ne-lache-rien", "type": "citation",
  "citation": "« Ne lâche rien : chaque petit pas compte. »", "auteur": "Séverine, Un Prof dans ta Poche",
  "note": "Merci pour cette belle année d'apprentissages !<br><b>Belles fêtes à tous ! 💛</b>",
  "legende": "🌱 La phrase de la semaine\n\nNe lâche rien : chaque petit pas compte.\n\n"
             "Une notion enfin comprise, un exercice réussi seul, un peu plus de confiance… "
             "Ce sont ces petits pas qui font les grandes réussites. ✨\n\n"
             "Merci aux élèves et aux parents pour leur confiance. "
             "Je vous souhaite de très belles fêtes de fin d'année 💛" + SIGNATURE},
]
for p in posts:  # espaces insécables autour des guillemets (pas de « » » orphelin)
    if "citation" in p:
        p["citation"] = p["citation"].replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")
posts.sort(key=lambda p: p["date"])

racine = pathlib.Path(__file__).resolve().parents[2]
json.dump(posts, open(racine / "facebook" / "2026-12.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
a_rendre = [p for p in posts if p["type"] != "existant"]
json.dump(a_rendre, open(racine / "facebook" / "2026-12-a-rendre.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(posts), len(a_rendre))
