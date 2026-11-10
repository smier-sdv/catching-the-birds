# catching-the-birds

Projet python utilisant:
- pygame
- random
- json

Contexte: Dans une réserve naturelle, des oisillons sont en train d'apprendre à voler mais certains n'y arrivent pas.
Le but est d'attraper les oiseaux avant qu'ils ne touchent le sol pour éviter qu'ils se fassent mal.

Le joueur a droit à 3 erreurs et doit se déplacer avec les flèches gauche et droite ou avec les touches q et d sur un clavier azerty.

Le score est sauvegardé dans un fichier json s'il est supérieur au précédent et le record est affiché en haut du menu principal (mon record est de 402).

Il y a plusieurs paliers de difficulté:
Initialement, on ne peut faire apparaitre que 5 oiseaux en même temps à l'écran, et un oiseau apparait toutes les demies secondes (limite du cycle à 30).
A partir de 50 points, on passe à 7 oiseaux et la limite du cycle passe à 20.
A partir de 100 points, on passe à 10 oiseaux et la limite du cycle passe à 10.
A partir de 170 points, on passe à 15 oiseaux et la limite du cycle passe à 5.
A partir de 200 points, on passe à 20 oiseaux. 
La difficulté du niveau 200 étant déjà élevée je n'ai pas prévu de difficulté supérieure.
