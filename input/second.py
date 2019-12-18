# import first
import re


def validate(my_array):
    if my_array is not None:
        len_array = len(my_array)
        # print(len_array)

        middlename = ''
        lastname = ''
        firstname = my_array[0]
        if len_array == 2:
            lastname = my_array[1]
            
        if len_array == 3:
            middlename = my_array[1]
            lastname = my_array[2]
    else:
        print("Veuillez entrer au moins un caractère")
    d = {"firstname": firstname, "middlename": middlename, "lastname": lastname}
    print(d)


def validate_only_string(my_var):
    """
    Permet de savoir si la variable ne contient que du texte
    """
    # char valides
    valid_char = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
    
    # si ma var est vide, on return false
    if len(my_var) == 0 or not len(my_var):
        print("c'est vide")
        return False
    
    # si ma var est un int, return false
    if type(my_var) == int:
        print("c'est un nombre")
        return False

    # verif que chaque char de ma var est un char valide
    for c in my_var:
        if valid_char.__contains__(c) is False:
            print("vous utilisez un caractère non autorisé")
            return False
        else:
            print("votre var est ok")
            return True

    # autre solution pour la même fonctionnalité en utilisant
    # les regex (re = regular expression)
    r = re.match('^[A-Za-z]+$', my_var)  # '+' signifie pour 1 char ou plus  '^' début de ma var  '$' fin de ma var
    return True if r else False


print("SECOND")

validate_only_string("12")

"""
names = first.verifImput("jess bouq")
validate(names)

names3 = first.verifImput("")
validate(names3)
"""
