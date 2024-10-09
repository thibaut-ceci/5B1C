# Introduction

iReaz est un créateur de contenu sur Youtube spécialisé dans le jeu League of Legends (abrégé LoL) qui s'est un jour posé une question intéressante : "Est-ce qu'un joueur de niveau Challenger pourrait vaincre, à lui seul, 5 joueurs débutants dans une partie classique de LoL ?". Pour y répondre, il a organisé une série de vidéos intitulée "1 Challenger contre 5 Bronzes" où des quintettes de joueurs, classés Bronze, ont affrontés des joueurs Challenger dans des parties classiques. Cette série de vidéo est disponible sur Youtube à l'adresse suivante : https://www.youtube.com/playlist?list=PLg9Rno9Ks-fPMNRjuxAt9YbFAL8--NEij.

Avant le lancement du défi, tout portait à croire que les Challengers gagneraient le défi relativement facilement, étant donné qu'il s'agit des meilleurs joueurs du jeu. Cependant, après de nombreuses vidéos, il est démontré que ce défi est en réalité très complexe et demande une précision de jeu quasi parfaite. Bien que débutant, les 5 joueurs, grâce à leur supériorité numérique, ont une plus grande facilité à dominer la carte, collecter des ressources et les utiliser contre le Challenger. Aussi, un combat à 1 contre 5 est très difficile à gagner sur LoL et il faut user de stratégie complexe pour parvenir à remporter ces combats.

5B1C (abbréviation de 5 Bronzes 1 Challenger) est un projet qui vise à analyser les parties de LoL de cette série de vidéo pour en tirer des informations intéressantes permettant de faciliter la réussite de ce challenge. Plusieurs questions vont trouver une réponse ici comme par exemple : 
- Quel est le nombre maximal de morts qu'un Challenger peut subir avant de rendre ce défi presque impossible à gagner ?
- Quel est le nombre de kills par minute qu'un Challenger doit obtenir pour maximiser ses chances de réussir le défi ?
- Quel est le nombre optimal de creep par minutes à farmer pour avoir une bonne entrée d'or tout au long de la partie ?
- Quelle est la meilleure stratégie pour atteindre le Nexus ennemi ?
Et autres.

# Analyse
Pour voir l'analyse, il faut ouvrir le fichier "5B1C.ipynb". "librairie.py" est un module Python contenant des fonctions pour réaliser des calculs dans le fichier précédent.

# Conclusion
- Pour réussir le défi, il faut générer environ 950 or par minutes. Plusieurs moyens sont possibles pour parvenir à générer autant d'or. Certaines moyens doivent être plus appuyé que d'autres.
- Pour générer beaucoup d'or en tuant des joueurs, il faut essayer d'avoir 2 kills vers 5 minutes de jeu, 10 kills vers 10 minutes de jeu, 18 kills vers 15 minutes de jeu et 29 kills vers 20 minutes de jeu. 
- Farmer est important et il faut en moyenne 9.7 creeps par minutes. Il ne faut pas trop se concentrer sur ce moyen pour générer de l'or mais plutôt sur l'obtention de kills ou la destruction de structures (plates et tours)
- Détruire 6 à 7 tours et 1 inibiteur permets de réussir le défi. Il n'est pas nécessaire d'en détruire davantage car il est préférable d'axer son push sur une seule lane.
- Il est préférable de commencer par acheter un item plutôt que compléter ces bottes.
- Il est possible de mourir 3 fois avec des grands intervalles de temps et de réussir le défi.
- Il est conseillé de prendre des risques en début de partie quitte à mourir pour commencer à générer beaucoup d'or.
- Mourir plus de 4 fois rend le défi quasi impossible.
- Perdre 1 inibiteur n'est pas grave et n'entraine pas forcément un échec du défi. En perdre 2 augmente les chances de perdre. En perdre 3 rend le défi impossible.
- Une partie doit durer le moins de temps possible, environ 23 minutes. 

**Stratégie de jeu :**

Voici une stratégie qui, selon moi, permettrait de maximiser les chances de victoire. Tout d'abord, après l'achat des items de départ, il est conseillé de commencer par farmer sur la midlane étant donné que c'est ici ou les creeps arrivent le plus vite. Je ne conseille pas de prendre de risque car parfois, les joueurs débutants peuvent s'amuser à tendre un piège et venir à 5 au milieu de la carte pour tuer le Challenger. Après quelques waves et après, si possible, avoir mis le midlaner ennemis dans une position peu favorable, il est conseillé de décaller sur la botlane. C'est à ce moment là qu'il faut prendre des risques pour essayer de tuer les deux joueurs d'en face et commencer à récupérer des golds, quitte à mourrir. Après cela, je pense qu'il est préférable d'axer son push sur la botlane. Etant donné que les joueurs sont deux sur cette lane, cela permets de récupérer plus de kills (avec possiblement la venue du jungler), de réduire la venue du toplaner et de prendre des plates plus facilement (étant donné que la protection des tourelles n'est pas appliquée sur la tour en botlane). Bien sûr, il faut aussi, de temps en temps, aller défendre les autres lanes pour éviter que les adversaires obtiennent des structures alliées trop tôt. Il est conseillé de prendre uniquement les plates et de ne pas insister davantage (c'est à dire de chercher à obtenir des tours) mais de plutôt se concentrer sur une seule lane jusqu'au Nexus.

Pour finir, je tiens à préciser que ceci est mon analyse personnelle des résultats. Elle peut contenir des erreurs, des imprécisions, des imperfections et vous pouvez aussi être totalement en désaccord avec ce que je dis. Si vous souhaitez en discuter, vous pouvez toujours me contacter sur Discord (mon nom d'utilisateur : thibot ; mon ID : 227126730567974912). Mon niveau est Emeraude sur LoL.