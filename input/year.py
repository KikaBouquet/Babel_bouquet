import datetime


def ask_for_year():
    """
    demande d'entrer l'année de naissance 
    """
    my_year = input("Quel est votre année de naissance ?")
    lenght_year = len(my_year)
    if lenght_year < 2 or lenght_year == 3 or lenght_year > 4:
        print("entrée incorrecte")
        return None
    return my_year


def verify_only_number(my_var):
    """
    verifie que les chars sont bien des int, retourne un bool
    """
    autorized_char = ["0","1","2","3","4","5","6","7","8","9"]
    for char in my_var:
        if autorized_char.__contains__(char) is False:
            print("Vous avez entré un caractère non autorisé")
            return False
    return True


def days_passed(my_year):
    """
    calcul du nombre de jours entre l'année en cours et l'année entrée
    """
    try:
        my_year_int = int(my_year)
    except ValueError:
        my_year_int = None
        print("les caractères entrés sont invalides")

    if my_year_int is not None:
        date_time_obj = datetime.datetime(my_year_int,1,1)
        date_now = datetime.datetime.now()

        to_return = date_now - date_time_obj
        return to_return
    else:
        return None


my_bool = True

while my_bool is True:
    result = ask_for_year()
    if result is not None:
        isOk = verify_only_number(result)
        if isOk is True:
            print("année entrée : " + result)
            number_of_days = days_passed(result)
            if number_of_days is not None:
                print("Nombre de jours passés " + str(number_of_days))
