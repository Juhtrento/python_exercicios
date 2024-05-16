print("Bem-vindo(a) a paridade dos números!!! ")
soma = 0
iteracao = 0
impar = 0
par = 0
while iteracao<5:
    num=int(input('Informe um número: '))
    if num%2==0:
        print('Seu número é par')
        par+=1
    else:
        print("Seu número é impar")
        impar+=1
    iteracao+=1
print(f'{par} são pares')
print(f'{impar} são ímpares')