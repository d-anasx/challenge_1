



fname = input("enter your first name : ")
lname = input("enter your last  name : ")


notes = []

x = 0
while x < 3 : 
    while True :
        user_input =  input(f"enter your note {x+1} : ")
        try :
            note = float(user_input)
            if note > 0 and note <= 20 :
                notes.append(note)
                x = x+1
                break
            
        except ValueError :
            print(f'{user_input} is not a valid number')


def average() :
    sum = 0
    for i in notes:
        sum =sum + i
    avg = round(sum / len(notes),2)
    return avg

def appreciation(avg) :
    if avg >= 10 :
        return 'passable'
    if avg >=12 :
        return 'assez bien'
    if avg >= 14 :
        return 'bien'
    if avg >=16 :
        return 'tres bien'
    if avg >=18 :
        return 'exellent'










