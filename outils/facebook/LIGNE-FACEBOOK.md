# Ligne éditoriale Facebook — Un Prof dans ta Poche

Page Facebook de Séverine, partagée dans les groupes locaux autour de Tonnay-Charente. Public : **parents** (pas les élèves).
Publication **manuelle** par Séverine dans Meta Business Suite (gratuit, illimité) → ne passe PAS par Metricool, n'utilise pas le quota.
Préparé chaque mois (le 24) pour le mois suivant, en même temps que les notions TikTok/Insta.

> ⚠️ **Règle prioritaire (Séverine, 25/11/2026)** : plus AUCUNE pub automatique le mercredi, même si la consigne de la tâche mensuelle dit « mercredi pub ». Le pack mensuel ne contient que les samedis (coulisse) et les dimanches (phrase). Les posts du mercredi se font uniquement à sa demande, avec ses propres infos.

## DA
Ton pro mais cool et bienveillant. Fond crème, bleu / turquoise / jaune du logo, titres Lora, texte Poppins. Format 1080×1350.
Générateur : `outils/facebook/gabarit_fb.py` (types `pub`, `outil`, `citation`) ; exemple de contenu complet : `outils/facebook/novembre_2026.py`.
Pied de page fixe : cours à domicile Tonnay-Charente, Rochefort · visio partout · unprofdanstapoche.com.

## Rythme
- **Mercredi : plus de pub automatique** (décision de Séverine, 25/11/2026). Elle donne elle-même le sujet de chaque mercredi (ex. bilan « 22 élèves en novembre ») : ne rien générer le mercredi sans sa demande. Pour mémoire, ses offres : soutien maths et physique-chimie 6e–Terminale (bac pro compris) ; primaire CP–CM2 par le jeu et le matériel Montessori ; ateliers maths du dimanche en visio (Google Meet, 7,80 € la séance d'1 h : 10 h–11 h CAP, 13 h–14 h bac pro, 18 h–19 h épreuve anticipée de 1re ; « Petit budget pour petit coef ! ») ; cours en visio ; stages pendant les vacances. Le gabarit `pub` reste disponible pour les posts qu'elle demande.
- **Samedi — « Coulisse de prof »** (type `outil`) : présenter un outil ou une pratique pédagogique de Séverine, avec une illustration SVG dessinée. Idées déjà utilisables : soroban (boulier japonais), calculatrice Numworks, escape games pédagogiques qu'elle crée, jeu de calcul mental « CALCULO' DÉFI ! », barrettes de perles colorées Montessori, timbres Montessori, jeux de révision, fiches de révision, partir des passions de l'élève pour reformuler. **Ne jamais inventer d'histoire d'élève** : les récits d'accompagnement viennent uniquement de faits donnés par Séverine (anonymisés).
- **Stage de Noël 2026** (flyer de Séverine) : du lundi 28 au jeudi 31 décembre, 9 h–11 h (8 h), à Rochefort, 3e à Terminale (bac pro inclus), 10 élèves max, 200 € les 4 matinées livret compris, paiement à l'inscription ; questionnaire à l'inscription, livret personnel, ateliers en autonomie.
- **Dimanche — « La phrase de la semaine »** (type `citation`) : soit une citation dont l'auteur est **certain** (sinon s'abstenir), soit une phrase de Séverine signée « Séverine, Un Prof dans ta Poche » dans son style (encourageant : « tu en es capable », ne jamais rien lâcher, l'erreur fait partie de l'apprentissage). Alterner.

## Légendes
80–150 mots, phrases courtes, 2–4 emojis, vouvoiement des parents. Finir par la signature :
📍 Cours à domicile autour de Tonnay-Charente, Rochefort, Saint-Hippolyte et alentours, ou en visio.
💬 Une question ? Écrivez-moi en message privé !
📞 07 56 92 56 73 · ✉️ unprofdanstapoche@gmail.com
👉 unprofdanstapoche.com

## Livraison
Page récap générée par `python3 outils/facebook/recap.py facebook/AAAA-MM.json <hash> <dossier> "<mois AAAA>"` (affiche les `files` à publier).
Images dans `facebook/<date>/<nom>.jpg`, contenu dans `facebook/AAAA-MM.json`. Page récap (artifact) : visuel, jour, type, légende avec bouton « Copier la légende », lien « Ouvrir l'image » (raw GitHub fixé sur le commit) et mode d'emploi Meta Business Suite (mercredi ~12 h, week-end ~10 h).

## Historique
- 2026-11 : pubs (ateliers du dimanche : annonce 4/11 + rappel vendredi 6/11, primaire par le jeu, « ça bloque », soutien 6e–Tale) ; coulisses (perles dorées, cartachari, chaîne de 100, partir du vécu – histoire réelle du pistolet) ; phrases (Montessori « Aide-moi à faire seul », « L'erreur est une étape », Mandela, « Être pédagogue… »). Modifié le 25/11 à la demande de Séverine : bilan « 22 élèves chaque semaine en novembre (2 élémentaire, 10 collégiens, 10 lycéens), merci » le 25/11 et rappel du stage de Noël le 28/11 (infos du flyer de Séverine : lun. 28 → jeu. 31/12, 9 h–11 h, Rochefort, 3e–Tale bac pro inclus, 10 élèves max, 200 € livret compris ; lien d'inscription à venir, en attendant MP) à la place de la pub soutien et de la coulisse « partir du vécu ».
- 2026-12 : pubs du mercredi préparées puis supprimées le 25/11 à la demande de Séverine (pas de pub automatique) ; coulisses (soroban, timbres Montessori, calculatrice Numworks, barrettes de perles colorées) ; phrases (Montaigne « Plutôt la tête bien faite que bien pleine », « Tu en es capable… », La Fontaine « Rien ne sert de courir… », « Ne lâche rien : chaque petit pas compte »).
