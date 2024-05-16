quant = int(input("Informe quantos números você quer calcular: "))
iteracao = 1
soma = 0
while iteracao<=quant:
    nums=float(input('Informe um número: '))
    soma+=nums
    iteracao+=1
print(f'A média dos números infprmados é igual a: {soma/quant}')