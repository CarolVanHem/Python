from random import randint

def create_word(num_letters) :
    letters = ["a", "h", "k", "o", "n", "s", "t"]

    word = ""

    for _ in range(num_letters) :
        index = randint(0, len(letters) - 1 )
        word = word + letters[index]
    
    return word

word_length = input("Combien de lettre(s) : ")
word_length = int(word_length)

print(create_word(word_length))

