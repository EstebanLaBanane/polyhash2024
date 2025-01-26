# Projet Poly#

## Le projet
Le projet Poly# est inspiré du projet mené par Google X Lab nommé le [Project Loon](https://fr.wikipedia.org/wiki/Projet_Loon). Celui-ci consiste à utiliser des **ballons haute-altitude** équipés d'emetteurs pour fournir une couverture internet aux zones ne possèdant pas les infrastructures ou la topologie pour.

La question qui se pose est comment **guider les ballons** vers la cible en **utilisant les vents** stratosphériques quand le seul contrôle possible sur ces ballons est leur altitude.

Le but de notre projet était donc de **représenter la situation** algorithmiquement et ensuite de **développer le meilleur algorithme possible** pour diriger les ballons.

Ce projet à été effectué en **1ère année** d'école d'ingénieur, par **groupe de 4** en utilisant **Python**.

## L'équipe A
- Berrada Hamza - hamza.berrada@etu.univ-nantes.fr
- YASMINE Achraf - achraf.yasmine@etu.univ-nantes.fr
- HO Hugo - hugo.ho@etu.univ-nantes.fr
- GIROUX Esteban - esteban.giroux@etu.univ-nantes.fr
  
## Descriptif
Description du fonctionnement du projet, notamment comment le lancer (paramètres, etc).

La syntaxe générale/minimale est

    polyhash.py ./challenges/challenge.in ./output/sortie.txt

## Répartition des tâches/fonctions du projet au sein de l'équipe

### Esteban Giroux 

#### Les fonctions

- balloon.py  
- cell.py  
- create_game.py  
- game.py  
- get_instructions.py  
- gui.py  
- map.py  
- polyhash.py  
- read_input.py  
- rando_algo.py

> a participé à la réalisation du montage vidéo

### Achraf Yasmine

#### Les fonctions

- Decoupe_OPT.py  
- Diriger_Ballon.py  
- Main_Algo.py  
- Main_Algo_v3.py  
- ZonePoints.py  
- random_OPT.py  

> a participé à la réalisation du montage vidéo

> a développé les solutions Main Algo et Random OPT

### Hamza Berrada

#### Les fonctions

- Main_Algo.py  
- Main_Algo_v3.py  
- cut_map.py  
- distance_cells.py  
- find_dead_cells.py  
- random_OPT.py  
- score_of_cells2.py  

> a participé à la réalisation du montage vidéo

> a développé les solutions Main Algo et Random OPT


### Hugo Ho

#### Les fonctions

- algo_best_path.py

> a participé à la réalisation du montage vidéo 

> a conçu la solution algo_best_path


## Procédure d'installation 

Au sein de notre projet il n y a qu'une seule installation à faire et qui permet la visualisation de la stimualation grâce au fichier *gui.py*.

il faut inserer dans le terminale :

>pip install tkinter

## Procédure d'exécution 

Afin d'executer notre projet, il faut choisir une map **chalenge.in** et mettre un fichier texte de sortie **output.txt**, si il n'existe pas il sera créé et enfin mettre le nom de notre fichier main **polyhash**.

Ainsi pour lancer la stimulation on met dans le terminale :

>python -m polyhash "challenge.in" "output.txt"




## Organisation du code

Pour représenter la situation réelle du projet, la meilleure pratique est d'utiliser la **programmation orientée objet** (POO). En effet nous utilisons des objets tels que des ballons, des cible, une zone ou même des vents. C'est donc ainsi que la première ségmentation du code a été décidée. Des **classes objets** nommées après ceux-ci ont été crées (<ins>ex :</ins> *balloon.py* ou *map.py*).

Avec ces **classes** il était plus simple de représenter la situation réelle algorithmiquement : 
> Une liste de ballons

> Une map/carte composée de cellules

> Les ballons sont définis par leur position, numéro, altitude, rayon.

> etc...

Il manquait encore un **controleur central**, celui-ci n'est pas un objet physique du problème mais est plutôt comme le **plan de travail** qui permet de joindre tous ces éléments.

Encore une fois la POO est la meilleure option pour créer cet élément.

Celui-ci contiendra toutes les **parties** du problème (<ins>i.e :</ins> les classes créées) et les **méthodes** de fonctionnement du problème (<ins>i.e :</ins> passage d'un tour à l'autre, comptage des points, gestion des mise à jour...)

Le controleur (*game.py*) passe d'un tour au suivant en applicant des **instructions** passées en paramètre à chacun des éléments concernés.

Ces instructions sont générés par un **algorithme**, c'est une manière de dicter aux ballons comment se comporter. A chaque tour l'algorithme choisi analysera la situation et donnera une action à effectuer pour chaque ballon : ce sont les **instructions**.

L'organisation finale est la suivante, un **ensemble de classes** représentent les objets du problème, le **controleur central** lie toutes ces parties, un module contient les **différents algorithmes** développés.

Des méthodes préalables sont aussi utilisées pour extraire les données et les convertir en instances des classes.

## Détail de la/des stratégie.s mise.s en oeuvre et commentaire à propos des performances (temps d'exécution et place mémoire)

### Solution Main Algo 

- La solution **Main Algo** utilise plusieurs fonctions auxiliaires pour optimiser la stratégie de déplacement des ballons. **find_dead_cells** identifie les zones dangereuses où les ballons risquent d’être perdus. Ensuite, **cut_map_optimise** divise la carte en zones, et **score_of_cells** attribue des points aux cellules en fonction des cibles atteignables. **concentration_cells_pts** calcule la densité de points dans chaque zone, et **assignation_ballon_vers_zones** affecte les ballons aux zones prioritaires en fonction de leur score. Une fois les zones assignées, la distance entre chaque ballon et les cellules centrales de sa zone assignée est calculée pour orienter ses déplacements. À chaque tour, l’altitude optimale est déterminée pour rapprocher le ballon de la cellule cible, tout en évitant les zones identifiées comme dangereuses.

### Solution Random_OPT

- La solution **Random_OPT** utilise également **find_dead_cells** pour identifier et éviter les cellules dangereuses. Elle repose sur **rando_algo2**, qui génère des déplacements aléatoires pour les ballons en s'assurant que leurs mouvements restent dans des zones sécurisées.

### Explications détaillées sur chaque fonction 

- **Fonction Dead_Cells** 

    - Cette fonction analyse une grille de cellules avec différentes altitudes et effets de vent pour déterminer le statut de sécurité de chaque cellule. 
    
    - En fonction des données d'entrée, elle identifie les cellules où un ballon serait poussé hors des limites ("killer") ou resterait dans une position sûre ("safe").
    
    - Les résultats sont stockés dans un dictionnaire.

- **Fonction Score_of_cells**

    - Cette fonction calcule un score pour chaque cellule d'une grille en fonction du nombre de cibles qu'elle peut couvrir avec un ballon, compte tenu de son rayon de couverture. 
    
    - Les scores sont retournés sous forme d'un dictionnaire où chaque cellule est associée à son score.

-  **Fonction distance_cells** 

    - Cette fonction calcule la distance euclidienne entre deux cellules représentées par leurs coordonnées (x, y).
    
    - Elle retourne la distance sous forme de nombre flottant.


- **Fonction Cut_Map_Optimise** 

    - Cette fonction découpe une carte en blocs optimisés en fonction de la portée de couverture des ballons.
    
    - À partir d'un fichier contenant les dimensions de la carte, la portée de couverture **cov_r** et d'autres paramètres, elle calcule les dimensions des blocs **row_eff, col_eff** en tenant compte de la couverture effective des ballons.
    
    - La carte est ensuite divisée en blocs de ces dimensions, en incluant les éventuelles lignes et colonnes restantes dans les derniers blocs. Chaque bloc est une liste des coordonnées des cellules qu’il couvre, et la fonction retourne la liste complète de ces blocs.

- **Fonction concentration_cell_pts** 

    - calculer la concentration de points pour chaque partie découpée de la carte. Le résultat est un dictionnaire qui associe l'identifiant de chaque partie découpée à un pourcentage du score total qu'elle contient.

- **Fonction Points_Centre_Bloc** 

    - Cette fonction trouve les points centraux d’un bloc dans une grille donnée. elle s’adapte à différentes dimensions de blocs, qu’il s’agisse d’un bloc "standard" ou de blocs aux dimensions irrégulières (par exemple, lorsqu’il reste des lignes ou colonnes supplémentaires).

- **Fonction assignation_Ballon_vers_centre**

    - Attribuer un certain nombre de ballons (nb_balloon) à différentes zones en fonction du nombre de points qu’elles contiennent. Les zones avec le plus grand nombre de points reçoivent prioritairement les ballons.

- **Solution Main_Algo**

    - Cette solution implémente un algorithme principal pour gérer les mouvements des ballons dans une simulation. Elle détermine les actions nécessaires pour chaque ballon à chaque tour en fonction de plusieurs facteurs, tels que :

        > **Zones assignées** : Les ballons se voient attribuer des zones spécifiques où ils doivent se déplacer.

        > **Centres des blocs** : Les centres de blocs sont calculés pour guider les ballons vers leurs zones assignées.

        >**Vent et sécurité** : Les vents et les cellules dangereuses ("deadcells") influencent les décisions de montée, descente ou maintien de l'altitude.

        >**Priorités stratégiques** : En début de partie, les ballons sont répartis aléatoirement, tandis que des stratégies optimisées sont appliquées ensuite.

- ### Solution random OPT
    
    - Le code gère les déplacements sécurisés des ballons. La fonction **check** valide une action en vérifiant que le ballon ne se dirige pas vers une cellule "killer".

    - La fonction **rando_algo2** génère des actions aléatoires sécurisées, adaptées à chaque ballon selon son altitude, tout en évitant les mouvements risqués.

### Limitations de notre solution Main Algo 

- Concernant le Main Algo, la principale limitation résidait dans le fait que chaque ballon ne pouvait anticiper qu’un seul pas à la fois. Sur certaines cartes comme *d_final*, où les vents imposaient une direction très spécifique, les ballons étaient souvent contraints de suivre ces vents sans pouvoir trouver une trajectoire efficace vers leur zone assignée. Il aurait été pertinent d'intégrer une capacité d'anticipation sur 5 ou 10 coups à l'avance, plutôt que de se limiter à un pas, afin d'améliorer leur capacité à se rapprocher de leur objectif.

## Bugs et limitations connues


Après l'utilisation de notre **Main Algo** sur toutes les maps disponibles dans le dossier chellenges, notre strategie marchait pour des maps avec des vents irregulier comme dans la map *c_medium.in* où on a obtenu un score de 140 points mais pour les maps avec des vents régulier (<ins>i.e :</ins> à partir d'une altitude les vents dans les autres altitudes poussent dans la même direction) comme la map *d_final.in* on a remarqué ce qu'on appelle **les cycles**, (<ins>i.e :</ins> le ballon tourne dans un cycle car il prend à chaque fois le choix qui le rapproche de sa cible même si cela implique de revenir à sa position initiale ) 

Alors on a implémenter deux solutions créeant par consequence deux versions de notre Main Algo.

La premiere solution est **Main Algo + Random optimisé**, elle se trouve dans le fichier *Main_Algo_v3.py*

>cette solution consiste à ajouter un attribut mémoire au type ballon ce qui nous permet de detecter les ballons coincés dans un cycle, une fois repérés ces ballons vont agir d'une manière random sans pour autant sortir de la map

La deuxieme solution est **Main Algo + Attribution nouveaux centres**, elle se trouve dans le fichier *Main_Algo_v2.py*

>cette solution consiste à detecter les ballons coincé dans un cycle grâce à leur attribut mémoire, ensuite on leur attribue des centres de ballons qui ne sont pas coincé dans un cycle et afin de sauvegarder les données lors de chaque tour on utilise des fonctions qui sauvegarde les données dans un fichier json, finalement cette solution ne marche pas car il y a des fois des confusions (des fois on attribut au ballon cible un centre qui provoque un cycle ou des fois ça marche pas pour une raison inconnue). 

## Algo_best_path

### Fonctionnement

1-De manière récursive, essaie toutes instructions/chemins possibles avec un seul ballon
2-Garde le chemin donnant le meilleur score
3-Une fois l’algorithme principal lancé, à chaque tour, envoie un ballon suivant les instructions

### Limitations et performances
rapide et peu de mémoire utilisée mais très mauvais score simple et pas adapté au problème