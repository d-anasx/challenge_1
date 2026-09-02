def ajouter_etudiant():
    fname = input("Enter the first name: ")
    notes = []
    x = 0

    while x < 3:
        while True:
            user_input = input(f"Enter your note {x + 1}: ")

            try:
                note = float(user_input)

                if 0 <= note <= 20:
                    notes.append(note)
                    x += 1
                    break
                else:
                    print("The note must be between 0 and 20.")

            except ValueError:
                print(f"{user_input} is not a valid number")
    
    etudiants.append({
        'nom' : fname,
        'notes' : notes
    })




def calculer_moyenne(notes):
    total = 0
    len = 0

    for note in notes:
        total += note
        len = len + 1

    return round(total / len, 2)

# print(calculer_moyenne(notes))

def appreciation(moyenne):
    if moyenne < 10:
        return "Insuffisant"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 16:
        return "Bien"
    else:
        return "Tres bien"
    
# print(appreciation(calculer_moyenne(notes)))


#module 2


etudiants = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
    {"nom": "Lina", "notes": [3, 9, 4]}
]


meilleur_etudiant = None
moins_bon_etudiant = None

meilleure_moyenne = None
moins_bonne_moyenne = None


for e in etudiants :
    nom = e['nom']
    e_notes = e['notes']
    moyenne = calculer_moyenne(e_notes)
    mention = appreciation(moyenne)


    if meilleure_moyenne is None or  moyenne > meilleure_moyenne:
        meilleure_moyenne = moyenne
        meilleur_etudiant = nom

    if moins_bonne_moyenne is None or moyenne < moins_bonne_moyenne:
        moins_bonne_moyenne = moyenne
        moins_bon_etudiant = nom


    # print(f'{nom} --- {moyenne} --- {mention}')


# print(f'meilleur : {meilleur_etudiant} ------- mois bon : {moins_bon_etudiant}')



#module 3
def sort_etudiant():

    resultat = {}
    for e in etudiants :
        nom = e["nom"]
        e_notes = e['notes']
        moyenne = calculer_moyenne(e_notes)
        mention = appreciation(moyenne)

        resultat[nom] = {
            'moyenne' : moyenne,
            'mention' : mention
        }

    return sorted(resultat.items() , key=lambda e : e[1]['moyenne'],reverse=True)

# print(sorted_etudiants)



echec_etudiants = []
for e in etudiants :
    nom = e["nom"]
    e_notes = e['notes']
    moyenne = calculer_moyenne(e_notes)
    if moyenne < 10 :
        echec_etudiants.append((nom,moyenne))

# print(echec_etudiants)



#defis
resultat_par_mention = {}
for e in etudiants :
    nom = e["nom"]
    e_notes = e['notes']
    moyenne = calculer_moyenne(e_notes)
    mention = appreciation(moyenne)

    if mention in  resultat_par_mention :
        resultat_par_mention[mention].append(e)
    else:
        resultat_par_mention[mention] = [e]
# print(resultat_par_mention)


etudiants_set = set(map(lambda e : e["nom"],etudiants))
if len(etudiants) > len(etudiants_set) :
    print('un nom est redouble')



groupe_a = {
    "Karim": {"moyenne": 12.0, "mention": "Bien"},
}
groupe_b = {
    "Karim": {"moyenne": 15.0, "mention": "Bien"},
    "Sara": {"moyenne": 17.0, "mention": "Tres bien"},
}

merged = {}



for nom, infos in groupe_a.items():
    merged[nom] = [infos]

for nom, infos in groupe_b.items():
    if nom in merged:
        merged[nom].append(infos)
    else:
        merged[nom] = [infos]

print(merged)


while True :
    choix = int(input('entrez votre choix\n1 -> ajouter un etudiant\n2 -> voir le classement\n3-> quitter\n '))
    match choix :
        case 1:
            ajouter_etudiant()
        case 2:
            res = sort_etudiant()
            for key , infos in res:
                print(f'{key} - {infos['moyenne']}')
        case 3 :
            quit(0)

