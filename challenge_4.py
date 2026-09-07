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
print(livre)
print(ali.nombre_livres_empruntes())



#bloc 2



