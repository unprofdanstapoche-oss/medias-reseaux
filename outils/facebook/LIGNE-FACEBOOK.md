# Ligne éditoriale Facebook — Un Prof dans ta Poche

Page Facebook de Séverine, partagée dans les groupes locaux autour de Tonnay-Charente. Public : **parents** (pas les élèves).
Publication **manuelle** par Séverine dans Meta Business Suite (gratuit, illimité) → ne passe PAS par Metricool, n'utilise pas le quota.
Préparé chaque mois (le 24) pour le mois suivant, en même temps que les notions TikTok/Insta.

## DA
Ton pro mais cool et bienveillant. Fond crème, bleu / turquoise / jaune du logo, titres Lora, texte Poppins. Format 1080×1350.
Générateur : `outils/facebook/gabarit_fb.py` (types `pub`, `outil`, `citation`) ; exemple de contenu complet : `outils/facebook/novembre_2026.py`.
Pied de page fixe : cours à domicile Tonnay-Charente, Rochefort · visio partout · unprofdanstapoche.com.

## Rythme
- **Mercredi — « Ta pub »** (type `pub`) : une offre par semaine, en rotation : soutien maths et physique-chimie 6e–Terminale (bac pro compris) ; primaire CP–CM2 par le jeu et le matériel Montessori ; « votre enfant bloque ? » (confiance, bases) ; ateliers visio collectifs (ne jamais inventer de date ni de prix) ; cours en visio pour les familles éloignées ou à l'étranger ; stages pendant les vacances scolaires (sans date ni prix inventés). Appel à l'action : message privé.
- **Samedi — « Coulisse de prof »** (type `outil`) : présenter un outil ou une pratique pédagogique de Séverine, avec une illustration SVG dessinée. Idées déjà utilisables : soroban (boulier japonais), calculatrice Numworks, escape games pédagogiques qu'elle crée, jeu de calcul mental « CALCULO' DÉFI ! », barrettes de perles colorées Montessori, timbres Montessori, jeux de révision, fiches de révision, partir des passions de l'élève pour reformuler. **Ne jamais inventer d'histoire d'élève** : les récits d'accompagnement viennent uniquement de faits donnés par Séverine (anonymisés).
- **Dimanche — « La phrase de la semaine »** (type `citation`) : soit une citation dont l'auteur est **certain** (sinon s'abstenir), soit une phrase de Séverine signée « Séverine, Un Prof dans ta Poche » dans son style (encourageant : « tu en es capable », ne jamais rien lâcher, l'erreur fait partie de l'apprentissage). Alterner.

## Légendes
80–150 mots, phrases courtes, 2–4 emojis, vouvoiement des parents. Finir par la signature :
📍 Cours à domicile autour de Tonnay-Charente, Rochefort, Saint-Hippolyte et alentours, ou en visio.
💬 Une question ? Écrivez-moi en message privé !
👉 unprofdanstapoche.com

## Livraison
Images dans `facebook/<date>/<nom>.jpg`, contenu dans `facebook/AAAA-MM.json`. Page récap (artifact) : visuel, jour, type, légende avec bouton « Copier la légende », lien « Ouvrir l'image » (raw GitHub fixé sur le commit) et mode d'emploi Meta Business Suite (mercredi ~12 h, week-end ~10 h).

## Historique
- 2026-11 : pubs (soutien 6e–Tale, primaire par le jeu, « ça bloque », ateliers visio) ; coulisses (perles dorées, cartachari, chaîne de 100, partir du vécu – histoire réelle du pistolet) ; phrases (Montessori « Aide-moi à faire seul », « L'erreur est une étape », Mandela, « Être pédagogue… »).
