# 0 | 1 | 2 | 3 | 4
# 5 | 2 | 4 | 6 | 1
#

numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))
for i in range(tamanho):
    # 0 .. 5
    valor = int(input(f"Digite o número do vetor na posição {i}: "))
    numeros.append(valor)
print("Vetor: ", numeros)
print("Posição 1", numeros[1])

# BUSCA LINEAR
# Melhor caso: 1 vez O(1)
# Pior caso: N vezes O(n)
# Caso médio: n/2 vezes

numero_pesquisar = int(input("Digite o valor a ser pesquisado no vetor: ")) #2
posicao_resultado = -1
for i in range(tamanho):
    # 0 .. 5
    if numeros[i] == numero_pesquisar:
        posicao_resultado = i
        break
if posicao_resultado < 0:
    print("O elemento não foi encontrado no vetor")
else:
    print(f"Elemento encontrado na posição {posicao_resultado}")
# FIM BUSCA LINEAR

# SELECTION SORT
# 0 | 1 | 2 | 3 | 4
# 5 | 2 | 4 | 6 | 1
# 1 | 2 | 4 | 6 | 5
# 1 | 2 | 4 | 5 | 6

# Melhor caso: N * N = N^2 O(n^2)
# Pior caso: N * N = N^2 O(n^2)
# Caso médio: N * N = N^2

for i in range(tamanho): # N
    indice_menor = i #5
    for j in range(int(i + 1), tamanho): # N
        if numeros[j] < numeros[indice_menor]:
            indice_menor = j
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
    print("vetor:", numeros)

# FIM SELECTION SORT

# BUSCA BINÁRIA
# 2
# 1 | 2 | 4 | 5 | 6
# 1 | 2
# 2

resultado = -1
inicio = 0
fim = tamanho - 1
meio = 0
alvo = int(input("Digite o elemento a ser encontrado: "))
while inicio <= fim:
    meio = int((inicio + fim) / 2)
    if (numeros[meio] < alvo):
        inicio = meio + 1
    elif (numeros[meio] > alvo):
        fim = meio - 1
    else:
        resultado = meio
        break
if resultado < 0:
    print("Elemento não encontrado")
else:
    print(f"O elemento {alvo} está na posição {resultado}")
# FIM BUSCA BINÁRIA