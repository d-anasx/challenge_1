fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

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


def calculer_moyenne(notes):
    total = 0

    for note in notes:
        total += note

    return round(total / len(notes), 2)


def appreciation(moyenne):
    if moyenne < 10:
        return "Insuffisant"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 16:
        return "Bien"
    else:
        return "Tres bien"
    


