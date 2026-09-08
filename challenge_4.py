#bloc 1 

#1-1

class Livre():
    def __init__(self,name , author , disponible = True):
        self.name = name
        self.author = author
        self.disponible = disponible    

    def __str__(self):
        if self.disponible :
            return f'"{self.name}" de {self.author} -- disponible'
        else:
            return f'"{self.name}" de {self.author} -- emprunte'
        

# livre = Livre("book1" , "unknown")
# print(livre)


class Adherent() :
    def __init__(self,name , livres = []):
        self.name = name
        self.livres = livres

    def emprunter_livre(self, livre) :
        self.livre = livre
        if (livre.disponible == False) :
            print(f'Erreur : le livre "{livre.name}" n est pas disponible')
            return
        livre.disponible = False
        self.livres.append(livre)

    def nombre_livres_empruntes(self):
        return len(self.livres)


    def rendre_livre(self,livre):
        self.livre = livre
        livre.disponible = True
        index = self.livres.index(livre)
        self.livres.pop(index)

# livre = Livre("Dune", "Frank Herbert")
# ali = Adherent("Ali")
# sara = Adherent("Sara")
# ali.emprunter_livre(livre)
# sara.emprunter_livre(livre)


livre = Livre("Dune", "Frank Herbert")
ali = Adherent("Ali")
ali.emprunter_livre(livre)
ali.rendre_livre(livre) 
# print(livre)
# print(ali.nombre_livres_empruntes())



#bloc 2

class CompteBancaire():
    nom_banque = "BanquePyDiag"
    nombre = 0
    def __init__(self, name , solde_initial):
        self.name = name
        self.__solde = solde_initial
        CompteBancaire.nombre +=1

    @property
    def solde(self):
        print(self.__solde)
        return self.__solde

    # @solde.setter
    # def solde(self , new_solde):
    #     self.__solde =  new_solde

    def deposer(self , amount) :
        if amount <= 0 :
            raise ValueError( f"le montant du depot doit etre positif ({amount})")
        self.__solde += amount

    def retirer(self , amount) :
            if amount > self.__solde :
                raise ValueError(f"fonds insuffisants (solde : {self.__solde}, retrait demande : {amount})")
            self.__solde -= amount

    @classmethod
    def nombre_comptes(cls):
        print(cls.nombre)
        return cls.nombre

    @staticmethod
    def convertir_devise(ammount , taux):
        print(ammount * taux)
        return ammount * taux

compte = CompteBancaire("Ali", 100)
# print(compte.solde)   
# compte.solde = 5000
# print(compte.solde) 

# compte.deposer(50)
# compte.retirer(30)
# compte.solde

# try :
#     compte.deposer(-20)
# except ValueError as v:
#     print(f"{type(v).__name__} : {v}")

# try :
#     compte.retirer(500)
# except ValueError as v:
#     print(f"{type(v).__name__} : {v}")




# c1 = CompteBancaire("Ali", 100)
# c2 = CompteBancaire("Sara", 200)
# print(c1.nom_banque, c2.nom_banque)
# c1.solde, c2.solde




# c1 = CompteBancaire("Ali", 100)
# c2 = CompteBancaire("Sara", 200)
# c3 = CompteBancaire("Lina", 0)
# 3
# CompteBancaire.nombre_comptes()
# CompteBancaire.convertir_devise(100, taux=10.5)


#bloc 3 

class Vehicule() : 
    base = 20
    def __init__(self, marque , immatriculation):
        self.marque = marque
        self.immatriculation = immatriculation

    def tarif_journalier():
        pass

    def __str__(self):
        return f'{self.marque} ({self.immatriculation}),'

    


class Voiture(Vehicule) :
    def __init__(self, marque , immatriculation,nombre_places):
        super().__init__(marque , immatriculation)
        self.nombre_places = nombre_places

    def tarif_journalier(self):
        tarif =  super().base + (5 * self.nombre_places)
        return tarif

    def __str__(self):
        return 'Voiture ' + super().__str__() + f'-- {self.nombre_places} places -- {self.tarif_journalier()}/jour'


class Moto(Vehicule) :
    def __init__(self, marque , immatriculation,cylindree):
        super().__init__(marque , immatriculation)
        self.cylindree = cylindree

    def tarif_journalier(self):
        tarif =  super().base + (5 * self.cylindree)
        # print(tarif)
        return tarif

    def __str__(self):
            return 'Moto ' + super().__str__() + f'-- cylindree : {self.cylindree}  -- {self.tarif_journalier()}/jour'


class Camion(Vehicule) :
    def __init__(self, marque , immatriculation,charge_utile):
        super().__init__(marque , immatriculation)
        self.charge_utile = charge_utile

    def tarif_journalier(self):
        tarif =  super().base + (5 * self.charge_utile)
        # print(tarif)
        return tarif

    def __str__(self):
            return 'Camion ' + super().__str__() + f'-- charge : {self.charge_utile}  -- {self.tarif_journalier()}/jour'

    
# voiture = Voiture("Renault", "123-A-45", nombre_places=5)
# voiture.marque
# voiture.tarif_journalier()


# moto = Moto("Yamaha", "987-B-65", cylindree=600)
# camion = Camion("Volvo", "456-C-78", charge_utile=3000)
# moto.tarif_journalier()
# camion.tarif_journalier()



# flotte = [
# Voiture("Renault", "123-A-45", nombre_places=5),
# Moto("Yamaha", "987-B-65", cylindree=600),
# Camion("Volvo", "456-C-78", charge_utile=3000),
# ]
# for v in flotte:
#     print(v.marque, "->", v.tarif_journalier())




# voiture = Voiture("Renault", "123-A-45", nombre_places=5)
# moto = Moto("Yamaha", "987-B-65", cylindree=600)
# camion = Camion("Volvo", "456-C-78", charge_utile=3000)
# print(voiture)
# print(moto)
# print(camion)

#bloc4 

from abc import ABC, abstractmethod

class Modele(ABC) :
    @abstractmethod
    def entrainer(donnees):
        pass

    @abstractmethod
    def predire(entree) :
        pass
    
# modele = Modele()

import statistics as s
class ModeleMoyenne(Modele) :
    moyenne = 0

    def entrainer(self , donnees):
        self.donnees = donnees
        ModeleMoyenne.moyenne =  s.mean(self.donnees)
    
    def predire(self, entree):
        return ModeleMoyenne.moyenne



class ModeleLineaireSimple():
    def __init__(self, poids , biais):
        self.poids = poids
        self.biais = biais


    def entrainer(self , donnees):
            pass 

    def predire(self, entree):
            return  self.poids * entree + self.biais



# donnees = [5, 8, 11]
# modele = ModeleMoyenne()
# modele.entrainer(donnees)
# print(modele.predire(999))

# modele = ModeleLineaireSimple(poids=2, biais=1)
# modele.entrainer(donnees=None)
# print(modele.predire(5))

def normaliser(donnees):
    maximum = max(donnees)
    return [d / maximum for d in donnees]

class Pipeline() :
    def __init__(self, pretraitement , modele):
        self.pretraitement = pretraitement
        self.modele = modele

    def executer(self, donnees , entree):
        data = self.pretraitement(donnees)
        self.modele.entrainer(data)
        return self.modele.predire(entree)


pipeline_moyenne = Pipeline(pretraitement=normaliser, modele=ModeleMoyenne())
pipeline_lineaire = Pipeline(pretraitement=normaliser, modele=
ModeleLineaireSimple(2, 1))

donnees = [5, 8, 11]
pipeline_moyenne = Pipeline(pretraitement=normaliser, modele=ModeleMoyenne())
pipeline_lineaire = Pipeline(pretraitement=normaliser, modele=
ModeleLineaireSimple(2, 1))
for pipeline in [pipeline_moyenne, pipeline_lineaire]:
    resultat = pipeline.executer(donnees, entree=5)
    print(type(pipeline.modele).__name__, "->", resultat)
        
        

