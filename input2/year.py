import datetime


def ask_for_year(my_year):
    """
    demande d'entrer l'année de naissance 
    """
    if my_year:
        try:
            length_year = len(my_year)
        except ValueError:
            return None
        
        if length_year is None or length_year < 2 or length_year == 3 or length_year > 4:
            print("entrée incorrecte")
            return None
        return my_year
    else:
        return None


def verify_only_number(my_var):
    """
    verifie que les chars sont bien des int, retourne un bool
    """
    autorized_char = ["0","1","2","3","4","5","6","7","8","9"]
    if my_var:
        for char in my_var:
            if autorized_char.__contains__(char) is False:
                print("Vous avez entré un caractère non autorisé")
                return False
        return True
    else:
        return False


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


# ne fonctionne pas, à tester
def verify_year(my_year):
    """
    si le nombre contient 4 chiffres alors il doit être inférieur à l'année en cours
    si le nombre contient 2 chiffres, on ajoute 2000 ou 1900
    """
    year_now = datetime.datetime.now().year
    if my_year > 999 and my_year < year_now:
        return my_year
    elif my_year < 100:
        year_now = str(year_now)[-2:]
        if 0 <= my_year and my_year <= year_now:
            my_year += 2000
        else:
            my_year += 1900
        return my_year
    else:
        return None


my_bool = True

while my_bool is True:
    year = input("Quel est votre année de naissance ?")
    result = ask_for_year(year)
    if result is not None:
        isOk = verify_only_number(result)
        if isOk is True:
            # complete_year = verify_year(result)
            # if complete_year:
            print("année entrée : " + result)
            number_of_days = days_passed(result)
            if number_of_days is not None:
                print("Nombre de jours passés " + str(number_of_days))        
