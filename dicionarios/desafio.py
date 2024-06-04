produtos={}
iteracao=1
quant_item=int(input("Informe quantos produtos você irá comprar: "))

while iteracao<=quant_item:
    prod=input(f"Informe qual é o {iteracao} produto: ")
    valor=float(input("Digite o valor do produto: R$ "))
    quant_prod=int(input("Qual a quantidade que você irá comparar: "))
    produtos.update({iteracao:[prod, valor, quant_prod]})
    iteracao+=1
total = 0 

print(50 * '-')
print('Carrinho de Compras')
print(50 * '-')

for cod, prod in produtos.items():
    subtotal = prod[1] * prod[2]
    print(f"{prod[0]} - R$ {prod[1]:.2f} - {prod[2]} unid - R$ {subtotal:.2f}")
    total += subtotal

print(50 * '-')
print(f"Total da compra: R$ {total:.2f}")
print(50 * '-')

 



