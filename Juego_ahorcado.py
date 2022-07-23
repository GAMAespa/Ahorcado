import os
import random
from colorama import Back, Fore, init


ahorcado_image_ascci = """

                       .-'''-.                   _..._                               .-'''-.     
                      '   _    \              .-'_..._''.           _______         '   _    \   
            .       /   /` '.   \           .' .'      '.\          \  ___ `'.    /   /` '.   \  
          .'|      .   |     \  '          / .'                      ' |--.\  \  .   |     \  '  
         <  |      |   '      |  '.-,.--. . '                        | |    \  ' |   '      |  ' 
    __    | |      \    \     / / |  .-. || |                 __     | |     |  '\    \     / /  
 .:--.'.  | | .'''-.`.   ` ..' /  | |  | || |              .:--.'.   | |     |  | `.   ` ..' /   
/ |   \ | | |/.'''. \  '-...-'`   | |  | |. '             / |   \ |  | |     ' .'    '-...-'`    
`" __ | | |  /    | |             | |  '-  \ '.          .`" __ | |  | |___.' /'                 
 .'.''| | | |     | |             | |       '. `._____.-'/ .'.''| | /_______.'/                  
/ /   | |_| |     | |             | |         `-.______ / / /   | |_\_______|/                   
\ \._,\ '/| '.    | '.            |_|                  `  \ \._,\ '/                             
 `--'  `" '---'   '---'                                    `--'  `"                              
"""


def compare(letter,chosen_word, guess ):
    if letter in chosen_word:
        for i,x in enumerate(chosen_word):
            if x == letter:
                guess.insert(i, x)
                guess.pop(i + 1)
    return guess


def run():
    init()
    os.system("cls")
    with open("./archivos/data.txt", "r", encoding= "utf-8") as word:
        words_list = [i for i in word]
    guess = []
    chosen_word = words_list[random.randint(0, len(words_list) - 1)]
    chosen_word = list(chosen_word)
    chosen_word.pop(len(chosen_word) - 1)
    for i in chosen_word:
            guess.append("-")
    while chosen_word != guess:
        print(Back.RED + Fore.BLACK + ahorcado_image_ascci + Fore.RESET + Back.RESET)
        print(Fore.RED + "".join(guess))
        chosen_letter = input("Escribe una letra: ")
        compare(chosen_letter, chosen_word, guess)
    if chosen_word == guess:
        print("felicitaciones ganaste")
        print("".join(guess))


if __name__ == '__main__':
    run()