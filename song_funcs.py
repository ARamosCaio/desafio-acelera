from num2words import num2words
import platform
import os
import time
import sys

def clean_verse():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def lyrics(sentence):
    for letter in sentence:
        print(letter, end="")
        time.sleep(0.08)
        sys.stdout.flush()

def song(n, ni):
    clean_verse()
    num = num2words(n, lang='pt_BR').capitalize()
    numi = num2words(ni, lang='pt_BR')
    if n == 0:
        sentence = (f'A mamãe patinha foi procurar\nAlém das montanhas\nNa beira do mar\nA mamãe gritou: Quá, quá, quá, quá\nE os {numi} patinhos voltaram de lá')
    elif n == 1:
        sentence = (f'{num} patinho foi passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas nenhum patinho voltou de lá')
    elif n == 2:
        sentence = (f'{num} patinhos foram passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só um patinho voltou de lá')
    else:
        sentence = (f'{num} patinhos foram passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só {num2words(n-1, lang="pt-br")} patinhos voltaram de lá')
    lyrics(sentence)
        

