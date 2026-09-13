from abc import ABC, abstractmethod

class Livre:
    
    def __init__(self, titre, auteur):
        self.auteur = auteur
        self.titre = titre
        self.disponible = True

    def emprunter(self):
        self.disponible = False

    def rendre(self):
        self.disponible = True

    def __str__(self):
        etat = "disponible" if self.disponible else "emprunte"
        return f'"{self.titre}" de {self.auteur} -- {etat}'

class  Adherent:

    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def emprunter_livre(self, livre):
            if livre.disponible:
                self.livres.append(livre)
                livre.emprunter()
            else:
                print(f"Erreur : le livre \"{livre.titre}\" n'est pas disponible.")

    def nombre_livres_empruntes(self):
        return len(self.livres)

    def rendre_livre(self, livre):
        try:
            self.livres.remove(livre)
            livre.rendre()
        except ValueError:
            print(f"{self.nom} doesn't have the book")

# livre = Livre("Dune", "Frank Herbert")
# livre1 = Livre("Jane", "Long Faces")
# livre2 = Livre("Nevada", "NBA Youngboy")
# livre3 = Livre("The Bigger Picture", "Lil Baby")
#
# ali = Adherent("Ali")
# ali.emprunter_livre(livre)
# ali.emprunter_livre(livre1)
# ali.emprunter_livre(livre2)
# ali.emprunter_livre(livre3)
# print(ali.livres)
# print(ali.nombre_livres_empruntes())
#
# ali.rendre_livre(livre)
#
# sara = Adherent("Sara")
# sara.rendre_livre(livre)
# sara.emprunter_livre(livre)
# print(sara.nombre_livres_empruntes())

class  CompteBancaire:

    nom_banque = "BanquePyDiag"
    accounts = 0

    def __init__(self, name, solde):
        self.name = name
        self.__solde = solde
        CompteBancaire.accounts += 1

    def  deposer(self, montant):
        if montant < 0:
            raise ValueError(f"le montant du depot doit etre positif ({montant}).")
        self.__solde += montant

    def  retirer(self, montant):
        if montant < 0:
            raise ValueError(f"le montant du retrait doit etre positif ({montant}).")
        if montant > self.__solde:
            raise ValueError(f"fonds insuffisants (solde : {self.__solde}, retrait demande : {montant}).")
        self.__solde -= montant

    @property
    def solde(self):
        return self.__solde

    @classmethod
    def nombre_comptes(cls):
        return cls.accounts

    @staticmethod
    def convertir_devise(solde, taux):
        return solde * taux

# compte = CompteBancaire("Ali", 100)
# print(compte.solde)
# compte.__solde = 5000

# compte = CompteBancaire("Ali", 100)
# compte.deposer(50)
# compte.retirer(30)
# print(compte.solde)

# compte = CompteBancaire("Ali", 100)
# compte.deposer(-20)
# compte.retirer(500)

# c1 = CompteBancaire("Ali", 100)
# c2 = CompteBancaire("Sara", 200)
# print(c1.nom_banque, c2.nom_banque)
# print(c1.solde, c2.solde)

# c1 = CompteBancaire("Ali", 100)
# c2 = CompteBancaire("Sara", 200)
# c3 = CompteBancaire("Lina", 0)
# print(CompteBancaire.nombre_comptes())
# print(CompteBancaire.convertir_devise(100, 10.5))


class Vehicule:
    def __init__(self, marque, immatriculation):
        self.marque = marque
        self.immatriculation = immatriculation

    def tarif_journalier(self):
        raise NotImplementedError("doit être redéfinie")

    def __str__(self):
        return f"{self.__class__.__name__} {self.marque} ({self.immatriculation})"

class Voiture(Vehicule):
    def __init__(self, marque, immatriculation, nombre_places):
        super().__init__(marque, immatriculation)
        self.nombre_places = nombre_places

    def tarif_journalier(self):
        return 20 + 5 * self.nombre_places

    def __str__(self):
        return f"{super().__str__()} -- {self.nombre_places} places -- {self.tarif_journalier()}/jour"

class Moto(Vehicule):
    def __init__(self, marque, immatriculation, cylindree):
        super().__init__(marque, immatriculation)
        self.cylindree = cylindree

    def tarif_journalier(self):
        return 20 + self.cylindree / 100

    def __str__(self):
        return f"{super().__str__()} -- {self.cylindree}cc -- {self.tarif_journalier()}/jour"

class Camion(Vehicule):
    def __init__(self, marque, immatriculation, charge_utile):
        super().__init__(marque, immatriculation)
        self.charge_utile = charge_utile

    def tarif_journalier(self):
        return 50 + self.charge_utile / 100

    def __str__(self):
        return f"{super().__str__()} -- {self.charge_utile}kg -- {self.tarif_journalier()}/jour"

# voiture = Voiture("Renault", "123-A-45", 5)
# print(voiture.marque)
# print(voiture.tarif_journalier())
# print(voiture)
#
# moto = Moto("Yamaha", "987-B-65", cylindree=600)
# camion = Camion("Volvo", "456-C-78", charge_utile=3000)
# print(moto.tarif_journalier())
# print(camion.tarif_journalier())


class Modele(ABC):
    @abstractmethod
    def entrainer(self, donnees):
        pass

    @abstractmethod
    def predire(self, entree):
        pass

class ModeleMoyenne(Modele):
    def __init__(self):
        self.moyenne = 0

    def entrainer(self, donnees):
        if donnees:
            self.moyenne = sum(donnees) / len(donnees)

    def predire(self, entree):
        return self.moyenne

class ModeleLineaireSimple(Modele):
    def __init__(self, poids, biais):
        self.poids = poids
        self.biais = biais

    def entrainer(self, donnees):
        pass

    def predire(self, entree):
        return self.poids * entree + self.biais

class Pipeline:
    def __init__(self, pretraitement, modele):
        self.pretraitement = pretraitement
        self.modele = modele

    def executer(self, donnees, entree):
        donnees_traitees = self.pretraitement(donnees)
        self.modele.entrainer(donnees_traitees)
        return self.modele.predire(entree)

# def normaliser(donnees):
#     maximum = max(donnees)
#     return [d / maximum for d in donnees]
# 
# pipeline_moyenne = Pipeline(pretraitement=normaliser, modele=ModeleMoyenne())
# pipeline_lineaire = Pipeline(pretraitement=normaliser, modele=ModeleLineaireSimple(2, 1))
# 
# donnees = [5, 8, 11]
# for pipeline in [pipeline_moyenne, pipeline_lineaire]:
#     resultat = pipeline.executer(donnees, entree=5)
#     print(type(pipeline.modele).__name__, "->", resultat)
