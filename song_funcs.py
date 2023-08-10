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
        time.sleep(0.05)
        sys.stdout.flush()

def song(n, ni):
    clean_verse()
    if n == 0:
        sentence = (f'A mamãe patinha foi procurar\nAlém das montanhas\nNa beira do mar\nA mamãe gritou: Quá, quá, quá, quá\nE os {ni} patinhos voltaram de lá')
    elif n == 1:
        sentence = (f'{n} patinho foi passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas nenhum patinho voltou de lá')
    elif n == 2:
        sentence = (f'{n} patinhos foram passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só um patinho voltou de lá')
    else:
        sentence = (f'{n} patinhos foram passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só {n-1} patinhos voltaram de lá')
    lyrics(sentence)
        

