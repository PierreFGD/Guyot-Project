# PF-Guyot
	# Objective/Objectif # 
[en] The sole purpose of this program is to make hours on projet voltaire training, not to resolve evalution.

[fr] L'unique but de ce programme est de faire des heures sur l'entrainement du projet voltaire et non de résoudre les évalutions. 

	# Dependencies/Dépendances #
[en]
	-python 3 (https://www.python.org/)

	-selenium, install with "pip install selenium" if you have pip already install, if not install pip or look at the documentation
		https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium

	-chrome, if you want to change it to work on an other platform this might be possible, you will need to look at the selenium documentation

[fr]
	-pyhon 3 (https://www.python.org/)
	
	-selenium, installation via "pip install selenium", si pip est disponible sur votre machine, sinon installer pip ou voir la documentation
		https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium

	- chrome, pour utiliser un autre moteur de recherche il faudra regarder la documentation selenium et changer le programme en conséquence.

	# Use it/L'utiliser #
[en]
Step 1: Enter your voltaire connection email and password between the arrows in the "config.txt" file like this : 

	email:>your_email<
	password:>your_password<

Step 2: Launch the python programm

[fr]
Etape 1: Entrer vos identifiants de connexions au projet voltaire entre les flèches dans le fichier "config.txt" :

	email:>votre_email<
	password:>votre_password<
	
Etape 2: Lancer le programe python

	# Current Issue/Problème récurrent #
[en] if the program doesn't click on the level it may be that the xpath of the button is not in the programm to resolve this issue you can go in the level
selection of Projet Voltaire, right click on the level button, click on inspect. You see the html code of the button, click right on it and in copy, select copy
full xpath. Then go in the program in the "niveau" method and replace the "add_xpath_here" by your xpath. If you need to add an other one, just copy the code
structure and do the same.
[fr] si le programme ne clique pas sur le niveau, c'est surement que le xpath du bouton correspondant n'est pas dans le programme, pour résoudre ce problème, il 
faut aller sur la selection de niveau de projet voltaire (normalement, pas via la programme), faite un clique droit sur le bouton du niveau, puis sur "inspecter"
ensuite cliquer droit sur le code html du bouton et dans "copy", selectionner full xpath puis dans le code remplacer dans la méthode niveau le "add_xpath_here"
par votre xpath. S'il faut encore en ajouter un, vous pouvez juste copier la structure du code au dessus et refaire la même chose.

	# Issues/Problèmes #
[en] if you meet any issue, do not hesitate to contact me at pierrefrancoisdf@gmail.com or post an issue on the github
[fr] si vous rencontrez un problème, n'hésiter pas à me contacter à pierrefrancoisdf@gmail.com ou a poster une issue sur ce github

	# Licence #
[en]
This program is under MIT License, you can freely use it, improve it

[fr]
Ce programme est sous licence MIT, utilisable et transformable librement




