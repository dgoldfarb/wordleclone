import colorama
from colorama import Fore
import random
words = list()
filename = "words.txt"
with open (filename) as fin:
        for line in fin:
                words.append(line.strip())
word=(random.choice(words))


i=0
n=0
guess=""
while(guess!= word and n<6):
    guess=input("\n"+Fore.LIGHTWHITE_EX+"please guess a word: ")
    if(len(guess)==5 and guess in words):
        for letters in guess:

            if letters == word[i]:
                print(Fore.LIGHTGREEN_EX+(letters)+Fore.LIGHTWHITE_EX, end=" ")
            elif letters in word:
                print(Fore.LIGHTYELLOW_EX+(letters)+Fore.LIGHTWHITE_EX, end =" ")
            else:
                print(Fore.LIGHTRED_EX+(letters)+Fore.LIGHTWHITE_EX, end=" ")

            i+= 1
        n += 1
    else:
        print("only five letter real words are accepted")

    i = 0
if(n<6 and word ==guess):
    print(Fore.LIGHTWHITE_EX+"congrats you guessed the word!")
else:
    print("\n you lost the word was "+Fore.CYAN+word)

