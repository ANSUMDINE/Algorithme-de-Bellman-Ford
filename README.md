# Introduction et Généralité sur les Graphes:
### Introduction sur les Graphes:
• Graphe est une structure de données pouvant représenter des situations très diverses :
   - réseau routier
   - planning de tâches
   - courant dans un circuit électrique
   - réseau informatique
• On peut attribuer aux sommets ou aux arcs/arêtes des valeurs :
  - longueur, durée
  - capacité de transport
  - probabilité de transition
  - fiabilité de transmission ...
### Graphe orienté :
•  Un graphe orienté, noté G = {S, A} est déterminé par:
  - ensemble fini de sommets  S= { S1, S2, S3, ..... Sn}
  -   un ensemble fini d'arcs A= {A1, A2,.... An}
•  Vocabulaire :
  - Soient un graphe orienté G = { S, A } et deux sommets $x \in S$ et $y \in S$
  - Si $a = (x,y) \in A$ :
      -  x est l’extrémité initiale de a 
      -  y est l’extrémité terminale de a
      -   on dit que y est un successeur de x et x est un prédécesseur de y
  - Deux arcs ayant au moins une extrémité commune sont dits adjacents
  - x est adjacent à  y s’il est un prédécesseur ou un successeur de y. On dit que x et y sont voisins.
# Définition et Description de l'algorithme de bellman Ford
### Définition
L’algorithme de Bellman-Ford est un algorithme de recherche de plus courts chemins dans un graphe orienté pondéré. 
Il est capable de gérer des graphes avec des poids d’arcs négatifs, ce qui le rend plus polyvalent que d'autre algorithme.
### Condition d'application
-  Plus courts chemins à origine unique s0
-  Réseau sans circuit, poids des arcs quelconques
### Principe de l'algorithme
on construit progressivement un ensemble M de sommets du réseau pour lesquels on connaît les plus courts chemins d'origine s0 (au départ M={s0}).  
A chaque étape, on ne cherche le plus court chemin de s0 à un sommet x que si les plus courts chemins de s0 à tous les prédécesseurs 
de x sont déjà calculés, i.e. si tous les prédécesseurs de x sont dans M.  
D'où la nécessité de ne pas avoir de circuit. 
### Implémentation de l'algorithme

##### Données
- Un réseau \( R = (X, U, p) \)
- \( s_0 \in X \)

###### Résultats
- Une fonction \( \delta \) indiquant la plus courte distance de \( s_0 \) à un sommet \( x \) de \( X \)
- Une fonction `pred` indiquant le prédécesseur du sommet \( x \) dans un plus court chemin de \( s_0 \) à \( x \)

###### Algorithme

```python
def BellmanFord(R, s0):
    M = {s0}
    for x in S:
        δ[x] = float('inf')
        pred[x] = None
    δ[s0] = 0

    while exists(x not in M whose predecessors are all in M):
        M.add(x)
        for (y, x) in arcs where y in M:
            if δ[x] > δ[y] + p(y, x):
                δ[x] = δ[y] + p(y, x)
                pred[x] = y

    return δ, pred
