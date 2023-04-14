from random import randint

code_length = 4

possibilities = ["a", "b", "c", "d", "e", "f"]
print(possibilities)

code = []

for _ in range(code_length):
    index = randint(0, len(possibilities)-1)
    value = possibilities[index]

    code.append(value)
    
print(code)

answer = None
essais = 12

while answer != code and essais > 0:
    
    answer = input("Devinez le code à "+str(code_length)+" lettres (vous avez " + str(essais) + " essais) : ")

    essais = essais - 1
    
    while len(answer) != 4:
        print("Pas le bon nombre de lettres !")
        answer = input("Donnez moi un code à "+str(code_length)+" lettres :")

    answer = list(answer)
    print(answer)

    correct_places = []

    for index in range(code_length):
        if answer[index] == code[index]:
            correct_places.append(index)
        
    print("Lettres bien placée(s) : "+str(len(correct_places)))

    wrong_places = []

    for index_answer in range(len(answer)):
        for index_code in range(len(code)):
            if answer[index_answer] == code[index_code] and index_code not in correct_places and index_answer not in correct_places and index_code not in wrong_places:
                wrong_places.append(index_code)
                break
        
    print("letters mal placée(s) : " + str(len(wrong_places)))

if answer == code:
    print("Bravo ! Tu es le mastermind !!")