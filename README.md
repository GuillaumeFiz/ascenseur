

## Installation

* A la racine
  ```bash
    docker-compose up -d
    ```

* Connexion au Container
  ```bash
    docker exec -it ascenseur_app bash
  ```


## Utilisation

* Depuis le dossier **src**
  ```bash
    python main.py
  ```
  
P.S. : Le script ne se coupe pas tout seul, pour laisser le temps de voir le résultat. **CTRL + C** pour le couper.

**Attention** : Vérifier que la fenêtre du terminal est suffisament large pour contenir la tailles de l'interface. Si des lignes vides sont présentes entre chaque ligne d'étage, c'est que la fenêtre est trop petite.


## Fonctionnement

Le script tourne dans une boucle infinie qui va incrémenter un **tick**. Ce **tick** jouera le rôle d'indicateur temporel et des actions seront réalisées à chaque tick : 
- Ajout des personnes censées apparaître à ce tick (voir la partie **Paramétrage** ci-dessous)
- Exécution de la fonction **.next()** de l'ascenseur qui va déterminée la prochaine étape de celui-ci


## Paramétrage

Pour créer une séquence qui sera jouée automatiquement par le script, éditer la variable **chronology_patterns** dans le fichier :
  `chronology.py`

Cette variable est un dictionnaire clé / valeur où :
- la clé = le nom de la personne
- la valeur = les informations de cette personne dans la séquence : 
  - tick = le "moment" où la personne va faire sa demande à l'ascenseur
  - start = l'étage où elle va faire sa demande
  - arrival = l'étage qu'elle souhaite atteindre

P.S. : Cette manière de créer la séquence est un peu triviale mais elle permet de créer une séquences parfaitement timée et donc de tester des combinaisons plus précisement qu'avec un ajout manuel en temps réel.




