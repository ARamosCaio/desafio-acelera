ni = int(input('Insira o número de patinhos: '))
n = ni
while n > 0:
    if n == 1:
        print(f'{n} patinhos foram passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas nenhum patinho voltou de lá')

    else:
        print(f'{n} patinhos foram passear \nAlém das montanhas \nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só {n-1} patinhos voltaram de lá')
    n -= 1

if n == 0:
    print(f'A mamãe patinha foi procurar\nAlém das montanhas\nNa beira do mar\nA mamãe gritou: Quá, quá, quá, quá\nE os {ni} patinhos voltaram de lá')
