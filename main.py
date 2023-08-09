from song_funcs import song

ni = int(input('Insira o número de patinhos: '))
n = ni
while n > 0:
    song(n, ni)
    n-=1
