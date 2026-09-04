def division_securisee(a, b):
    try:
        res = a / b
        print(res)
    except ZeroDivisionError:
        print(f"Error: division {a} / {b} is impossible")


def convertir_entier(value):
    try:
        res = int(value)
        print(res)
    except ValueError:
        print(f"Error : \"{value}\" is not a valid int")


def acceder_element(list, index):
    try:
        res = list[index]
        print(res)
    except IndexError:
        print(f"Error : index {index} out of range (size of list : {len(list)}).")


def acceder_cle(dictionary, key):
    try:
        res = dictionary[key]
        print(res)
    except KeyError:
        print(f"Error : the key \"{key}\" doesn't exist")


def traiter_valeur(value):
    try:
        res = int(value)
    except ValueError:
        print(f"Error : \"{value}\" is unconvertible.")
    else:
        print(f"Conversion reussie : {res}")
    finally:
        print("Traitement termine.")



def verifier_age(age):
    if age < 0:
        raise ValueError(f"l'age ne peut pas etre negatif ({age}).")
    print(f"Age valide : {age}")


def traiter_liste_de_valeurs(value):
    for v in value:
        try:
            int(v)
        except ValueError:
            print(f"Log : value \"{v}\" invalid, exception relancee.")
        raise



def main():

    # division_securisee(1, 2)
    # division_securisee(7, 0)
    # convertir_entier("8")
    # convertir_entier("x")
    # acceder_element([1, 2, 3], 1)
    # acceder_element([1,2,3], 18)
    # acceder_cle({"name":"abdellah"}, "lastname")
    # traiter_valeur("8")
    # traiter_valeur("x")
    # verifier_age(250)
    # verifier_age(-3)
    # traiter_liste_de_valeurs(["3", "9", "x", "5"])


if __name__ == "__main__":
    main()