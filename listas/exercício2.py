numeros=[]
iteracao=1
while iteracao <= 5:
    resposta= int(input(f"Digite {iteracao}º números inteiros: "))
    numeros.append(resposta)
    iteracao+=1

print(f" Sua lista ficou da seguinte forma: {numeros}")
print(f" A soma de todos os númros da lista é de: {sum(numeros)}")
print(f" O maior número da lista é: {max(numeros)}")
print(f" O menor número da lista é: {min(numeros)}")
print(f" A média dos números da lista é de: {sum(numeros)/len(numeros)}")

