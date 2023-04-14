# def say_hello():
#     print("Hello")

# a = 3
# b = 5
# say_hello()
# print(a+b)

from random import randint, choice

def say_hello():
    words = ["Bonjour", "Hello", "Ciao", "Ola"]
    index = randint(0, len(words) - 1)
    print(words[index])

def say_hello_v2():
    words = ["Bonjour", "Hello", "Ciao", "Ola"]
    print(choice(words))

for _ in range(100):
    say_hello()