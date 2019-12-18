def verifImput(new_input):
    if new_input is not None:
        names = new_input.split()
        len_input = len(names)

        if len_input == 2:
            print("Nom : " + names[0] + " Prenom : " + names[1])
        elif len_input == 3:
            print("Nom :" + names[0] + " Middle : " + names[1] + " Prenom : " + names[2])
        elif len_input == 1:
            print("Nom seul :" + names[0])
        else:
            print("Que faire de :" + " ".join(names[3:]))
    else:
        print("Le champs est vide")
    return names


# Premier traitement

# fullname = input("Entrez votre nom puis votre prenom")
# names = verifImput(fullname)
