from random import randint
def num_aleatorio():
    aleatorio=randint(1,10)
    chute=10
    while aleatorio!= chute:
        chute=int(input('digite um valor (entre 1 e 10:'))
    if (aleatorio== chute):
        print('parabens, voce acertou!')
    else:
        print('tente novamente.')
        num_aleatorio()