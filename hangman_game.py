import os
import random
import time
from functools import reduce


def logo_hangman():
    print('''

    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
''')


def image_hangman():
    die0 = '''













'''
    die1 = '''







        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die11 = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / '''+chr(92)+'''
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10, 11: die11}
    return deaths


def read_word():
    word_li = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as data_words:
        word = random.choice([word.strip().upper() for word in data_words])
    for letter in word:
        if letter == 'Á':
            letter = 'A'
        elif letter == 'É':
            letter = 'E'
        elif letter == 'Í':
            letter = 'I'
        elif letter == 'Ó':
            letter = 'O'
        elif letter == 'Ú':
            letter = 'U'
        word_li.append(letter)
    return ''.join(word_li)


def new_word(word, dict_word, discovered, deaths, letters):
    word = read_word()
    dict_word = {i[0] : i[1] for i in enumerate(word)}
    discovered = ['- ' for i in range(len(dict_word))]
    deaths = 0
    letters = ['A','B','C','D','E','F','G','H',
               'I','J','K','L','M','N','Ñ','O',
               'P','Q','R','S','T','U','V','W',
               'X','Y','Z']
    return word, dict_word, discovered, deaths, letters


def compare_letter(letter, dict_word, discovered, fail):
    for l in range(len(dict_word)):
        if dict_word.get(l) == letter:
            discovered[l] = letter + ' '
            fail = False
    return discovered, fail


def refresh(hangman_deaths,deaths,letters):
    os.system('clear')
    logo_hangman()
    print('Letras disponibles: '+"  ".join(letters))
    print(hangman_deaths.get(deaths))


def game_loop(hangman_deaths, deaths, letters, non_letter, discovered, dict_word, word):
    while True:
        refresh(hangman_deaths, deaths, letters)
        if non_letter == 1:
            print('Debes ingresar una de las letras disponibles')
            non_letter = 0
        try:
            letter = input('''¡Adivina la palabra!     ''' + ''.join(discovered) + '''
    Ingresa una letra: ''').upper()
            letters[letters.index(letter)] = ''
        except ValueError:
            non_letter = 1
        fail = True
        discovered, fail = compare_letter(letter, dict_word, discovered, fail)
        if fail == True:
            deaths += 1
            if deaths == 10:
                refresh(hangman_deaths, deaths, letters)
                print('¡Perdiste! La palabra era ' + word)
                again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
                if again == '1':
                    word, dict_word, discovered, deaths, letters = new_word(word, dict_word, discovered, deaths,
                                                                            letters)
                    continue
                else:
                    print('Gracias por jugar :)')
                    break
        if ''.join(discovered).replace(' ', '') == word:
            refresh(hangman_deaths, 11, letters)
            print('Tuviste ', deaths, ' erorres      ' + ''.join(discovered))
            again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
            if again == '1':
                word, dict_word, discovered, deaths, letters = new_word(word, dict_word, discovered, deaths, letters)
                continue
            else:
                print('Gracias por jugar :)')
                break

def run():
    hangman_deaths = image_hangman()
    word = ''
    dict_word = {}
    discovered = []
    deaths = 0
    letters = []
    non_letter = 0
    word, dict_word, discovered, deaths, letters = new_word(word, dict_word, discovered, deaths, letters)
    game_loop(hangman_deaths, deaths, letters, non_letter, discovered, dict_word, word)


if __name__ == '__main__':
    os.system('clear')
    run()
