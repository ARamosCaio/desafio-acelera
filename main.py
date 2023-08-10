from song_funcs import song
from song_funcs import clean_verse
import time
import sys

ni = int(input('Insira o número de patinhos: '))
n = ni
while n >= 0:
    song(n, ni)
    time.sleep(2)
    n-=1
    clean_verse()

    