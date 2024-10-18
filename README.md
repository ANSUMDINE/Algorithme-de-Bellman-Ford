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
- $\( s_0 \in X \)$

###### Résultats
- Une fonction \( \delta \) indiquant la plus courte distance de \( s_0 \) à un sommet \( x \) de \( X \)
- Une fonction `pred` indiquant le prédécesseur du sommet \( x \) dans un plus court chemin de \( s_0 \) à \( x \)

###### Algorithme

BellmanFord(R, s0)
    M ← {s0}
    pour tout x ∈ X faire
        δ(x) ← +∞
        pred(x) ← indéfini
    δ(s0) ← 0
    tant qu'il existe x ∉ M dont tous les prédécesseurs sont dans M faire
        M ← M ∪ {x}
        pour chaque arc (y, x) tel que y ∈ M faire
            si δ(x) > δ(y) + p(y, x) alors
                δ(x) ← δ(y) + p(y, x)
                pred(x) ← y

    retourner (δ, pred)
# Structure du Projet
- `main.py` : Le script principal qui démontre l'utilisation des deux implémentations.
- `implementation/` :
  - `bellman_ford_list.py` : Implémentation utilisant des listes pour stocker les arêtes.
  - `bellman_ford_dict.py` : Implémentation utilisant des dictionnaires pour stocker les arêtes.
- `test/` :
  - `test_bellman_ford.py` : Tests unitaires pour vérifier la correction des implémentations.

# Résumé des Implémentations
1. **Bellman-Ford avec Listes**
   - Utilise des listes pour stocker les arêtes du graphe.
   - Complexité temporelle : \( O(V * E) \)
   - Complexité spatiale : \( O(V + E) \)

2. **Bellman-Ford avec Dictionnaires**
   - Utilise des dictionnaires pour stocker les arêtes du graphe.
   - Complexité temporelle : \( O(V * E) \)
   - Complexité spatiale : \( O(V + E) \)

# Visualisation
Une visualisation interactive de l'algorithme Bellman-Ford est générée en utilisant `networkx` et `Pyvis`, offrant une représentation graphique claire des calculs de distances minimales. Pour voir la visualisation, exécutez le script principal et ouvrez le fichier `bellman_ford.html` généré.

# Tests
Les tests unitaires sont inclus pour vérifier l'exactitude des implémentations. Utilisez `pytest` pour exécuter les tests :
```sh
pytest
```
# Analyse de Complexité des Algorithmes Bellman-Ford

Cette analyse compare la complexité temporelle et spatiale de deux implémentations de l'algorithme Bellman-Ford, en utilisant respectivement des listes et des dictionnaires.

## 1. Implémentation avec Liste

### Complexité Temporelle
#### Initialisation : 
La création de la liste dist a une complexité de 
O(V).

#### Boucle Principale : 
La boucle externe s'exécute V−1 fois et la boucle interne parcourt chaque arête. Cela donne une complexité temporelle de O(V×E)


#### Vérification des Cycles Négatifs : 
Cette boucle parcourt à nouveau chaque arête, ce qui ajoute une complexité de O(E)

Au total, la complexité temporelle est de O(V×E)

### Complexité Spatiale
#### Liste des Arêtes : 
La liste self.graph stocke toutes les arêtes, ce qui nécessite O(E) espace.

#### Liste des Distances : 
La liste dist nécessite O(V) espace.

Au total, la complexité spatiale est de O(V+E).

## 2. Implémentation avec Dictionnaire

### Complexité Temporelle

#### Initialisation : 
La création du dictionnaire dist a une complexité de O(V).

#### Boucle Principale : 
La boucle externe s'exécute V−1 fois et la boucle interne parcourt chaque sommet et chaque arête. Cela donne une complexité temporelle de O(V×E)

#### Vérification des Cycles Négatifs : 
Cette boucle parcourt à nouveau chaque sommet et chaque arête, ce qui ajoute une complexité de O(E)

Au total, la complexité temporelle est de O(V×E).

### Complexité Spatiale
#### Dictionnaire des Arêtes : 
Le dictionnaire self.graph stocke toutes les arêtes, ce qui nécessite O(E) espace.

#### Dictionnaire des Distances : 
Le dictionnaire dist nécessite O(V) espace.

Au total, la complexité spatiale est de O(V+E)


# 3. Conclusion
Les deux implémentations ont les mêmes complexités temporelle et spatiale :

- Complexité Temporelle : O(V×E)

- Complexité Spatiale : O(V+E)

La différence principale réside dans la structure de données utilisée :

La première implémentation utilise une liste de listes pour stocker les arêtes.

La deuxième implémentation utilise un dictionnaire de listes pour stocker les arêtes.

# Ressources:
- https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford
- https://www.techno-science.net/definition/6471.html
