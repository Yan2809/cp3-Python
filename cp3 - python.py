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
        escolha = input(f"{msg}\n{opcoes}\n-> ")
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

#AQUI
def buscar_indice(lista, opcao):
    for i in range(len(lista)):
        if opcao == lista[i]:


vinhos = ['Dom Bosco', 'Goes', 'Pérgola', 'Cabernet Sauvignon']
precos = [17, 15, 23, 70]


print("Boas vindas a nossa vinheria!!")
anoNascimento = verifica_numero("Qual seu ano de nascimento?\n-> ")
if anoNascimento < 18:
    print("Volta pra sua mamadeira!!!")
else:
    endereco = input("Qual seu endereço?\n-> ")
    custoMedio = valor_medio(precos)
    vinhoCaro = maior_valor(precos)
    vinhoBarato = menor_valor(precos)
    print(f"O custo médio dos vinhos de nossa vinheria é {custoMedio}, "
          f"sendo o {vinhos[vinhoCaro]} o mais caro e {vinhos[vinhoBarato]} o mais barato.")
    vinhoEscolhido = escolher_opcao(vinhos, "Qual vinho deseja comprar?\n-> ")
    quantidade = verifica_numero("Quantas garrafas deseja comprar?\n-> ")

    #AQUI
    indiceVinho =
    subtotal += quantidade *