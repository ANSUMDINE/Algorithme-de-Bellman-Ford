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
