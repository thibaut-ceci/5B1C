# Présentation du projet 5B1C

iReaz est un créateur de contenu sur Youtube spécialisé dans le jeu League of Legends (abrégé LoL) qui s'est un jour posé une question intéressante : "Est-ce qu'un joueur de niveau Challenger pourrait vaincre, à lui seul, 5 joueurs débutants dans une partie classique de LoL ?". Pour y répondre, il a organisé une série de vidéos intitulée "1 Challenger contre 5 Bronzes" où des quintettes de joueurs, classés Bronze (équivalent à un niveau débutant), ont affronté des joueurs Challenger (le rang des meilleurs joueurs du jeu) dans des parties classiques. Cette série de vidéos est disponible sur Youtube à l'adresse suivante : https://www.youtube.com/playlist?list=PLg9Rno9Ks-fPMNRjuxAt9YbFAL8--NEij.

5B1C (abréviation de 5 Bronzes 1 Challenger) est un projet qui vise à analyser les parties de LoL de cette série de vidéo pour en tirer des informations intéressantes permettant de faciliter la réussite de ce challenge. Plusieurs questions vont trouver une réponse ici, comme par exemple : 
- Quel est le nombre maximal de morts qu'un Challenger peut subir avant de rendre ce défi presque impossible à gagner ?
- Quel est le nombre optimal de creeps par minutes (CS/min) à farmer pour avoir une bonne entrée d'or tout au long de la partie ?
- Quelle est la meilleure stratégie pour atteindre le Nexus ennemi (le batiment à détruire pour remporter la victoire) ?
Et autres.

# Analyse
Pour voir l'analyse, il faut ouvrir le fichier "5B1C.ipynb". "librairie.py" est un module Python contenant des fonctions pour réaliser des calculs dans le fichier précédent.

# Résultats
- Pour réussir le défi, il faut générer environ 950 or par minutes. Plusieurs moyens sont possibles pour parvenir à générer autant d'or. Certains moyens doivent être plus appuyé que d'autres.
- Pour générer beaucoup d'or en tuant des joueurs, il faut essayer d'avoir 2 kills vers 5 minutes de jeu, 10 kills vers 10 minutes de jeu, 18 kills vers 15 minutes de jeu et 29 kills vers 20 minutes de jeu.
- Farmer est important et il faut tuer en moyenne 7 sbires par minutes. Il ne faut pas trop se concentrer sur ce moyen pour générer de l'or mais plutôt sur l'obtention de kills ou la destruction de structures (plates et tours)
- Détruire 6 à 7 tours et 1 inhibiteur permets de réussir le défi. Il n'est pas nécessaire d'en détruire davantage de structures car il est préférable de se concentrer sur la destruction sur un seul chemin.
- Il est préférable de commencer par acheter un objet plutôt que compléter ces bottes.
- Il est possible de mourir 3 fois avec des grands intervalles de temps et de réussir le défi.
- Il est conseillé de prendre des risques en début de partie quitte à mourir pour commencer à générer beaucoup d'or.
- Mourir 5 fois rend le défi quasi impossible donc il faut absolument éviter de mourir autant.
- Perdre 1 inhibiteur n'est pas grave et n'entraine pas forcément un échec du défi. En perdre 2 augmente grandement les chances de perdre. En perdre 3 rend le défi impossible.
- Une partie doit durer le moins de temps possible et finir de préférence avant 23 minutes. 

**Stratégie de jeu :**

Voici une stratégie qui, selon moi, permettrait de maximiser les chances de victoire. Tout d'abord, après l'achat des items de départ, il est conseillé de commencer par farmer sur le chemin du milieu étant donné que c'est ici ou les sbires arrivent le plus vite. Je ne conseille pas de prendre de risque car parfois, les joueurs débutants peuvent s'amuser à tendre un piège et venir à 5 au milieu de la carte pour tuer le Challenger. Après quelques vagues de sbires et après, si possible, avoir mis le joueur du milieu dans une position peu favorable (c'est à dire, le tuer ou mettre au moins tous ses sbires sous sa tour), il est conseillé de se diriger sur le chemin du bas. C'est à ce moment là qu'il faut prendre des risques pour essayer de tuer les deux joueurs d'en face et commencer à récupérer de l'or, quitte à mourir. Ensuite, de mon point de vu, il est intéressant de se diriger un peu sur tous les chemins, pour éviter que les adversaires détruisent trop vite les structures mais aussi pour tenter de récupérer des kills, tuer beaucoup de sbires mais aussi de tenter de récupérer des plates et des tours. Après 14 minutes de jeu, je pense qu'il est préférable de se concentrer sur la destruction des structures d'un seul chemin. Le chemin du bas semble être le meilleur choix, étant donné que les adversaires sont deux à defendre ce chemin, cela permets de récupérer plus de kills (avec possiblement la venue du jungler), de réduire la venue du toplaner. Bien sûr, il faut aussi, de temps en temps, aller défendre les autres lanes pour éviter que les adversaires obtiennent des structures alliées trop tôt. Une stratégie intéressante à développer serait que, lors des retours à la base, il faut choisir un chemin à protéger, le défendre au maximum puis retourner sur le chemin du bas avec une téléportation et continuer la destruction des structures de ce chemin.

L'analyse est terminée, elle peut contenir des erreurs. Si vous souhaitez en discuter, vous pouvez me contacter sur Discord (mon nom d'utilisateur : thibot ; mon ID : 227126730567974912).