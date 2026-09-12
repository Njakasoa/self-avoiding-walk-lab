# Honeycomb : contrôle positif et limites du transfert au carré

## Objet et identité locale

Dans un domaine honeycomb simplement connexe, le départ a est un mid-edge
au bord; les extrémités sont des milieux d'arêtes. |γ| compte les sommets visités,
convention différente du n d'arêtes entre sommets de NORMALIZATION.md.
Ces conventions ont le même taux exponentiel, mais leurs petites séries ne
peuvent être identifiées terme à terme.

F(z)=Σ_(γ:a→z) exp(−iσW(γ)) x^|γ|, avec winding géométrique total W.
Pour σ=5/8 et x_c=1/√(2+√2), le lemme1 de
[Duminil-Copin–Smirnov](https://arxiv.org/abs/1007.0575) donne
Σ_(p adjacent à v) (p−v)F(p)=0 (trois mid-edges).
La preuve partitionne les contributions en paires de trajets et triplets
obtenus par prolongement. Elle requiert le domaine simplement connexe et le
départ au bord pour identifier les windings. Poser j=exp(2πi/3), λ=exp(−5πi/24).
Les deux facteurs sont jλ̄⁴+j̄λ⁴=0 et 1+x_c(jλ̄+j̄λ)=0.

## Contrôle exact exécuté

experiments/honeycomb_control.py représente t=exp(iπ/24) dans
Q[t]/(t¹⁶−t⁸+1)=Q[t]/Φ₄₈. Alors j=t¹⁶, λ=t⁻⁵ et
μ=t³+t⁻³=2cos(π/8). Les numérateurs des facteurs deviennent
 t³⁶+t¹² et μ+t²¹+t²⁷. Leur réduction vaut zéro. La relation
μ⁴−4μ²+2=0 est également vérifiée; l'embedding positif et l'identité radicale
sélectionnent √(2+√2), pas arbitrairement une des quatre racines.
Remplacer t²¹+t²⁷ par t²⁰+t²⁸ produit un reste non nul (contrôle négatif).

Ce calcul certifie les facteurs scalaires connus. La partition combinatoire et
la preuve globale sont étudiées ci-dessous, sans prétendre les formaliser en code.

## Passage local → global

La somme sur une bande finie S_(T,L) annule les contributions intérieures.
La géométrie de bord fixe les phases; avec séries positives A(retour gauche),
B(traversée), E(sortie haut/bas), l'identité est
1=cos(3π/8)A_(T,L)(x_c)+B_(T,L)(x_c)+cos(π/4)E_(T,L)(x_c).

Dans le passage L→∞, il faut traiter les deux cas, sans supposer E_T=0 :
si une contribution E_T(x_c)>0 persiste, les trajets arbitrairement longs
impliquent la divergence critique. Dans l'autre cas, les identités de bandes
et l'inégalité A_(T+1)−A_T≤x_c B_(T+1)² donnent une minoration harmonique
de B_T, donc encore la divergence à x_c. Pour x<x_c, le coût de traversée
et la décomposition de Hammersley–Welsh contrôlent les bridges et assurent la
convergence. Ce sont deux directions nécessaires; l'annulation locale seule
ne donne pas μ. Détails : source primaire archivée, §3, pp.5–9.

## Carte des obstructions

| Ingrédient | Honeycomb | Carré ordinaire | Obstruction précise | Déformation à étudier |
|---|---|---|---|---|
| Degré | Trois directions | Quatre | Le classement en paires/triplets de la preuve ne couvre plus les configurations | Etats à plusieurs composantes |
| Poids | Un fugacity et spin5/8 | Un poids uniforme | Les équations du modèle dilué carré font intervenir plusieurs types de connectivité | Six poids locaux du modèle O(n) |
| Géométrie | Tournants ±π/3 | ±π/2 et droit | Copier les facteurs j,λ ne représente pas les trajets carrés | Rhombes et poids directionnels |
| Identité de bord | Exacte à chaque largeur | Aucune identité analogue établie ici | Une annulation partielle ne contrôle pas toutes les sorties | Tester une largeur non utilisée pour ajuster les paramètres |
| Criticité | Deux côtés du rayon prouvés | μ exact ouvert | Aucune implication globale d'un simple fit | Renewal et positivité avec modèle défini explicitement |

[Beaton–Guttmann–Jensen2011](https://arxiv.org/abs/1110.1141) adaptent
numériquement les identités de bandes et observent des corrections dépendantes
de la largeur sur le carré. Cela limite cet ansatz, sans être un théorème
universel d'impossibilité des observables parafermioniques.

[Ikhlef–Cardy](https://arxiv.org/abs/0810.5037) relient les équations locales
parafermioniques aux poids intégrables du modèle dilué O(n). Les poids
indépendants t,u₁,u₂,v,w₁,w₂ décrivent des configurations de boucles;
les résoudre ne prouve pas que le SAW carré uniforme en est une spécialisation.
[Nienhuis1982](https://doi.org/10.1103/PhysRevLett.49.1062) avait prédit la
valeur honeycomb via O(n), limite n→0 pour les polymères; la preuve rigoureuse
spécifique est ultérieure.

[Glazman2014](https://arxiv.org/abs/1402.5376) et
[Glazman–Manolescu2017](https://arxiv.org/abs/1708.00395) donnent des familles
pondérées sur rhombes et des transformations Yang–Baxter. L'angleπ/3 retrouve
honeycomb, l'angleπ/2 donne un modèle à géométrie carrée mais à poids/configurations
différents du SAW ordinaire. Il faut conserver leur convention de longueur et
leur paramètre de fugacity; μ(x,y) défini ici ne s'y identifie pas automatiquement.

Pour le polymère honeycomb, log√(2+√2) est l'entropie dimensionless dominante
par pas et x_c le fugacity critique. Aucune conséquence sur les exposants
universels, ni application expérimentale supplémentaire, n'est inférée.
