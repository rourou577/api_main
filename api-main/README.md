# api
En python Django réaliser une api renvoyant les données des tables donnée dans pokedex.sql Le site doit utiliser mariadb, des points bonus seront accordés si un dockerfile et un docker-compose sont dans le rendu afin de pouvoir automatiser le déploiement sur le port 8042.

Réaliser les endpoints suivant :

/api/items/{id item}

/api/moves/{id moves}

/api/pokemon/{id pokemon}

/api/pokemon/{name pokemon}

/api/pokemon/types/{identifier pokemon}

/api/connexion /api/register

/api/mesPokemons (auth)

/api/role (auth admin) /api/admin/users (auth admin) Dans le cas d'un GET de données la réponses doit être formatée en json. Dans le cas d'un POST les données doivent être ajouter a la base de données. Dans le cas d'un DELETE les données doivent être effacer en base de données.

De plus vous devrez faire un JWT pour la connexion ainsi que la mise en place de rôle pour certaine routes.
