numero=1 
max=int(input('digite um numero maior que 1:'))
print("numeros impares entre 1 e ",max,':')
while numero <= max:
    if numero%2==1:
        print(numero, end=" ")
        numero+=2