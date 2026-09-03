import math

# def vendre(stock, produit, quantite):
#     if produit in stock:
#         if stock[produit] >= quantite:
#             stock[produit] -= quantite
#             print(f"Vente enregistree : {quantite} {produit}.")
#         else:
#             print(f"Stock insuffisant pour {produit} (disponible : {stock[produit]}).")
#     else:
#         print(f"Stock insuffisant pour {produit} (disponible : 0).")
#
# def produits_epuises(stock):
#     epuises = []
#     for produit, quantite in stock.items():
#         if quantite == 0:
#             epuises.append(produit)
#     return epuises

def main():
    notes = [12, 18, 7, 15, 9, 20, 3, 14]
    # min = math.inf
    # max = - math.inf
    # for note in notes:
    #     if(note >= max):
    #         max = note
    #
    #     if(note <= min):
    #         min = note
    #
    # print(f"Note max: {max}")
    # print(f"Note min: {min}")
    #
    # seuil = 12
    #
    # for note in notes:
    #     if(note > seuil):
    #         print(note)
    #
    # fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
    #
    # occurrence = {}
    # for fruit in fruits:
    #     if fruit not in occurrence:
    #         occurrence[fruit] = 1
    #     else:
    #         occurrence[fruit] += 1
    #
    # for fruit in occurrence.items():
    #     print(f"{fruit[0]} : {fruit[1]}")

    # liste = [1, 2, 3, 4 ,5]
    #
    # for i in range(len(liste) // 2):
    #     a = liste[len(liste) - i - 1]
    #     liste[len(liste) - i - 1] = liste[i]
    #     liste[i] = a
    #
    # print(liste)

    # liste_a = [1, 4, 7]
    # liste_b = [2, 3, 8, 9]
    # liste_c = liste_a #[1, 4, 7, 2, 3, 8, 9]
    #
    #
    # for n in liste_b:
    #     if n not in liste_c:
    #         liste_c.append(n)
    #
    # for j in range(len(liste_c)):
    #     for i in range(len(liste_c) - j - 1):
    #         if liste_c[i] > liste_c[i + 1]:
    #             temp = liste_c[i]
    #             liste_c[i] = liste_c[i + 1]
    #             liste_c[i + 1] = temp
    #
    # print(liste_c)
    #
    #
    # stock = {"pommes": 50, "bananes": 30, "oranges": 0}
    # vendre(stock, "pommes", 20)
    # vendre(stock, "oranges", 5)
    # print(stock)
    #
    # stock2 = {"pommes": 30, "bananes": 0, "oranges": 0, "kiwis": 12}
    # print(produits_epuises(stock2))

    commandes = [
        {"client": "Ali", "produit": "pommes", "quantite": 5},
        {"client": "Sara", "produit": "bananes", "quantite": 10},
        {"client": "Ali", "produit": "oranges", "quantite": 2},
    ]
    total_par_client = {}
    for commande in commandes:
        client = commande["client"]
        quantite = commande["quantite"]
        if client in total_par_client:
            total_par_client[client] += quantite
        else:
            total_par_client[client] = quantite
    print(total_par_client)

    d = {"a": 1, "b": 2, "c": 3}
    inverse = {}
    for k, v in d.items():
        inverse[v] = k
    print(inverse)

    mots = ["chat", "elephant", "abeille", "riz"]
    dict_mots = {mot: len(mot) for mot in mots}
    print(dict_mots)

    entreprise = {
        "IT": ["Ali", "Sara", "Omar"],
        "RH": ["Lina"],
        "Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
    }
    for departement, employes in entreprise.items():
        print(f"{departement} : {len(employes)} employe(s)")


if __name__ == "__main__":
    main()