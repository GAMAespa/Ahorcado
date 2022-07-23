import os
import random


def compare(letter,chosen_word, guess ):
    if letter in chosen_word:
        
        for i,x in enumerate(chosen_word):
            if x == letter:
                guess.insert(i, x)
                guess.pop(i + 1)
    return guess


def run():
    os.system("cls")
    with open("./archivos/data.txt", "r", encoding= "utf-8") as word:
        words_list = [i for i in word]
    run = True
    lives = 10
    guess = []
    chosen_word = words_list[random.randint(0, len(words_list) - 1)]
    chosen_word = list(chosen_word)
    chosen_word.pop(len(chosen_word) - 1)
    for i in chosen_word:
            guess.append("-")
    while chosen_word != guess and lives > 0:
        print("".join(guess) + "        " +str(lives) + "\u2764")
        chosen_letter = input("Escribe una letra: ")
        compare(chosen_letter, chosen_word, guess)
        lives -= 1
    if chosen_word == guess:
        print("felicitaciones ganaste")
        print("".join(guess))
        play = int(input("Quieres volver a jugar?: \n (1)Si (2)No, salir"))
        if play == 1:
            run()
        elif play == 2: 
            run = False
        else:
            play
    else:
        print("perdiste")
        try:
            play = int(input("Quieres volver a jugar?: \n (1)Si (2)No, salir"))
        except ValueError:
            print("Sea serio")
            play = 2
        if play == 1:
            run()
        elif play == 2: 
            run = False
        else:
            play


if __name__ == '__main__':
    run()