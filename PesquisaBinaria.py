# Criação da Lista
lista = []
# Definindo o tamanho da lista:
for indc in range(101):
    lista.append(indc)

# Definindo o número a ser encontrado
sort = 51
#Numeros de tentativas
tentativa = 1

# inicio da Função
def pesquisaBinaria(lista,sort,tentativa):
    print(f"=========================== TENTATIVA {tentativa} ========================")
    tentativa += 1
    # Definindo o chute do algoritmo (Sempre será o meio, no caso o número 50)
    chute = lista[int( len(lista) / 2 )]

   # Definindo o limite a ser percorrido na lista, nesse caso
    limite = lista[0]
    print(f"chute: {chute} | limite: {limite}")

    # Se o chute for o número sorteado, o programa para
    if chute == sort:
        print("Venceu")
    # Senão, ele continua procurando o número, com base na dica do sistema(Se o chute for maior que o número selecionado ou menor )
    else:
        # Se o chute for maior...
        if chute > sort:
            print("O chute foi Maior")
            # Reatribuindo o chute
            chute = lista[int(len(lista) / 2)]
            # Esvaziando a lista a fim dela ser recriada com os possíveis números escolhidos
            lista = []
            # Recriando a lista
            for num in range(limite, chute):
                lista.append(num)

            print(f"Lista: {lista}")
            # Se não for achado o número, a função se chama para recomeçar a partir da nova lista, senão finaliza
            pesquisaBinaria(lista, sort, tentativa) if chute != sort else print("venceu")
        # Se o chute for menor...
        else:
            print("Menor")
            print(f"previsão de chute: {lista[int(len(lista) / 2)]}")
            # Define o meio da lista
            chute = lista[int(len(lista) / 2)]
            # Define um novo limite da lista(A partir do meio até o fim da lista )
            limite = lista[len(lista) - 1]

            #Esvaziando a lista
            lista = []
            # Recriando a lista
            for num2 in range((chute + 1), (limite + 1)):
                lista.append(num2)
            print(f"Lista: {lista}")
            #Termina o programa ou retorna
            pesquisaBinaria(lista, sort, tentativa) if chute != sort else print("venceu")

# Chamando a função
pesquisaBinaria(lista,sort,tentativa)