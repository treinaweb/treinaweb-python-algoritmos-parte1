# 0 | 1 | 2 | 3 | 4
# 5 | 2 | 4 | 6 | 1

numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))
for i in range(tamanho):
    # 0 .. 5
    valor = int(input(f"Digite o número do vetor na posição {i}: "))
    numeros.append(valor)
print("Vetor: ", numeros)
print("Posição 1", numeros[1])
