# Reprendre la recherche sur W — état au 12 septembre 2026

La recherche est **en pause à la demande du mainteneur**. Ce dépôt publie
les résultats et les pistes disponibles pour permettre une reprise autonome.
La théorie effective complète de W n'est pas achevée. Les revues mentionnées
sont des revues internes assistées par IA, pas une validation externe.

## Ce qui est acquis dans le dossier

- La non-D-finitude de W : [preuve](proofs/W_NON_DFINITE.md).
- M8 : six pôles certifiés, aux indices 32, 64, 128, 256, 512 et 1024,
  avec encadrements de dérivées et de résidus.
- M9 : existence et unicité pour tous les indices N >= 10^27, avec
  estimations quantitatives de position et de résidu.
- M12 : absence d'annulation au zéro du dénominateur dans les secteurs étudiés.
- M13 : F_theta < -1/25 pour tout entier N >= 32 et theta dans [4/5, 9/10].
  Chaque bande contient donc **au plus un** zéro, simple s'il existe.
  Cela ne prouve pas l'existence dans toutes les bandes.

Voir [le bilan détaillé](W_THEORY_PROGRESS.md),
[les obligations complètes](W_THEORY_PLAN.md),
[la preuve M13](proofs/M13_UNIFORM_PHASE_DERIVATIVE.md) et
[sa clôture interne](results/m13-closure-review.md).
Les anciens documents d'étape restent présents comme historique.

## Frontière ouverte : M14

La piste actuelle vise des signes opposés du dénominateur aux deux bords
pour **tous N >= 512**. Ce seuil est un objectif de la preuve candidate,
**pas un théorème accepté**. Aucun paquet canonique M14 complet n'existe.

Ordre de lecture et statut :

| Composant | Fichier dans proofs/ | État à la pause |
|---|---|---|
| Marges critiques et référence dirigée | M14_ENDPOINT_MARGIN_TRANSFER.md | Revue interne du composant disponible |
| Variation critique et déplacement du noyau | M14_CRITICAL_VARIATION.md | Revue interne du composant disponible |
| Transfert du poids combiné | M14_COMBINED_WEIGHT_TRANSFER.md | Revue interne, conclusion conditionnelle |
| Encadrement Gamma des primitives | M14_GAMMA_BLOCK_ENVELOPE.md | Revue interne du composant disponible |
| Produit lisse | M14_SMOOTH_ENVELOPE.md | Candidat, revue indépendante non terminée |
| Comparaison intégrée des masses | M14_WEIGHTED_MASS_COMPARISON.md | Candidat, revue indépendante non terminée |

Les scripts m14_*.py associés vérifient des calculs exacts. Un résultat
PASS ne valide pas à lui seul les hypothèses analytiques, les échanges de
limites ou toute la preuve. Les indicateurs `claims` ne sont pas des preuves.

## Prochaines tâches concrètes

1. Relire indépendamment le lemme du produit lisse, notamment la borne
   abs(log K_e,n - log K0(ne)) < e*(17/8 + 20*n*e), uniformément en n.
2. Auditer la comparaison des masses : singularité Gamma, voisinage de
   zéro, translation de la primitive, queue infinie et constantes.
   Si ces étapes passent, intégrer les signes aux deux bords pour N >= 512.
3. Construire les certificats d'existence pour **chaque entier 32 <= N <= 511**,
   avec arithmétique d'intervalles et queues complètes. Réutiliser
   proofs/m7_finite_poles.py et les outils de phase M10. Le producteur de
   cette campagne n'a pas été livré et aucune campagne de 480 indices
   n'a été exécutée. Les six certificats existants ne remplacent pas cela.
4. Geler les sources corrigées, produire de nouveaux reçus et faire une
   clôture indépendante vérifiant toutes les obligations du plan.

Ne pas modifier les sources acceptées pour faire correspondre un ancien
reçu. Utiliser de nouveaux fichiers et identifiants pour les nouveaux résultats.

## Installation et vérification

Depuis un clone du dépôt, avec Python 3.12 :

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/check_public_snapshot.py
.venv/bin/python -m pytest -q
.venv/bin/python publication/reproduce.py
.venv/bin/python publication/reproduce_w.py
PYTHONPATH=. .venv/bin/python -m proofs.m14_critical_variation
PYTHONPATH=. .venv/bin/python -m proofs.m14_combined_weight_transfer
PYTHONPATH=. .venv/bin/python -m proofs.m14_gamma_block_bounds
PYTHONPATH=. .venv/bin/python -m proofs.m14_smooth_envelope
PYTHONPATH=. .venv/bin/python -m proofs.m14_weighted_mass_bounds
PYTHONPATH=. .venv/bin/python -m proofs.m14_endpoint_margins
```

Les reçus historiques conservent les empreintes et identifiants de commits
originaux. Les vérificateurs qui utilisent `git show` sur cet historique
privé ne fonctionnent pas directement dans l'export public. Le manifeste
public vérifie les fichiers exportés ; les deux commandes `reproduce`
fournissent les relectures arithmétiques portables J/W. Cela ne constitue
pas une revalidation complète portable de M5–M13. Pour de nouvelles
expériences, créer un commit public des sources et de nouveaux reçus.

Une contribution utile peut être une correction précise, une relecture
annotée, un vérificateur portable ou un certificat manquant. Indiquer
le commit étudié, la commande, les dépendances et la portée exacte du résultat.
Aucun résultat ici ne donne la constante connective exacte du réseau carré.
