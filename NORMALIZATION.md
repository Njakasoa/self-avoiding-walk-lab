# Conventions canoniques

Réseau carré : sommets Z², arêtes non orientées entre voisins à distance L1=1.
Une marche est une liste ordonnée de sommets distincts ω₀,…,ωₙ, ω₀=(0,0).
La longueur compte les arêtes. c₀=1. Les marches sont enracinées et orientées
par leur ordre de parcours. Rotations et réflexions sont comptées séparément;
aucun quotient implicite. Fixer le premier pas est une optimisation : multiplier
par quatre uniquement pour n≥1.

Bridge horizontal : n≥1 et 0=x₀<xᵢ≤xₙ pour chaque i=1,…,n.
Son span vaut xₙ. Le maximum final peut avoir été atteint avant la fin.
Un point de renouvellement k interne satisfait : préfixe et suffixe translaté
sont chacun des bridges dans cette même convention. Un bridge irréductible
n'a aucun tel point. b₀=1 par convention de série, i₀=0.
B(z)=1/(1-I(z)) comme série formelle par décomposition unique.
Une borne tirée d'une famille finie d'irréductibles est une borne inférieure,
avec certificat de signe rationnel (jamais une simple racine flottante).

Polygones : cycles simples fermés; ils ne sont PAS inclus dans cₙ.
Toute future série de polygones précisera racine/orientation/translation.
Trails : pas d'arête répétée, sommets répétés possibles; objet différent,
non implémenté comme SAW.

Poids : x≥0 par pas horizontal et y≥0 par pas vertical, poids multiplicatif;
Zₙ(x,y)=Σ x^(n_h)y^(n_v), μ(x,y)=lim Zₙ^(1/n) par submultiplicativité.
μ(1,1)=μ carré; μ(tx,ty)=tμ(x,y), μ(x,y)=μ(y,x).
Pour x=0 ou y=0, μ=max(x,y); μ(0,0)=0.

Confinement : toute expérience indique l'ensemble de sommets autorisé,
la racine, et les conditions aux bords. Une grille rectangulaire finie n'a
pas une constante connective infinie non nulle; ses comptes ne constituent
pas à eux seuls une borne asymptotique. Un automate de mémoire m interdit
les retours aux m derniers sommets; il peut accepter de longues boucles.
Ses marches contiennent toutes les SAW, donc donnent une borne supérieure.

Catégories : EXACT INTEGER / RIGOROUS INTERVAL / CERTIFIED SPECTRAL BOUND /
HIGH-PRECISION NUMERICAL / EXTRAPOLATION / HEURISTIC / CONJECTURE.
La validité et la priorité de publication sont deux axes séparés.
