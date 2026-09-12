# NEXT — bilan d'exécution du programme E1–E3

> Mise à jour M3/M4 : ce bilan historique est complété par
> `M3_ACCEPTANCE.md`, `claims/CLAIM-0006.md` et le dossier `publication/`.
> La non-D-finitude des rampes NE-prudentes irréductibles a passé la revue
> interne. La priorité scientifique reste UNRESOLVED.

Les expériences E1, E2 et E3 ci-dessous sont exécutées et vérifiées. Le moteur
M2 couvre les paramètres annoncés et produit des observations automatiquement.
Voir DISCOVERY_REPORT.md, DISCOVERY_ENGINE.md et results/discovery-astra-review.md.
L'observation sélectionnée a été recalculée indépendamment jusqu'à mémoire12,
attaquée, expliquée et auditée : conséquence connue, sans nouveauté établie.
M3 comme contribution scientifique nouvelle et M4 publication restent UNRESOLVED.
La mission scientifique générale n'est donc pas déclarée réussie.

Le contrat original est conservé intégralement dans environment/NEXT_GOAL_BRIEF.md.
Le texte ci-dessous est le plan historique, pas une nouvelle liste à réexécuter.

## Plan initial — après acceptation M1

M1 validé : voir M1_REVIEW.md. M2 (moteur de découverte), M3 (résultat candidat)
et M4 (publication) ne sont pas atteints. La mission scientifique demeure ouverte;
aucune percée ni nouveauté n'est revendiquée. Les trois expériences ci-dessous
sont proposées après la revue, et ne sont pas des résultats déjà obtenus.

## E1 — Compression certifiée et mémoire supplémentaire

Question : quelles distinctions d'états changent réellement une borne, à budget
d'états fixé ? Construire une minimisation par raffinement de partitions fondée
sur les sommes de transitions vers chaque classe, puis comparer sans symétrie,
D4 et quotient équitable aux mémoires3…11. Vérifier la relation exacte AP=PB
et transférer les vecteurs rationnels. Mesurer états, transitions, U certifié,
temps/RAM et meilleur U au même coût. Limite initiale100000états/5minutes,
arrêt si le coût ne répond plus à cette question.

Falsification : égalité des continuations hors échantillon; partitions aléatoires
inexactes rejetées; m pair/impair comme contrôle de parité connu. Une compression
qui change les comptes sans preuve d'inclusion est un échec conservé.
Priorité : Pönitz–Tittmann, Couronné, quotient équitable/bisimulation déjà connus.
La nouveauté éventuelle concerne un invariant additionnel ou une règle de
simplification certifiable; réduire une matrice seule n'est pas une découverte.

## E2 — Dictionnaires de bridges contrôlés par span

Question : à coût d'énumération égal, vaut-il mieux augmenter la longueur,
le span ou certaines géométries d'irréductibles ? Produire i_(n,s), sélectionner
des familles emboîtées n≤12…18 et spans bornés, puis comparer des racines
certifiées rationnellement. Contrôle positif analytique : span1 donne
I(z)=z(1+z)/(1−z) et taux1+√2. Chercher une factorisation/génératrice rationnelle
sur une famille définie avant le fit, pas une récurrence supposée générale.

Falsification : autre sens de bridge, extension d'au moins deux coefficients
hors échantillon et collisions de concaténation. Une récurrence échouée est
archivée. Plafond initial5minutes par famille, pas de record n250 envisagé.
Priorité : Kesten/Jensen, SAWs partiellement/weakly directed; toute famille
exactement soluble doit être comparée à ces travaux avant label de nouveauté.

## E3 — Anisotropie avec certificats et symétries valides

Question : quel invariant géométrique améliore simultanément une famille de
bornes μ(x,y), plutôt que son seul point isotrope ? Reproduire d'abord de petits
cas symboliques de He2025, puis des matrices de mémoire pour poids rationnels
x/y∈{1/4,1/2,1,2,4}. Hors x=y, conserver D2 ou les orientations : D4 n'est pas
un quotient préservant les poids. Comparer U(x,y), homogénéité, échange x↔y,
limites axiales, log-convexité en log-poids et coût du certificat.

Falsification : mutant quotient D4 anisotrope, points rationnels non utilisés
pour optimiser, symétrie et x→0. Un meilleur chiffre sans structure n'est pas
un succès scientifique. Relier les sorties à log μ (entropie/free energy par
pas) et z_c=1/μ; pas d'exposants critiques inférés. Plafond3minutes par point.
Priorité : He/Alm, Grimmett–Li, Glazman–Manolescu; distinguer poids d'arêtes de
poids de configurations intégrables sur rhombes.

## Comparaison scientifique et ordre retenu

| Piste | Nouveauté probable au départ | Possibilité de preuve | Coût local initial | Sens physique | Généralisation |
|---|---|---|---|---|---|
| E1 automates | Faible pour compression standard; ouverte pour invariant nouveau | Forte via AP=PB/Av≤Uv | Faible→moyen, explosion surveillée | Entropie surestimée par oubli | Réseaux/poids, si inclusion prouvée |
| E2 bridges | Faible pour truncation; ouverte pour famille structurée | Forte via concaténation/GF | Moyen, exponentiel | Conformations avec renewal/confinement | Familles pondérées et bandes |
| E3 anisotropie | Travail2025 proche : audit de priorité essentiel | Forte pour inégalités; incertaine pour identité exacte | Faible sur petites matrices | Direct : anisotropie/fugacity | Paramètres continus et poids périodiques |

Ordre technique retenu : E1 d'abord pour bâtir le moteur/certificateur, E2 comme
contrepoids indépendant, puis E3 avec audit de symétrie. Ce sont des pistes
compatibles; aucune décision scientifique irréversible n'est requise.
Le moteur M2 devra exposer explicitement les variantes prises en charge de
réseau, bord, état, mémoire, motifs, poids, bridges, largeur et symétrie. Les
combinaisons non prises en charge doivent échouer clairement. Une observation
doit être produite automatiquement puis attaquée; les plateaux de parité connus
M1 ne suffisent pas à revendiquer une découverte M2.

Avant M3 : sélectionner selon importance×preuve×nouveauté/coût, refaire le calcul
indépendamment, chercher des contre-exemples, créer un claim complet, auditer
la littérature et faire une nouvelle revue Astra. Publication : UNRESOLVED.
