# Audit du périmètre initial — 2026-09-12

Le tour précédent est classé PROGRESS : code, sources primaires, certificats,
tests et revue indépendante ont été créés et archivés. Le présent audit ne
considère pas la conclusion précédente comme une preuve de complétude.

Objectif actif : construire le laboratoire et exécuter l'action immédiate M1,
jusqu'à proposer trois expériences après revue. Le point15 du cahier des charges
emploie « proposer »; exécuter M2, obtenir une percée M3 et publier M4 ne sont pas
les conditions de clôture de cette action. Ces jalons restent explicitement
ouverts dans NEXT.md. Aucun objectif scientifique n'est présenté comme résolu.

| Point de l'action immédiate | Source probante inspectée |
|---|---|
| 1 Créer le laboratoire | Racine du dépôt et11dossiers requis présents |
| 2 Installer l'orchestration locale | .codex/config.toml,5profils,skill et commit upstream épinglé |
| 3 Auditer le matériel | environment/audit.json et ENVIRONMENT_AUDIT.md; mesures et limites explicites |
| 4 Initialiser Git | Historique depuis0840c52, branchecodex/m1 |
| 5 Quatre tâches indépendantes | Appels Luna/max réels, deux vagues, rapports et journal; capacité3children |
| 6 Bibliographie au2026-09-12 | Sources primaires archivées, recherches datées et limites documentées |
| 7 STATE_OF_THE_ART.md | Fichier présent, bornes/estimation/comptage exact séparés |
| 8 NORMALIZATION.md | Objet enraciné orienté, rotations, bridges, poids, domaines finis |
| 9 Énumérateur de référence | src/reference_enumerator.py, code examiné et tests indépendants |
| 10 Tests contre données | data/A001411.txt, comptes jusqu'à20, tests et reçus canoniques |
| 11 Bornes publiées | Jensen2004, Couronné2025; détail du préprint séparé de l'arrondi publié |
| 12 Petit certificat spectral | Matrices/vecteurs rationnels, reconstruction des états et vérificateur exact |
| 13 Honeycomb | Preuve analysée, cas globaux, obstruction au carré, test cyclotomique et mutant |
| 14 Revue indépendante M1 | M1_REVIEW.md, rapports du tester et d'Astra, rejeux |
| 15 Trois propositions après revue | NEXT.md E1–E3, falsification/coût/priorité/sens physique et comparaison |

## Écart détaillé détecté avant clôture

Astra completion_scope_audit (Astra/low) relève que§8.2 demande des bitsets et
états canoniques pour l'énumérateur optimisé. Le C++ initial utilise des octets
avec premier pas fixé; sa correction numérique ne prouve pas cette couverture.
Root a donc rouvert ce point : packed bitsets et mode optionnel de mémoïsation
sur occupation complète canonisée+extrémité+longueur restante. Le mode facultatif
sera évalué sur sa correction et son coût; aucune mémoïsation par extrémité seule.
La clôture exige son implémentation, tests indépendants, benchmark et nouvelle
revue. Les anciens reçus restent attachés à leurs sources historiques.

## Écart corrigé et revu

Le code8f25c4b contient désormais les bitsets et la mémoïsation exacte sur états
complets canoniques, dans le même énumérateur. La preuve contient l'invariant
qui rend cette identification valide; les branches restent comptées avec leur
multiplicité. Le reviewer Astra accepte explicitement§8.2 et les15actions.
Le tester Luna obtient17tests passants, y compris une exécution ASan/UBSan.

m1-optimized-modes-v1 attache les calculs au commit8f25c4b : accord exact des
modes à n0/1/12, avec référence Python n12 et OEIS; mode direct jusqu'à20.
Mesure unique n12 : direct0.0024s/3584KiB, mémo0.0663s/16156KiB. Direct n20 :
1.3393s/3584KiB. La mémoire est celle du child mesurée par GNU time. Le surcoût
de canonicalisation explique le mode facultatif; il est conservé comme résultat
négatif, sans prétendre que la mémoïsation accélère ces petits calculs.

Les rapports initiaux restent historiques et datés par leurs commits. Le reçu
m1-validation-v2 sera le contrôle courant des sources/tests et des cinq jeux
scientifiques après ce complément. Aucun changement aux certificats spectraux,
aux comptes de bridges ou à la démonstration honeycomb n'a été requis.

## Décision finale

Le contrôle indépendant Luna accepte les derniers reçus :8/8sources du benchmark
et36/36sources de validation concordent avec Git et les octets courants; les
deux empreintes de sortie concordent. Le résultat courant est17tests passants
en7.74s,39entrées historiques vérifiées, sans erreur pytest. Toutes les actions
immédiates et l'écart détaillé§8.2 sont désormais prouvés par les éléments
inspectés. Aucun travail requis pour cet objectif immédiat ne reste ouvert.

Décision root : objectif actif M1+trois propositions ACHEVÉ. Les conditions
scientifiques de découverte M2–M4 ne sont ni supprimées ni annoncées satisfaites;
elles sont conservées dans NEXT.md comme étapes ultérieures de la mission.
Tous les agents requis ont terminé. Sources finales de validation :
daa5a1c4127ff663cfbfbd35c6f11906c69392e9.
