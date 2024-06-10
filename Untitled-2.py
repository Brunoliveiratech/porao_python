numero=1
max=int(input('digite um numero maximo para o laço while'))
print('numeros pares entre 1 e',max)
while numero<= max:
    if numero%2==0:
        print(numero,end-"")
        numero+=1