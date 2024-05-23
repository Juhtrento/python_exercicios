numeros=[]
iteracao=1
while iteracao <= 5:
    resposta= int(input(f"Digite {iteracao}º números inteiros: "))
    numeros.append(resposta)
    iteracao+=1

print(numeros)
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros)/len(numeros))

