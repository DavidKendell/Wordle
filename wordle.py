from collections import Counter
import random
import time
from urllib.request import urlopen



def reveal(word: str, guess: str, keyboard: dict):
    countOfLetters = Counter(list(word))
    lettersToPrint = ["", "", "", "", ""]
    for i in range(5):
        if (word[i].lower() == guess[i].lower()):
            lettersToPrint[i] = guess[i].upper()
            countOfLetters[guess[i]] -= 1
            keyboard[guess[i].upper()] = guess[i].upper()

    for i in range(5):
        if (word[i].lower() == guess[i].lower()):
            continue
        if (guess[i].lower() in word and countOfLetters[guess[i]] > 0):
            lettersToPrint[i] = guess[i].lower()
            keyboard[guess[i].upper()] = guess[i].lower() if keyboard[guess[i].upper()] == "^" + guess[i].upper() else keyboard[guess[i].upper()]



            countOfLetters[guess[i]] -= 1
        else:
            lettersToPrint[i] = '*' + guess[i].lower()
            keyboard[guess[i].upper()] = '*' + guess[i].lower() if keyboard[guess[i].upper()] == "^" + guess[i].upper() else keyboard[guess[i].upper()]
    for letter in lettersToPrint:
        print(letter, end=" ", flush = True)
        time.sleep(0.55)


def printKeyboard(keyboard: dict):
    keys = list(keyboard.values())
    print(" ".join(keys[0:10]))
    print(end=" ")
    print(" ".join(keys[10:19]))
    print(end="  ")
    print(" ".join(keys[19:26]))


guessCount = 6


word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
response = urlopen(word_site)
txt = response.read().decode('UTF-8')

WORDS:str = txt.splitlines()
short_words:list = [word for word in WORDS if len(word) == 5]
randomword = (random.choice(short_words))
print("You have six tries to guess a five letter word.")
print("Your guess will be output to the console, formatted based on the correct letters")
print("A correct letter in the right place will show as a capital letter")
print("A correct letter in the wrong place will be lowercase")
print("Wrong letters will have an asterisk before them")
print("Example: the word is HELLO and you guess HOMES")
print("The output will be H o *m e *s")
print()
temp:str = "QWERTYUIOPASDFGHJKLZXCVBNM"
keyboard:dict = dict.fromkeys(temp)
for key in keyboard:
    keyboard[key] = '^' + key
lost:bool = True
while (guessCount > 0):
    printKeyboard(keyboard)
    guess = input("Guess the word ")
    if (guess.isalpha() and len(guess) == 5 and guess in short_words):
        reveal(randomword, guess, keyboard)
        print()
        guessCount -= 1
    if (guess == randomword):
        lost = False
        break
if (lost):
    for letter in randomword:
        print(letter.upper(), end=" ", flush = True)
        time.sleep(0.55)

