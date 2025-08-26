#Entrada cinema
print('\n')
estudante = False
idoso = False

nome = input("Seja bem-vindo ao CineJoas. Qual é o seu nome? ")
idade = input(f"Olá {nome}! Agora, por gentileza, digite sua idade: ")
idade_int = int(idade)

e_estudante = input(str(f"{nome}, você é estudante e está com documento comprovante? "))
if e_estudante.lower().rstrip().lstrip() == str:
    print('Você informou um valor inválido. Digite apenas "Sim", ou "Não".')
else:
    if e_estudante.lower().strip() == "sim":
        estudante = True

    if idade_int >= 60:
        idoso = True


    if idade_int <= 5:
        preco = 0
    elif idade_int <= 18:
        preco = 20
    elif estudante == True:
        preco = 15
    elif idoso == True:
        preco = 15
    else:
        preco = 30

    print(f"Certo. {nome}, o valor da sua entrada é R${preco},00.\nTenha uma ótima sessão!")