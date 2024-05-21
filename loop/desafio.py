tentativa=3
senha=123456
nome=input('Digite seu nome:')
while tentativa>0:
    senha_digitada=int(input("Digite sua senha: "))
    if senha != senha_digitada:
        tentativa-=1
        print(f'Senha incorreta! Você tem {tentativa} tentativas')
        if tentativa==0:
            print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas')
    else:
        print(f'Olá,{nome}. Bem vindo(a) ao nosso banco!!!')
        break
    
   



