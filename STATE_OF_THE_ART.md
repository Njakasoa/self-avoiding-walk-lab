# État de l'art — recherche arrêtée au 12 septembre 2026

Les meilleures bornes publiées identifiées dans cette recherche sont celles de
Jensen et Couronné. La valeur détaillée annoncée dans le théorème du préprint
Couronné est **2.625622 < μ carré ≤ 2.662342426**; la page de la version publiée
arrondit la borne supérieure à **2.662343**. Le laboratoire n'a pas recalculé
le certificat numérique de ce record. L'estimation **2.63815853032790(3)** est
une extrapolation numérique distincte, sans encadrement rigoureux à ces chiffres.

« Meilleur identifié » signifie dans la couverture de recherche ci-dessous.
Aucune garantie d'exhaustivité mondiale ni recherche de priorité experte n'est
revendiquée. Les méthodes connues sont séparées de leurs artefacts disponibles.

| Résultat / date / source primaire | Méthode et emplacement vérifié | Rigoureux ? Assistance / arithmétique / code | Limite / extension possible |
|---|---|---|---|
| Jensen, 2004 : μ>2.625622. [Article](https://arxiv.org/abs/cond-mat/0409381), J. Phys. A 37,11521–11529 | Kesten : dictionnaire d'irréductibles, TM span≤15 et longueur≤250; §2.2 p.7 | Borne rigoureuse annoncée; comptes entiers modulaires/CRT; environ 3000 CPU-h historiques; exécutable non trouvé | Pas de reproduction du record ici; dictionnaires plus riches et certificats rationnels locaux |
| Couronné, préprint2022 / publication2025-10-31 : μ≤2.662342426. [PDF](https://arxiv.org/pdf/2211.16146), [version publiée](https://link.springer.com/article/10.1007/s10955-025-03542-6) | Automates à choix de simplification, contraintes planaires; théorème p.1, algorithme §5 et tableau §6 p.7 | Théorème publié, calcul assisté; k26,430365791 états, fichier12.86GB; environ une semaine/32GB. Vecteurs propres par itération; certificat d'arrondi exact et code non trouvés | Le résumé publié donne2.662343. Les chiffres détaillés sont ceux du préprint; validation indépendante de leurs arrondis reste à faire. Son introduction cite une ancienne borne basse2.62002, dépassée par Jensen |
| Pönitz–Tittmann,2000 : μ≤2.679192495. [Article officiel](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r21) | Sur-langage évitant les boucles courtes, automate/Perron; k22 | Méthode rigoureuse; calcul assisté; pas de code ni certificat externe audités | Supplanté par Couronné. M1 reproduit petits k4/6/8 avec vérificateur rationnel |
| Jacobsen–Scullard–Guttmann,2016 : μ≈2.63815853032790(3). [Article](https://arxiv.org/abs/1607.02984) | Topological TM jusqu'à circonférence21, extrapolation; tables4/conclusion | NON rigoureux pour la limite; eigenvalues à40 chiffres, extrapolation en puissances supposées; source exécutable non trouvée | L'incertitude(3) est une dispersion d'estimateurs. Aucune preuve d'exposants ou formule exacte |
| Jensen,2013 : c₀…c₇₉. [Préprint](https://arxiv.org/abs/1309.6709) | TM à connectivité future, table2; c₇₉=10194710293557466193787900071923676 | Énumération exacte annoncée, modulaire/CRT; environ16500 CPU-h et jusqu'à1TB RAM | Pas de référence de revue dans la notice arXiv consultée; ne pas transformer en publication vérifiée. Données de contrôle OEIS archivées; frontière non reproduite |
| Clisby–Jensen,2012 : polygones périmètre130. [Article](https://arxiv.org/abs/1111.5877) | Finite-lattice TM de polygones | Comptes exacts assistés/CRT; implémentation record non auditée | SAP≠SAW. Ne pas annoncer c₁₃₀. Utile pour séries et contrôles croisés |
| Qidong He,2025 : bornes pondérées spectrales. [Article](https://arxiv.org/abs/2508.01993), J. Phys. A58,505003 | Théorème2.2 : μ≤ρ(G^P(m,n))^(1/(n−m)) sous primitivité; tableau1 symbolique | Théorème rigoureux; petits cas symboliques exacts, contours numériques flottants. [Code public](https://github.com/qidong-he/weighted_connective_constant) identifié, pas exécuté | Cas isotrope reproduit Alm; aucun meilleur record isotrope annoncé. Piste : certificats rationnels anisotropes et sous-groupes préservant les poids |
| Duminil-Copin–Smirnov,2012 : μ honeycomb=√(2+√2). [Article](https://arxiv.org/abs/1007.0575) | Observable parafermionique, annulations locales, contrôle global des bandes | Preuve mathématique; pas besoin de calcul record. M1 vérifie exactement les deux annulations scalaires locales | Ce contrôle ne re-prouve pas la partie globale et ne se transporte pas automatiquement au carré; voir proofs/HONEYCOMB.md |

## Couverture et actualité

Recherches primaires croisées : Jensen lower bound; Pönitz Tittmann upper bound;
Couronné connective constant; Jacobsen Scullard Guttmann; square SAW length80;
2025/2026 square lattice enumeration; weighted connective constant; valeur
2.63815853032790. Scholar-like résultats et pages secondaires servent seulement
à localiser les sources. Pages arXiv, articles et codes originaux ont été ouverts
par les agents; root a relu les PDF Couronné, He, honeycomb et les notices clés.

La recherche n'a pas identifié de dépassement récent de c79, SAP130, TTM21,
ni du record Couronné. Un article 2025/2026 d'énumération inspirée quantique
[arXiv:2512.24648](https://arxiv.org/abs/2512.24648) revendique notamment n71 :
il ne dépasse pas c79 et n'est pas adopté comme preuve du record. Une évaluation
détaillée de son code dépasse ce snapshot; aucune critique générale de validité
n'est inférée de son seul titre ou résumé.

## Historique et programme de lecture

Hammersley/Morton et Kesten sont les fondations de la croissance/renewal;
les arguments nécessaires à M1 sont explicités dans NORMALIZATION.md et
proofs/BRIDGE_RENEWAL.md, et la source primaire opérationnelle est Jensen2004.
Conway–Enting–Guttmann [1993](https://arxiv.org/abs/hep-lat/9211062) établit la
lignée finite-lattice. Nienhuis et les déformations intégrables sont étudiés
séparément dans proofs/HONEYCOMB.md. Une lecture exhaustive de tous les textes
historiques n'est pas prétendue. Voir references/CODE_ARCHAEOLOGY.md pour
les formats, licences non établies et distinctions de normalisation.

Priorité scientifique de nos reproductions : KNOWN. Aucun nouveau record.
