# Babel_bouquet
Affichage des setups et validation des valeurs insérées dans un input

# Setup
## setup.py
### fonctions
printseparator()
permet d'afficher une séparation

### fonctionnalités
affiche les valeurs suivantes :
* sys.executable
* sys.platform
* sys.path
* sys.version_info
* datetime

### imports
* import sys
* import os
* import datetime

 # Input
 
 ## first.py
 Demande un nom complet, vérifie ce qui a été entré par l'utilisateur et affiche une réponse sous forme de nom, middlename, prénom
 ### fontions
 verifInput(my_input)
 vérifie que my_input n'est pas nul, et retourne une réponse sous forme de nom, middlename, prénom

 ## second.py
 ### fonctions
validate(my_array)
my_array vers un dictionnary avec les clés nom, middlename, prénom

validate_only_string(my_var)
vérifier que my_var ne contient que des lettres

 ### import
* import first
* import re
