import os
import random

FILE_TO_READ = './archivos/data.txt'
MAX_MISTAKES = 10
WINNING_IMAGE_INDEX = 11

ALPHABET = ['A','B','C','D','E','F','G','H',
           'I','J','K','L','M','N','Ñ','O',
           'P','Q','R','S','T','U','V','W',
           'X','Y','Z']


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")


def print_logo():
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


def get_images():
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
    images = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10, 11: die11}
    return images


def read_word():
    word_li = []

    with open(FILE_TO_READ, 'r', encoding='utf-8') as data_words:
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


def new_word():
    word = read_word()

    dict_word = {i[0] : i[1] for i in enumerate(word)}
    discovered = ['- ' for i in range(len(dict_word))]

    return word, dict_word, discovered


def compare_letter(letter, dict_word, discovered, fail):
    for i in range(len(dict_word)):
        if dict_word.get(i) == letter:
            discovered[i] = letter + ' '
            fail = False
            
    return discovered, fail


def refresh(images, mistakes, available_letters):
    clearScreen()
    print_logo()
    print('Letras disponibles: ' + "  ".join(available_letters))
    print(images.get(mistakes))


def game_loop(images, word, dict_word, discovered):
    available_letters = ALPHABET.copy()
    mistakes = 0
    letter = ""
    end = False
    
    while True:
        refresh(images, mistakes, available_letters)
        print('¡Adivina la palabra!     ' + ''.join(discovered))

        while not letter in available_letters:
            letter = input('Ingresa una letra: ').upper()

            if not letter in available_letters:
                print('Debes ingresar una de las letras disponibles')

        available_letters[available_letters.index(letter)] = ''

        fail = True
        discovered, fail = compare_letter(letter, dict_word, discovered, fail)

        if fail:
            mistakes += 1

            if mistakes == MAX_MISTAKES:
                refresh(images, mistakes, available_letters)
                print('¡Perdiste! La palabra era ' + word)
                end = True
                
        if ''.join(discovered).replace(' ', '') == word:
            refresh(images, WINNING_IMAGE_INDEX, available_letters)
            print('Tuviste ', mistakes, ' errores      ' + ''.join(discovered))
            end = True

        if end:
            play_again = input('¿Quieres jugar otra vez? (1-Si / 0-No):  ') == "1"

            if play_again: 
                run()               
            else: 
                print('Gracias por jugar :)')

            break
            

def run():
    images = get_images()
    word, dict_word, discovered = new_word()
    game_loop(images, word, dict_word, discovered)


if __name__ == '__main__':
    clearScreen()
    run()
