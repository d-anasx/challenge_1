#bloc 1 

notes = [-1, 18, 7, 99, 9, 20, 3, 14 , 99 , 7 , 9 , 7]


def getMax() :
    max = None
    min = None
    for i in notes :
        if max is None or i > max :
            max = i
        if min is None or i < min :
            min = i
    return print(f"max is : {max}---------min is : {min}")

# getMax()

def notes_au_dessus(seuil):
   filtred =  filter(lambda x : x > seuil, notes )
   return list(filtred)

# print(notes_au_dessus(12))

def reverse() :
    reversed = []
    for i in range(len(notes)) :
        reversed.append(notes[len(notes)- i - 1])
    return reversed
# print(reverse())

def occurences_count():
    occurences = {}
    for i in notes :
        if i not in occurences:
            occurences[i] = 1
        else:
            occurences[i] += 1
    for key , value in occurences.items() :
        print(f'{key} is duplicated {value} times\n')

# occurences_count()

liste_a = [1, 4, 7]
liste_b = [2, 3, 8, 9]

def sorted_fusion():
    sorted_list = liste_b
    for i in liste_a :
        for j in sorted_list:
            if i < j :
                sorted_list.insert(sorted_list.index(j) , i)
                break
            if i not in sorted_list:
                sorted_list.append(i)
    print(sorted_list)

# sorted_fusion()

def ListComprehension() :
    return [x**2 for x in notes if x % 2 == 0]
# print(ListComprehension())


#bloc 2
stock = {"pommes": 50, "bananes": 30, "oranges": 0 , "fraises": 0}
def vendre(produit, quantite) : 
        current_quanity = stock[produit]
        if current_quanity >= quantite:
            print(f'enregistree : {quantite} {produit}.')
        else :
            print(f'Stock insuffisant pour {produit} (disponible : {current_quanity}).')

# vendre('bananes', 30)


def stock_epuises():
    return [i for i,v in stock.items() if v == 0]

# print(stock_epuises())



commandes = [
{"client": "Ali", "produit": "pommes", "quantite": 2},
{"client": "Sara", "produit": "bananes", "quantite": 10},
{"client": "Ali", "produit": "oranges", "quantite": 2},
]

def total_par_client():
    result = {}
    for i in commandes:
        name = i['client']
        quantity = i['quantite']
        if name not in result:
            result[name] = quantity
        else :
            result[name] += quantity
    return result
# print(total_par_client())



d = {"a": 1, "b": 2, "c": 3}

def dictReverse():
    result = {}
    for key , value in d.items():
        temp = key
        key = value
        value = temp
        result[key] = value
    return result

# print(dictReverse())



mots = ["chat", "elephant", "abeille", "riz"]
def dictComprehension():
    return {x:len(x) for x in mots }

# print(dictComprehension())

#bloc 3
atelier_python = ["Ali", "Sara", "Lina", "Karim"]
atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]

def setManagement(list1 , list2):
    list1 = set(list1)
    list2 = set(list2)
    intersection = list1 & list2
    print(intersection)
    union = list1 | list2
    print(union)
    difference = list1 - list2
    print(difference)
# setManagement(atelier_python,atelier_java)

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]

def duplicatesDetection(list) :
    myset = set(list)
    return True if len(myset) < len(list) else False

# print(duplicatesDetection(liste_2))
    

tags_articles = [
["python", "web", "api"],
["python", "data"],
["web", "css"],
]

def listToset(list) :
    result = set()
    for i in list:
        myset = set(i)
        result = result | myset
    return result
# print(listToset(tags_articles))




ventes = [
{"produit": "pommes", "montant": 120},
{"produit": "bananes", "montant": 80},
{"produit": "pommes", "montant": 45},
{"produit": "oranges", "montant": 60},
{"produit": "bananes", "montant": 30},
]

def ventesAnalyse():
    result = {}
    for i in ventes:
        product = i['produit']
        number = i['montant']
        if product not in result:
            result[product] = number
        else :
            result[product] += number
    maxi = max(result, key=result.get)
    print(result)
    print(f'max is {maxi} - {result[maxi]}')

    distincts = {x["produit"] for x in ventes }
    print(distincts)

# ventesAnalyse()


from collections import Counter
inv1 = {"pommes": 20, "bananes": 15}
inv2 = {"bananes": 10, "kiwis": 5}

def fusionner_inventaires(inv1, inv2) :
        
    return dict(Counter(inv1) + Counter(inv2))

# print(fusionner_inventaires(inv1,inv2))







etudiant = [
    {"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
    {"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
    {"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
]

import statistics as st
moyenne = {e["nom"] : round(st.mean(e['matieres'].values()),2) for e in etudiant}
# print(moyenne)






# print(set().union(*(e['matieres'].keys() for e in etudiant)))


from collections import defaultdict
notes = defaultdict(list)

for e in etudiant:
    for k, v in e["matieres"].items():
        notes[k].append(v)

print(dict(notes))




