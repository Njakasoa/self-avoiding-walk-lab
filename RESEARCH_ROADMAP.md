# Feuille de route post-M3/M4 — 12 septembre 2026

> Mise à jour après exécution de P1 : le [dossier W](W_ACCEPTANCE.md)
> contient une preuve complète acceptée en revue interne, un certificat exact
> des signes limites et les essais finis, y compris leurs échecs aux petits
> indices. Le plan initial ci-dessous est conservé comme historique ; ses
> mentions de W « ouvert dans ce dossier » sont désormais dépassées.
> Restent la relecture externe et la priorité (P0), puis les restes effectifs,
> un premier indice garanti et les résidus pour J et W (P2), avant P3.
> Suite choisie par l'utilisateur : préparer P0. Le
> [guide de relecture J/W](publication/REVIEW_J_W.md) est prêt ; aucun
> chercheur externe n'a été contacté et aucun avis externe n'est acquis.

Cette feuille de route part du niveau accepté dans `M3_ACCEPTANCE.md` et
`M4_ACCEPTANCE.md` : le résultat interne porte sur
$J=P_I=(P-H)/(1+P)$, la série des rampes $NE$-prudentes irréductibles,
et établit sa non-$D$-finitude. La priorité de publication reste
**UNRESOLVED**. Aucune étape ci-dessous ne transforme ce statut en priorité
établie, ni ne déduit un résultat sur la constante de connectivité du réseau
carré.

L'état du dépôt consulté pour ce plan est le commit `5b33c4c08a06fc461667e41f8443e3c5baa026a9`.
Ce fichier est un plan : aucune nouvelle expérience scientifique n'est lancée
ici et il n'a pas de sortie numérique à hacher.

## Décision de séquencement

L'étape mathématique la plus importante est le quotient de ponts $W$, mais
elle doit réutiliser les contrôles de phase et de pôles de $J$. Le meilleur
ordre est donc :

1. préparer la vérification éditoriale et l'audit de priorité, qui sont une
   étape de publication et non un résultat mathématique ;
2. attaquer $W$ par ses propres zéros de dénominateur ;
3. rendre effectives les asymptotiques de pôles déjà obtenues seulement sous
   la forme « pour $N$ assez grand » ;
4. ouvrir ensuite la continuation pondérée anisotrope, d'abord près de
   l'isotropie.

## P0 — Vérification externe et priorité (publication, en parallèle)

**But.** Faire relire le manuscrit autonome, le certificat d'intégrales, la
preuve de limite uniforme et la portée exacte du théorème par au moins deux
lecteurs indépendants ; refaire en parallèle une recherche bibliographique
plus large (citations, versions longues, prépublications et listes d'auteurs).

**Première action contrôlée.** Produire un paquet de revue en lecture seule à
partir du commit source gelé : reproduction « clean room », comparaison des
hashes du manuscrit et des certificats, puis grille de questions demandant
explicitement si chaque passage $N\to\infty$ est uniforme. L'envoi à des
chercheurs externes nécessitera une autorisation distincte ; ce plan ne
l'effectue pas.

**Obligation.** Aucune nouvelle preuve n'est requise pour appeler cette étape
éditoriale réussie, mais les lecteurs doivent vérifier : (i) la transcription
de $H=\widetilde P$, (ii) le contrôle au franchissement critique, (iii) le
passage des signes certifiés à tout $N$ assez grand, et (iv) l'obstruction
$D$-finie pour le germe continué.

**Succès mesurable.** Deux rapports écrits indépendants sans gap analytique
ou une liste finie de corrections résolues, plus un journal de recherche
bibliographique daté. **Échec mesurable.** Un rapport laisse un gap ou une
collision bibliographique : le manuscrit reste un candidat interne et le mot
« premier » reste interdit.

Cette étape ne doit pas être confondue avec la suite : même un avis éditorial
favorable ne prouverait pas la non-$D$-finitude de $W$.

## P1 — Quotient de ponts $W$ (première priorité mathématique)

**Cible exacte.** Dans Bacher--Beaton, le pont faiblement prudent à deux côtés
est
$$
  W=\frac{I}{1-I},\qquad
  I=4P_I-2D_I-t,\qquad
  P_I=J=\frac{P-H}{1+P},\qquad
  D_I=\frac{D}{1+D}.
$$
La formule est l'équation (5) et les équations (1)--(3) de la source
primaire. Un pôle de $J$ n'est pas un pôle de $W$ : la transformation
$I\mapsto I/(1-I)$ envoie une valeur infinie vers $-1$. Il faut donc
trouver des zéros de $1-I$ là où $I$ est fini ; le résultat M3 sur $J$
ne suffit pas.

**Première expérience.** Sur les mêmes coordonnées de phase que M3, évaluer
avec intervalles dirigés $I(t_N(\theta))-1$, en incluant exactement le
terme $D_I$, pour $N=32,64,128$, puis réserver $N=256$ comme test hors
ajustement. Isoler les éventuels changements de signe dans des intervalles
qui évitent les pôles de source et les pôles de $J$. Toute racine détectée
numériquement doit être enfermée par intervalle, pas seulement donnée par
une quadrature flottante.

**Obligation de preuve.** Obtenir une limite de phase pour $I-1$ avec un
contrôle uniforme du reste ; prouver qu'il existe une infinité de zéros de
$1-I$ dans des bandes disjointes ; et montrer que $I$ est holomorphe en
ces zéros, avec $I=1$. Le numérateur de $W$ vaut alors $1$, donc chaque
zéro donne un pôle non amovible. Un $N_0$ effectif, une racine simple et une
borne $|I'(s_N)|\geq\kappa>0$ sont des améliorations quantitatives utiles,
mais ne sont pas nécessaires à la conclusion de non-$D$-finitude.

**Critère de succès.** Une preuve uniforme de cette suite infinie de zéros
holomorphes suffit pour établir la non-$D$-finitude de $W$. **Critère
d'échec.** Les signes ne persistent pas, les racines coïncident avec des
pôles de $J$, ou aucun contrôle uniforme n'est obtenu : conserver alors
le résultat comme une obstruction/expérience négative sans annoncer de
théorème sur $W$.

## P2 — Asymptotiques quantitatives des pôles de $J$

**But.** Rendre quantitatives la localisation et les erreurs autour des
racines $r_N$, où $P(r_N)=-1$. Le profil limite est déjà strictement
croissant en phase, car $P_0(\theta)$ dépend de $B(\theta)$ avec
$B'(\theta)>0$ et $J_{1,\mathrm{post}}>0$. Les signes certifiés et la
convergence uniforme donnent donc une unique phase limite $\theta_*$ et
$\theta_N\to\theta_*$ pour les racines choisies ; ce n'est pas une question
ouverte de la feuille de route.

Un corollaire géométrique peu coûteux doit être extrait en premier. Avec
$F(t)=1/t-1+t+t^2$, on a $F(\sigma)=2$, $F'(\sigma)=-4$, et
$$
 q+q^{-1}=2\cosh(\varepsilon/2)=2+\varepsilon^2/4+O(\varepsilon^4),
 \qquad
 t(\varepsilon)=\sigma-\varepsilon^2/16+O(\varepsilon^4).
$$
Comme $\varepsilon_N(\theta_N)=s_*/N+O(N^{-2})$ pour une phase bornée,
on obtient déjà
$$
  \sigma-r_N\sim \frac{s_*^2}{16N^2}.
$$

**Première expérience.** Utiliser une méthode d'intervalle de Newton sur
$1+P(t_N(\theta))$ pour isoler les racines aux indices
$N=32,64,128$, enregistrer $\theta_N$, $\varepsilon_N$, $r_N$,
$P'(r_N)$ et le résidu local de $J$. Ajuster seulement sur ces trois
indices, puis prédire l'intervalle pour $N=256$, qui doit rester exclu de
l'ajustement. Cet ajustement est une heuristique de pilotage, jamais un
certificat.

**Obligation de preuve.** Quantifier la convergence des moments réguliers avec
un reste explicite provenant de la fenêtre de croisement et de la queue
exponentielle. Ne pas supposer un reste $O(N^{-1})$ : l'exposant singulier
$\eta=1/\sqrt2<1$ peut donner un taux fractionnaire. La cible est un
$\alpha>0$ explicite, démontré à partir de la décomposition réelle des
termes, puis une borne $|\theta_N-\theta_*|\leq C N^{-\alpha}$. L'indice
effectif $N_0$, la simplicité et les résidus sont des étapes quantitatives
ultérieures ; les coefficients ne seront traités qu'après contrôle des
autres singularités.

**Critère de succès.** Le corollaire $\sigma-r_N\sim s_*^2/(16N^2)$ est
certifié, puis un taux $\alpha>0$ et une constante de reste sont prouvés.
Un $N_0$ effectif et une borne de simplicité peuvent ensuite compléter le
dossier. **Critère d'échec.** Aucun taux positif ne découle du contrôle du
croisement, ou seules des extrapolations flottantes sont disponibles : le
théorème M3 demeure valide, mais la sortie reste classée « numérique haute
précision » ou « extrapolation ».

## P3 — Continuation pondérée anisotrope (près de l'isotropie)

**But.** Définir proprement les séries à deux fugacités
$x^{n_h}y^{n_v}$ pour les mêmes rampes et vérifier si le mécanisme de phase
survit lorsque $x/y\neq1$. Une rampe $NE$-prudente orientée par le
premier pas strict du bridge n'est pas automatiquement la même classe après
échange des axes : l'échange transporte la classe vers une autre convention,
sans identité automatique des coefficients de $J$. Cette piste étend la
structure analytique de $J$ et, à plus long terme, de $W$ ; elle ne vise
pas une valeur exacte de la constante de connectivité du SAW carré.

**Première expérience.** Dériver le noyau et la récurrence pondérés à partir
des objets de Bacher--Beaton, puis compter séparément la classe originale et
sa classe transportée par échange des axes jusqu'à la longueur 12. Vérifier la
spécialisation isotrope $x=y=t$ et les limites axiales. À $x=t$, commencer
par les rapports proches $y/x\in\{9/10,1,11/10\}$, avec des évaluations
d'intervalles et une bande de phase courte ; les rapports larges
$1/4,1/2,2,4$ viennent ensuite si le voisinage survit. Les matrices
spectrales de He concernent le SAW pondéré non orienté : elles peuvent fournir
une enveloppe de convergence, mais ne donnent ni les symétries de la rampe
orientée ni une continuation méromorphe de $P,H,J,W$.

**Obligation de preuve.** Fixer une branche analytique bivariée et un domaine
où les dénominateurs du noyau restent séparés, puis établir la formule
pondérée pour la classe choisie. Toute relation entre la classe originale et
la classe transportée doit venir d'une bijection explicite ; on ne doit pas
imposer $x\leftrightarrow y$ aux coefficients de $J$. Les identités
$\mu(tx,ty)=t\mu(x,y)$ et $\mu(x,y)=\mu(y,x)$ concernent la constante
pondérée du SAW non orienté (ou un objet pour lequel la bijection est prouvée),
pas automatiquement la rampe orientée. Pour une conclusion radiale, il
faudra ensuite certifier les zéros non annulés à rapport fixé.

**Critère de succès.** Soit une preuve d'un voisinage ouvert de rapports
$y/x$ où une suite de pôles de $J$ (puis éventuellement de $W$) est
uniformément persistante, soit un domaine bivarié de convergence analytique
avec bornes rationnelles reproductibles et amélioration mesurable de la borne
isotrope. **Critère d'échec.** Collision de branche, perte du signe au premier
rapport anisotrope ou simple série numérique : limiter alors la conclusion à
une carte exploratoire et ne pas étiqueter la continuation comme certifiée.

## Ce que la littérature autorise à dire

La vérification primaire du 12 septembre 2026 donne les repères suivants.

* **Bacher--Beaton (FPSAC/DMTCS 2014)** définissent exactement les ponts
  faiblement prudents à deux côtés, donnent $W=I/(1-I)$,
  $I=4P_I-2D_I-t$ et $P_I=(P-\widetilde P)/(1+P)$, et étudient les
  pôles de $P$ et $\widetilde P$. Leur source est la
  [notice DMTCS](https://dmtcs.episciences.org/2445), le
  [PDF officiel](https://dmtcs.episciences.org/2445/pdf) et le
  [DOI 10.46298/dmtcs.2445](https://doi.org/10.46298/dmtcs.2445). La source
  laisse explicitement ouverte la non-$D$-finitude de $P_I$ et de $W$ ;
  le résultat M3 ne doit donc pas être transféré à $W$ par la formule
  rationnelle.
* **Bacher--Bousquet-Mélou (2011)** prouvent la non-$D$-finitude d'un
  modèle différent, les marches faiblement dirigées, par une structure de
  ponts irréductibles et une accumulation de singularités. Voir la
  [version primaire arXiv](https://arxiv.org/abs/1010.3200) et le
  [DOI de l'article](https://doi.org/10.1016/j.jcta.2011.06.001). C'est un
  précédent méthodologique, pas une résolution de $W$.
* **Bousquet--Mélou (2009/2010)** résout une classe prudente plus restreinte
  et laisse la classe prudente générale ouverte ; ses séries anisotropes
  servent de contrôle historique mais les motifs de dénominateurs issus de
  séries finies ne sont pas une preuve de continuation. Voir la
  [version primaire arXiv](https://arxiv.org/abs/0804.4843) et le
  [DMTCS/FPSAC](https://dmtcs.episciences.org/3627).
* **Grimmett--Li (2019)** prouvent, sous leurs hypothèses de poids, des
  résultats d'égalité entre constante pondérée des marches et des ponts,
  ainsi qu'un théorème de continuité. Voir
  [Weighted self-avoiding walks](https://arxiv.org/abs/1804.05380) et le
  [texte publié](https://link.springer.com/article/10.1007/s10801-019-00895-6).
  Cela justifie un contrôle de normalisation pour P3, mais ne donne pas les
  formules bivariées de Bacher--Beaton.
* **He (2025)** étend la méthode d'Alm aux poids d'arêtes positifs : la plus
  grande valeur propre d'une matrice donne une borne supérieure de la
  constante pondérée et une région de convergence absolue de la série
  anisotrope. Voir le [préprint primaire et son HTML](https://arxiv.org/abs/2508.01993),
  ainsi que l'[article J. Phys. A](https://doi.org/10.1088/1751-8121/ae280e).
  Le papier impose de ne regrouper que par symétries préservant les poids ;
  il ne prouve ni une continuation méromorphe du quotient prudent, ni la
  non-$D$-finitude de $W$.
* Pour les pôles quantitatifs, les précédents prudents montrent que des
  suites de pôles accumulées et des corrections sous-dominantes peuvent
  gouverner les séries, mais l'objectif P2 est précisément de produire ici
  des constantes et des restes effectifs. Le [travail primaire sur les
  chemins prudents](https://mdpi.com/1099-4300/10/3/309) est donc un
  précédent, non une preuve de la nouvelle asymptotique.

La formulation sûre après ces étapes reste : **non-$D$-finitude de $J$
établie au niveau interne M3/M4 ; priorité UNRESOLVED ; $W$ et la constante
de connectivité du SAW carré ouverts dans ce dossier.**
