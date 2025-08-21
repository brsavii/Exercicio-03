capacidade = 100
valores = [None] * capacidade
ultima_posicao = -1

def inserir(valor):
    global ultima_posicao
    if ultima_posicao == capacidade - 1:
        print("Mensagem de vetor cheio")
    else:
        ultima_posicao += 1
        valores[ultima_posicao] = valor

def imprimir():
    if ultima_posicao == -1:
        print("Mensagem de vetor vazio")
    else:
        for i in range(ultima_posicao + 1):
            print(i, '-', valores[i])

def pesquisar(valor):
    for i in range(ultima_posicao + 1):
        if valores[i] == valor:
            return i
    return -1

def excluir(valor):
    global ultima_posicao
    posicao = pesquisar(valor)
    if posicao == -1:
        return -1
    else:
        for i in range(posicao, ultima_posicao):
            valores[i] = valores[i + 1]
        ultima_posicao -= 1

nome = "Bruna"
for letra in nome:
    inserir(letra)

print("Vetor após inserção:")
imprimir()

print("\nPesquisas:")
for letra in ['B', 'u', 'a']:
    pos = pesquisar(letra)
    print(f"Caractere '{letra}' encontrado na posição: {pos}")

excluir(nome[0])
excluir(nome[len(nome)//2])
excluir(nome[-1])

print("\nVetor após exclusões:")
imprimir()
