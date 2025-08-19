def verifica_numero(msg):
    escolha = input(msg)
    while not escolha.isnumeric():
        escolha = input(msg)
    return int(escolha)

def escolher_opcao(lista, msg):
    opcoes = '\n'.join(lista)
    print("\n==============================")
    escolha = input(f"{msg}\n{opcoes}\n-> ")
    while escolha not in lista:
        escolha = input(f"\n{msg}\n{opcoes}\n-> ")
    return escolha

def maior_valor(lista):
    indiceMaior = 0
    maior = lista[indiceMaior]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indiceMaior = i
    return indiceMaior

def menor_valor(lista):
    indiceMenor = 0
    menor = lista[indiceMenor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indiceMenor = i
    return indiceMenor

def valor_medio(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    return media

def achar_indice(lista, escolha):
    for i in range(len(lista)):
        if escolha == lista[i]:
            indice = i
            break
    return indice


print("Boas vindas a nossa vinheria!!")
anoNascimento = verifica_numero("Qual seu ano de nascimento?\n-> ")
idade = 2025 - anoNascimento

if idade < 18:
    print("Você é menor de idade, não pode beber!!")
else:
    vinhos = ['Dom Bosco', 'Goes', 'Pérgola', 'Cabernet Sauvignon']
    precos = [17, 15, 23, 70]
    quantidadeVinhos = [0] * len(vinhos)

    subtotal = 0

    endereco = input("Qual seu endereço?\n-> ")

    custoMedio = valor_medio(precos)
    vinhoCaro = maior_valor(precos)
    vinhoBarato = menor_valor(precos)
    print(f"O custo médio dos vinhos de nossa vinheria é {custoMedio}, "
          f"sendo o {vinhos[vinhoCaro]} o mais caro, custando R${precos[vinhoCaro]}, e {vinhos[vinhoBarato]} o mais barato, custando R${precos[vinhoBarato]}.")

    while True:

        vinhoEscolhido = escolher_opcao(vinhos, "Qual vinho deseja comprar?\n")
        quantidadeEscolhida = verifica_numero("Quantas garrafas deseja comprar?\n-> ")
        indiceVinho = achar_indice(vinhos, vinhoEscolhido)
        quantidadeVinhos[indiceVinho] += quantidadeEscolhida

        encerrar = escolher_opcao(['Continuar', 'Encerrar'], "Deseja encerrar a compra?")
        if encerrar == "Encerrar":
            break

    for i in range(len(vinhos)):
        subtotal += precos[i] * quantidadeVinhos[i]

    if subtotal > 500:
        frete = 0
        print("\nO seu pedido ultrapassou o valor de R$500,00 e você ganhou FRETE GRÁTIS!!")
    else:
        frete = subtotal * 0.07

    total = subtotal + frete
    print("\n==============================")
    print(f"Agradecemos a compra em nossa loja! O seu pedido será entregue no endereço: {endereco}.\n"
          
          f"\nQuantidade de cada garrafa:")
    for i in range(len(vinhos)):
        print(f"{vinhos[i]} - {quantidadeVinhos[i]} garrafa(s)")

    print(f"\nO total do seu pedido é R${total:.2f}.")
