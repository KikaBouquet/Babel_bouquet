import datetime


def ask_for_year():
    my_year = input("Quel est votre année de naissance ?")
    lenght_year = len(my_year)
    while lenght_year < 2 or lenght_year == 3 or lenght_year > 4:
        print("entrée incorrecte")
        year_str = input("Quel est votre année de naissance ?")
        lenght_year = len(year_str)
    return my_year


def verify_only_number(my_var):
    autorized_char = ["0","1","2","3","4","5","6","7","8","9"]
    for char in my_var:
        if autorized_char.__contains__(char) is False:
            return False
    return True

"""
def verify_valid_year_for4char(my_year):
    while 1900 > my_year and my_year < year_now:
"""

# on demande l'année de naissance et on vérifie si le nombre de char est de 2 ou 4 seulement
year_str = ask_for_year()

# on vérifie si les char entrés sont bien des chiffres
isOk = verify_only_number(year_str)

# tant que ce ne sont pas des chiffres, on redemande une date de 2 ou 4 char ne contenant que des chiffres
while isOk is False:
    print("vous avre entrez des caractère non-autorisés")
    print("merci de saisir à nouveau votre date de naissance")
    year_str = ask_for_year()
    isOk = verify_only_number(year_str)
    
# conversion de year en int
year = int(year_str)
year_now = datetime.date.today().year


if year > 999:
    # verification nombre compris entre 1900 et l'année en cours
    if 1900 > year and year < year_now:
        print("vous avez entré une date invalide")
elif year < 100:
    # ajout des 2 premiers chiffres de l'année
    if year >= 0 and year <= year_now:
        year += 2000
    else:
        year += 1900   
else:
    print("nous avons rencontré une erreur")

print(year)

"""
correction
"""
