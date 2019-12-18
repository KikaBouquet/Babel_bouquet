"""
SETUP VERSION 0.1
Programme qui affiche le setup de la machine
Changelog:
-dec 19 : initialisation
"""


import sys
import os
import datetime


def printseparator():
    """ fontion qui affiche une separation """
    print("-" * 50)


print(sys.executable)
print(sys.platform)
print(sys.path)

printseparator()

version = sys.version_info
# print(type(version))  # type permet de voir le type ou la classe #
# print(dir(version))  # dir permet de voir tout ce sui est contenu dans version #


# on veut afficher 'minor' 'micro' 'major' de la version #
print(f"Python version {version.major}.{version.minor}.{version.micro}")
# print("Python version {}.{}.{}".format(version.major, version.minor, version.micro)) #
# print("Python version %s.%s.%s" % (version.major, version.minor, version.micro)) #ça existe, mais à éviter #

# recup les variables d'environnements #
print("Environnement PythonPath " + os.getenv("PYTHONPATH", "Vide"))


printseparator()

print(datetime)
print(datetime.__file__)

dt = datetime.datetime.now()
print(f"Date et Heure {dt} - Année {dt.year}")

# Utilisation du PEP8 -> regroupe les bonnes pratiques de
# l'écriture pour faire en sorte que ce soit le plus lisible possible
# do not repeat yourself
# make your code readable ...
# pour voir tout ça faire import this dans la cmd python
