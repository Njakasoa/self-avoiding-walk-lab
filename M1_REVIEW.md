# M1 — Reproducible Lab : revue d'acceptation

**M1 validé dans le périmètre ci-dessous.** Revue scientifique indépendante
Astra/low favorable après correction et rejeu des10tests. Les résultats sont
des reproductions KNOWN, sans nouvelle borne record ni formule exacte du carré.
La mission de découverte M2–M4 reste ouverte.

## Exigences et preuves

| Exigence M1 | Preuve livrée | Statut / limite |
|---|---|---|
| Environnement réellement audité | ENVIRONMENT_AUDIT.md, environment/audit.json | WSL2/CPU/RAM/venv/C++/Git/web/PDF mesurés; SSD physique et backend root non attestés |
| Orchestration vérifiée | .codex, .agents, ORCHESTRATION_LOG.md | Quatre tâches initiales réalisées en deux vagues; Luna/max et Astra/low explicitement appelés |
| Définitions alignées | NORMALIZATION.md | n=arêtes, origine fixée, orientation conservée, bridges strict/weak, objets pondérés définis |
| Bibliographie actuelle | STATE_OF_THE_ART.md, references/ | Recherche jusqu'au2026-09-12; distinction publication/préprint, limites d'exhaustivité |
| Référence indépendante | src/reference_enumerator.py, tests/test_independent_m1.py | n≤14 Python; tester direction words/bitmask et données OEIS |
| Énumérateur optimisé | src/optimized_enumerator.cpp | n≤20 confronté à OEIS; domaine commun n≤14; rotation×4 et sûreté128bits |
| Bridges / irréductibles / spans | src/bridges.py, proofs/BRIDGE_RENEWAL.md | n≤12; revue Astra recalcule toute la géométrie, facteur de renewal et intervalles rationnels |
| Méthode basse connue | dictionnaire d'irréductibles; famille analytique span1 | μ≥1+√2 comme contrôle classique; dictionnaire12 donne μ≥2.516941 arrondi vers le bas |
| Petite borne spectrale | src/automaton.py, proofs/check_certificates.py | m1…8; entier/rationnel exact; m7/8 donnent μ≤2.744459 arrondi vers le haut |
| Petite TM et comparaison | src/transfer_matrix.py,src/connectivity_tm.py | Deux représentations, toutes deux égales au DFS dans7rectangles jusqu'à3×4; conserve tout le domaine, pas de frontier compétitive |
| Méthode haute connue | proofs/FINITE_MEMORY.md | Petits k4/6/8 concordent avec Pönitz–Tittmann; pas de reproduction de Couronné430M états |
| Contrôle honeycomb | proofs/HONEYCOMB.md, experiments/honeycomb_control.py | Deux annulations locales exactes et mutant rejeté; partie globale lue/revue, non formalisée informatiquement |
| Revue indépendante | Astra/low : suite, géométrie, preuves, hashes | Acceptation scientifique bornée, validité≠nouveauté |

## Expériences canoniques

| Expérience | Commit source | Résultat |
|---|---|---|
| m1-certificates-v1 | 0840c52 | Premier certificat conservé avec ses sources historiques |
| m1-certificates-v2 | cb9d1f8 | Rejeu final après validation des booléens; mêmes données scientifiques |
| m1-enumeration-v1 | 61b85b1 | c₂₀=897697164; références/TM concordantes |
| honeycomb-control-v1 | 61b85b1 | Trois restes cyclotomiques nuls; phase mutante non nulle |

Chaque metadata.json contient le hash Git complet, les empreintes des entrées et
sorties, l'UTC, la commande, les paramètres, le temps et le matériel. Les sources
sont comparées octet par octet à leur commit avant calcul. Des documents peuvent
avoir évolué ensuite; les anciennes expériences restent vérifiables via Git.
Le champ producer verification_status réserve explicitement une vérification
séparée; la présente revue et les reçus de vérification en documentent l'issue.

## Falsification et correction

Le tester et le reviewer ont trouvé une anomalie d'API : True accepté comme
taille entière dans deux fonctions Python. Corrigé par type(x) is int.
La suite indépendante complète passe ensuite :10tests. Aucun compte à argument
entier ni certificat mathématique n'était affecté. Le défaut et sa correction
restent dans l'historique au lieu de cacher le test initialement échoué.

Le vérificateur spectral reconstruit l'ensemble complet des états et les
transitions géométriques; il ne fait pas confiance à une matrice arbitraire.
Il vérifie Av≤Uv exactement. Sa partie bridge contrôle l'algèbre et les signes;
la géométrie est validée par le tester et le recalcul Astra distinct. Les
certificats modifiés sont testés négativement dans la suite.

## Interprétation et limites

Sur n14, mesure unique Python1.1019s/C++0.00459s; C++ n20≈1.196s. Cela justifie
C++ ici sans invoquer GPU ou jours de calcul. Les bandes finies servent aux
invariants; aucune limite de strip infini n'en est déduite.

Les grandes bornes de la littérature n'ont pas été recomputées. La précision
spectrale du record Couronné est une limite de reproduction explicitement
signalée. La TTM topologique et la TM comprimée de Jensen sont étudiées dans
les sources mais non implémentées à grande échelle. La preuve honeycomb entière
est comprise et revue sur texte, pas certifiée par le test local seul.

Niveau5 applicable aux deux petits résultats des dossiers CLAIM-0001/0002 :
preuve écrite, calcul exact, vérification indépendante et revue. Ce niveau ne
s'étend ni aux records cités, ni à de nouveaux théorèmes, ni à la priorité.
M2 n'est pas déclaré accompli : pas encore de moteur multidimensionnel ni
observation découverte automatiquement. M3/M4 non atteints.

## Clôture de validation canonique

results/m1-validation-v1, sourceebfed56 :10tests passent en3.77s;
31entrées de provenance historique vérifiées, quatre payloads vérifiés, v1/v2
scientifiquement identiques. Les décimales conservatrices2.516941 et2.744459
ont aussi été comparées aux rationnels exacts dans le bon sens. Rapports
indépendants : results/tester-report.md et results/astra-review.md. L'ancien
rapport tester décrit son worktree intermédiaire; le reçu canonique final fixe
sans ambiguïté toutes les sources exécutées. Aucun point bloquant M1 restant.

## Complément de conformité détaillée §8.2

L'audit ultérieur du texte intégral a relevé un écart malgré la validation
numérique initiale : le C++ utilisait des octets et pas les bitsets/canonical
states explicitement demandés. Écart corrigé à8f25c4b avec bitsets64bits et mode
`--memo-small` (N≤12), canonisant l'occupation complète relative à l'extrémité
sous D4 et mémorisant les vecteurs de prolongements. Preuve et code revus par
Astra;17tests indépendants passent avec ASan/UBSan. Résultats canoniques dans
results/m1-optimized-modes-v1. L'ancienne suite à10tests reste un fait historique;
la suite courante contient17tests. Voir COMPLETION_AUDIT.md pour le contrôle
exhaustif des15actions et la séparation entre clôture M1 et mission M2–M4.

Clôture après audit du cahier des charges : results/m1-validation-v2, source
daa5a1c,17tests/7.74s,39entrées historiques et36sources courantes vérifiées.
Contrôle indépendant des deux derniers reçus accepté; aucun écart§8.2 restant.
COMPLETION_AUDIT.md porte la décision définitive sur l'objectif immédiat.
