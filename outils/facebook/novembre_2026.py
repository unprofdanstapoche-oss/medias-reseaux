"""Contenu du pack Facebook de novembre 2026 -> facebook/2026-11.json"""
import json, pathlib

GRAD = ('<defs><radialGradient id="gg" cx="35%" cy="35%"><stop offset="0" stop-color="#ffe9a8"/>'
        '<stop offset=".6" stop-color="#e0a526"/><stop offset="1" stop-color="#a8740c"/></radialGradient></defs>')

def svg_cartachari():
    paires = [("3 × 4", "12"), ("½", "0,5"), ("10²", "100")]
    s = '<svg width="900" height="330" xmlns="http://www.w3.org/2000/svg">'
    for i, (q, r) in enumerate(paires):
        y = 10 + i * 108
        s += (f'<rect x="60" y="{y}" width="230" height="90" rx="16" fill="#fff" stroke="#1f5fa8" stroke-width="5"/>'
              f'<text x="175" y="{y+60}" font-family="Poppins" font-weight="700" font-size="42" fill="#1f5fa8" text-anchor="middle">{q}</text>'
              f'<rect x="470" y="{y}" width="230" height="90" rx="16" fill="#fff" stroke="#f2b632" stroke-width="5"/>'
              f'<text x="585" y="{y+60}" font-family="Poppins" font-weight="700" font-size="42" fill="#1d2b44" text-anchor="middle">{r}</text>'
              f'<line x1="300" y1="{y+45}" x2="455" y2="{y+45}" stroke="#1fb5a8" stroke-width="6" stroke-dasharray="14 10"/>'
              f'<polygon points="455,{y+33} 470,{y+45} 455,{y+57}" fill="#1fb5a8"/>')
    s += ('<circle cx="800" cy="165" r="70" fill="#1fb5a8"/>'
          '<path d="M768 167 l22 22 l42 -48" stroke="#fff" stroke-width="13" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
          '<text x="800" y="275" font-family="Poppins" font-weight="600" font-size="26" fill="#2f6f6a" text-anchor="middle">Je vérifie seul !</text></svg>')
    return s

def svg_chaine():
    s = f'<svg width="920" height="330" xmlns="http://www.w3.org/2000/svg">{GRAD}'
    r, pas, seg = 7.5, 16, 10
    lg = pas * seg  # 160
    x0, ys = 30, [90, 250]
    # fil
    s += f'<path d="M{x0} {ys[0]} H{x0+5*(lg+12)-12} q40 0 40 80 q0 80 -40 80 H{x0}" stroke="#b9892a" stroke-width="3" fill="none"/>'
    for k in range(10):
        row = 0 if k < 5 else 1
        j = k if row == 0 else 9 - k
        xs = x0 + j * (lg + 12)
        for i in range(seg):
            cx = xs + i * pas + r if row == 0 else xs + lg - i * pas - r
            s += f'<circle cx="{cx}" cy="{ys[row]}" r="{r}" fill="url(#gg)"/>'
        # étiquette de dizaine à la fin du segment
        ex = xs + lg - 8 if row == 0 else xs + 8
        ey = ys[row] - 62 if row == 0 else ys[row] + 26
        s += (f'<rect x="{ex-30}" y="{ey}" width="60" height="38" rx="8" fill="#1f5fa8"/>'
              f'<text x="{ex}" y="{ey+28}" font-family="Poppins" font-weight="700" font-size="24" fill="#fff" text-anchor="middle">{(k+1)*10}</text>')
    return s + '</svg>'

def svg_pistolet():
    s = '<svg width="900" height="330" xmlns="http://www.w3.org/2000/svg">'
    s += '<line x1="40" y1="290" x2="860" y2="290" stroke="#2f6f6a" stroke-width="6" stroke-linecap="round"/>'
    for i, n in enumerate(["3", "7", "5", "9"]):
        x = 60 + i * 150
        s += (f'<rect x="{x}" y="130" width="110" height="160" rx="14" fill="#fff" stroke="#1f5fa8" stroke-width="5"/>'
              f'<text x="{x+55}" y="242" font-family="Lora" font-weight="700" font-size="96" fill="#1f5fa8" text-anchor="middle">{n}</text>')
    # carte qui tombe
    s += ('<g transform="rotate(28 720 290)"><rect x="660" y="130" width="110" height="160" rx="14" fill="#fff" stroke="#f2b632" stroke-width="5"/>'
          '<text x="715" y="242" font-family="Lora" font-weight="700" font-size="96" fill="#d39a14" text-anchor="middle">2</text></g>')
    # fléchette en mousse
    s += ('<g transform="rotate(12 770 80)"><rect x="560" y="64" width="150" height="30" rx="10" fill="#f07a2f"/>'
          '<rect x="706" y="62" width="40" height="34" rx="16" fill="#1f5fa8"/>'
          '<path d="M560 64 l-34 -14 v58 l34 -14 z" fill="#1fb5a8"/></g>'
          '<path d="M380 60 q60 -6 120 12" stroke="#f2b632" stroke-width="5" fill="none" stroke-dasharray="12 10"/>'
          '<text x="830" y="150" font-family="Poppins" font-weight="700" font-size="40" fill="#f07a2f" text-anchor="middle">Paf !</text>')
    return s + '</svg>'

APPEL = "💬 Une question ? Écrivez-moi en message privé !"
SIGNATURE = ("\n\n📍 Cours à domicile autour de Tonnay-Charente, Rochefort, Saint-Hippolyte et alentours, ou en visio.\n"
             "💬 Une question ? Écrivez-moi en message privé !\n👉 unprofdanstapoche.com")

posts = [
 {"date": "2026-11-04", "nom": "pub-soutien-college-lycee", "type": "pub", "tag": "📣 Mes accompagnements",
  "titre": "Les maths et la physique,<br><span>sans stress</span>", "sous_titre": "De la 6e à la Terminale, bac pro compris",
  "points": ["Cours à domicile <b>autour de Tonnay‑Charente</b>, ou en visio",
             "Une méthode qui part <b>de votre enfant</b> : ses besoins, ses passions",
             "Enseignante de l'Éducation nationale, <b>17 ans</b> d'expérience",
             "Des encouragements <b>à chaque séance</b> 💪"],
  "appel": APPEL,
  "legende": "Les maths ou la physique-chimie, c'est devenu une source de stress à la maison ? 😟\n\n"
             "J'accompagne les élèves de la 6e à la Terminale (bac pro compris), à domicile ou en visio. "
             "Mon objectif : comprendre où ça coince, reprendre les bases sans jugement, et redonner confiance. "
             "Quand un élève bloque, je reformule avec un exemple tiré de ce qu'il aime : le foot, la cuisine, les jeux vidéo… "
             "et ça change tout !" + SIGNATURE},
 {"date": "2026-11-07", "nom": "coulisse-perles", "type": "existant",
  "legende": "✨ Coulisse de prof : les perles dorées Montessori\n\n"
             "Dans mon sac de prof, il y a un trésor : les perles dorées ! 🟡\n\n"
             "Une perle, c'est une unité. Dix perles enfilées, une dizaine. Dix barres côte à côte, une centaine… "
             "et dix plaques empilées, un vrai cube de mille qu'on soulève à deux mains !\n\n"
             "Avec ce matériel, les enfants ne récitent plus « le chiffre des centaines » : ils le voient et le touchent. "
             "Les échanges (10 unités contre 1 dizaine), les additions avec retenue, les grands nombres… tout devient concret. 🙌\n\n"
             "Je l'utilise dans mes accompagnements du CP au CM2, avec une pédagogie par le jeu." + SIGNATURE},
 {"date": "2026-11-08", "nom": "phrase-aide-moi", "type": "citation",
  "citation": "« Aide-moi à faire seul. »", "auteur": "Maria Montessori",
  "note": "Accompagner, c'est donner à l'enfant les outils pour réussir… par lui-même.<br><b>Bonne semaine à tous ! 💛</b>",
  "legende": "🌱 La phrase de la semaine\n\n« Aide-moi à faire seul. » Cette phrase résume la pédagogie de Maria Montessori.\n\n"
             "Mon rôle n'est pas de faire à la place de l'élève, mais de lui donner les bons outils pour qu'il réussisse par lui-même. "
             "Et quelle fierté dans ses yeux quand il y arrive ! ✨\n\nBelle semaine à tous les élèves et à leurs parents 💛" + SIGNATURE},
 {"date": "2026-11-11", "nom": "pub-primaire-jeu", "type": "pub", "tag": "📣 Nouveau : école élémentaire",
  "titre": "Du CP au CM2 :<br><span>apprendre en jouant</span>", "sous_titre": "Lecture, calcul, confiance en soi",
  "points": ["Du <b>matériel Montessori</b> pour toucher les notions",
             "Des <b>jeux</b> pour s'entraîner avec plaisir",
             "Le <b>rythme de l'enfant</b> respecté",
             "17 ans d'expérience <b>en classe de primaire</b>"],
  "appel": APPEL,
  "legende": "📣 J'ouvre mes accompagnements à l'école élémentaire, du CP au CM2 !\n\n"
             "Après 17 ans en classe de primaire, je sais à quel point chaque enfant apprend à sa façon. "
             "Ma pédagogie : le jeu et le matériel Montessori, pour que les notions deviennent concrètes, "
             "et que l'enfant reprenne plaisir et confiance. 🎲🟡" + SIGNATURE},
 {"date": "2026-11-14", "nom": "coulisse-cartachari", "type": "outil", "tag": "✨ Coulisse de prof",
  "titre": "Les <span>cartachari</span>", "sous_titre": "Des cartes à associer qui se corrigent toutes seules",
  "illustration": svg_cartachari(),
  "points": ["L'élève <b>associe</b> chaque question à sa réponse.",
             "Il <b>vérifie seul</b>, sans attendre la correction.",
             "Je les crée <b>sur mesure</b>, du primaire au lycée."],
  "legende": "✨ Coulisse de prof : les cartachari\n\n"
             "Ce sont des cartes à associer : une question d'un côté, sa réponse de l'autre. "
             "Leur super-pouvoir ? Elles sont autocorrectives : l'élève vérifie lui-même s'il a juste. ✅\n\n"
             "Résultat : il ose essayer, il se trompe sans pression, il recommence… et il retient ! "
             "Je les fabrique sur mesure selon le niveau et la notion : tables de multiplication, fractions, ensembles de nombres au lycée…" + SIGNATURE},
 {"date": "2026-11-15", "nom": "phrase-erreur", "type": "citation",
  "citation": "« Une erreur, ce n'est pas un échec : c'est une étape pour apprendre. »", "auteur": "Séverine, Un Prof dans ta Poche",
  "note": "Chaque erreur nous montre où travailler. On avance ensemble !<br><b>Bonne semaine à tous ! 💛</b>",
  "legende": "🌱 La phrase de la semaine\n\nUne erreur, ce n'est pas un échec : c'est une étape pour apprendre.\n\n"
             "En séance, on ne cache pas ses erreurs : on les regarde, on les comprend, et on repart plus fort. "
             "C'est comme ça qu'on progresse vraiment. 💪\n\nBelle semaine à tous 💛" + SIGNATURE},
 {"date": "2026-11-18", "nom": "pub-ca-bloque", "type": "pub", "tag": "📣 Parents, ça vous parle ?",
  "titre": "Votre enfant <span>bloque</span><br>en maths ?", "sous_titre": "On avance ensemble, pas à pas",
  "points": ["On identifie <b>où ça coince</b>",
             "On reprend les bases <b>sans jugement</b>",
             "On retrouve <b>confiance</b> et méthode",
             "À domicile ou <b>en visio</b>"],
  "appel": APPEL,
  "legende": "« Je suis nul en maths. » Vous l'avez déjà entendu à la maison ? 😔\n\n"
             "Souvent, il suffit d'une notion mal comprise pour que tout s'enchaîne. "
             "Ensemble, on cherche où ça coince, on reprend les bases tranquillement, et on reconstruit la confiance. "
             "Personne n'est « nul en maths » : on n'a juste pas encore trouvé la bonne explication. 💡" + SIGNATURE},
 {"date": "2026-11-21", "nom": "coulisse-chaine-100", "type": "outil", "tag": "✨ Coulisse de prof",
  "titre": "La <span>chaîne de 100</span>", "sous_titre": "Compter jusqu'à 100… en le voyant !",
  "illustration": svg_chaine(),
  "points": ["10 barres de 10 perles <b>attachées bout à bout</b>.",
             "On compte et on pose une <b>étiquette à chaque dizaine</b>.",
             "Repliée, elle forme… <b>le carré de 100</b> !"],
  "legende": "✨ Coulisse de prof : la chaîne de 100\n\n"
             "Dix barres de dix perles dorées, attachées les unes aux autres. L'enfant la déroule, compte perle après perle "
             "et pose une étiquette à chaque dizaine : 10, 20, 30… jusqu'à 100 ! 🟡\n\n"
             "Il voit que 100, c'est long… et qu'en repliant la chaîne, on obtient exactement le carré de 100. "
             "Compter, se repérer, comprendre les dizaines : tout ça avec les mains." + SIGNATURE},
 {"date": "2026-11-22", "nom": "phrase-mandela", "type": "citation",
  "citation": "« L'éducation est l'arme la plus puissante qu'on puisse utiliser pour changer le monde. »", "auteur": "Nelson Mandela",
  "note": "Chaque notion comprise est un petit pas vers ce changement.<br><b>Bonne semaine à tous ! 💛</b>",
  "legende": "🌱 La phrase de la semaine\n\n« L'éducation est l'arme la plus puissante qu'on puisse utiliser pour changer le monde. » – Nelson Mandela\n\n"
             "Chaque notion comprise, chaque petite victoire en classe ou à la maison, c'est un pas de plus. "
             "Merci aux parents qui accompagnent leurs enfants chaque jour 🙏\n\nBelle semaine à tous 💛" + SIGNATURE},
 {"date": "2026-11-25", "nom": "pub-ateliers-visio", "type": "pub", "tag": "📣 Les ateliers visio",
  "titre": "Apprendre <span>à plusieurs</span>,<br>depuis la maison", "sous_titre": "Des séances collectives en ligne",
  "points": ["Premier thème : <b>le théorème de Pythagore</b>",
             "Pour les <b>4e, 3e</b> et les curieux",
             "En petit groupe, <b>on ose poser ses questions</b>",
             "Accessible <b>partout</b>, même à l'étranger"],
  "appel": "📅 Infos et inscriptions en message privé !",
  "legende": "📣 Les ateliers visio sont lancés !\n\n"
             "Des séances collectives en ligne, en petit groupe, pour travailler une notion ensemble. "
             "Premier thème : le théorème de Pythagore, pour les 4e, les 3e… et tous les curieux ! 📐\n\n"
             "À plusieurs, on ose poser ses questions, on s'entraide et on apprend dans la bonne humeur." + SIGNATURE},
 {"date": "2026-11-28", "nom": "coulisse-partir-du-vecu", "type": "outil", "tag": "✨ Coulisse de prof",
  "titre": "Partir du <span>vécu</span><br>de l'élève", "sous_titre": "Quand un pistolet de jeu aide à apprendre les chiffres",
  "illustration": svg_pistolet(),
  "points": ["Il n'arrivait pas à <b>retenir les chiffres</b>.",
             "Son trésor du moment : <b>son nouveau pistolet</b>.",
             "Le défi : <b>faire tomber les chiffres</b> dans le salon !"],
  "legende": "✨ Coulisse de prof : partir du vécu de l'élève\n\n"
             "J'ai accompagné un petit garçon qui n'arrivait pas à retenir les chiffres. Ce qu'il adorait à ce moment-là ? "
             "Son nouveau pistolet ! 🎯\n\nAlors je l'ai mis au défi : j'avais disposé des chiffres dans son salon, "
             "et il devait faire tomber celui que je lui annonçais. Il a pris un plaisir fou… "
             "et petit à petit, ce genre d'activité l'a aidé à les reconnaître et à les retenir.\n\n"
             "Être pédagogue, c'est savoir rebondir en permanence pour répondre aux besoins de chaque élève. 💛" + SIGNATURE},
 {"date": "2026-11-29", "nom": "phrase-rebondir", "type": "citation",
  "citation": "« Être pédagogue, c'est savoir rebondir en permanence pour répondre aux besoins de chaque élève. »",
  "auteur": "Séverine, Un Prof dans ta Poche",
  "note": "Chaque enfant est unique : à nous de trouver son chemin.<br><b>Bonne semaine à tous ! 💛</b>",
  "legende": "🌱 La phrase de la semaine\n\nÊtre pédagogue, c'est savoir rebondir en permanence pour répondre aux besoins de chaque élève.\n\n"
             "Il n'existe pas de méthode unique : il existe des enfants uniques. Mon métier, c'est de trouver la porte d'entrée de chacun. 🔑\n\n"
             "Belle semaine à tous 💛" + SIGNATURE},
]

# --- Mise à jour du 1er nov. : ateliers visio du dimanche (dès le 8/11) ---
POINTS_ATELIERS = ["<b>10 h – 11 h</b> : on prépare le <b>CAP</b>",
                   "<b>13 h – 14 h</b> : on prépare l'épreuve du <b>bac pro</b>",
                   "<b>18 h – 19 h</b> : on prépare l'<b>épreuve anticipée</b> de maths (1re)",
                   "En visio sur <b>Google Meet</b> · <b>7,80 €</b> la séance d'1 h"]
LEG_ATELIERS = ("📣 Nouveau : les ateliers maths du dimanche, en visio !\n\n"
                "Petit budget pour petit coef : 7,80 € la séance d'une heure, sur Google Meet, en petit groupe. 💻\n\n"
                "🕙 10 h – 11 h : on prépare le CAP\n"
                "🕐 13 h – 14 h : on prépare l'épreuve du bac pro\n"
                "🕕 18 h – 19 h : on prépare l'épreuve anticipée de maths de 1re\n\n"
                "Pas besoin d'adorer les maths pour venir : on revoit l'essentiel, on s'entraîne sur des sujets types "
                "et on repart avec de la méthode et de la confiance. 💪\n\n")
for p in posts:
    if p["nom"] == "pub-soutien-college-lycee":
        p["date"] = "2026-11-25"
posts = [p for p in posts if p["nom"] != "pub-ateliers-visio"]
posts.append({"date": "2026-11-04", "nom": "pub-ateliers-dimanche", "type": "pub", "tag": "📣 Les ateliers du dimanche",
  "titre": "Petit budget<br>pour <span>petit coef</span> !", "sous_titre": "Des ateliers maths en visio, dès le dimanche 8 novembre",
  "points": POINTS_ATELIERS, "appel": "📩 Inscriptions en message privé !",
  "legende": LEG_ATELIERS + "🚀 Premier rendez-vous : dimanche 8 novembre.\n📩 Inscriptions en message privé !\n👉 unprofdanstapoche.com"})
posts.append({"date": "2026-11-06", "nom": "rappel-ateliers-dimanche", "type": "pub", "tag": "⏰ C'est ce dimanche !",
  "titre": "Les ateliers<br>du <span>dimanche</span>", "sous_titre": "Dimanche 8 novembre, en visio sur Google Meet",
  "points": POINTS_ATELIERS, "appel": "📩 Il reste des places : écrivez-moi en MP !",
  "legende": "⏰ C'est ce dimanche ! Les ateliers maths en visio démarrent le 8 novembre.\n\n" + LEG_ATELIERS
             + "📩 Il reste des places : réservez en message privé !\n👉 unprofdanstapoche.com"})
posts.sort(key=lambda p: p["date"])

racine = pathlib.Path(__file__).resolve().parents[2]
json.dump(posts, open(racine / "facebook" / "2026-11.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
a_rendre = [p for p in posts if p["type"] != "existant"]
json.dump(a_rendre, open(racine / "facebook" / "2026-11-a-rendre.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(posts), len(a_rendre))
