#Listas - Armazenam vários elementos em ordem

lista = ['Vinicius Horacio', 9.0, 10.0, 9.5, True]
#                [0]         [1]  [2]   [3]   [4] 
#                [-5]       [-4]  [-3]  [-2]  [-1] 

print(lista[-5])


for elemento in lista: 
    print(elemento)

lista[3] = 10.0

media = (lista[1] + lista[2] + lista[3])/3
print(media)

#Manipulação de Listas

    #(1) Quantidade de elementos
print(len(lista))

    #(2) Partição de elementos - nomeDaLista[inicio:fim] 
print(lista[1:4])
print(lista[:3])
print(lista[3:])

    #(3) Adição de elementos ao final da lista - obj.append()
lista.append(media)
print(lista)

    #(4) Adiciona vários elementos ao final da lista - obj.extend([])
lista.extend([10.0, 7.0, 8.0])
print(lista)

    #(5) Remove um elemento específico em uma lista - obj.remove()
lista.remove(7.0)
print(lista)

    #(6) Insere elementos em uma determinada posição da lista - obj.insert(indice, elemento)
lista.insert(1, 'Victor')
print(lista)

    #(7) Remove o elemento de uma determinada posição da lista - obj.pop(indice)
lista.pop(1)
print(lista)

    #(8) Retorna o índice de um elemento específico - obj.index(elemento)
lista.index('Vinicius Horacio')
print(lista)

    #(9) Organiza os elementos da lista em ordem crescente ou decrescente - obj.sort() 
lista.sort()
print(lista)


#Dicionários -> dicionario = {key: valor}
dicionario = {'chave_1': 1, 'chave_2':2}
print(dicionario)

dicionario = {'chave_1': 1, 'chave_2':2}
print(dicionario)


cadastro = {'matricula': 123,
'diaCadastro': 25,
'mesCadastro': 9,
'turma': '2E'}

print(cadastro['matricula'])

    #(1) Atualizar valor do dicionário
cadastro['matricula'] = 245
print(cadastro['matricula'])

    #(2) Adicionar novos dados ao dicionário
cadastro['modalidade'] = 'EAD'
print(cadastro)

    #(3) Remove o item do dicionário e retorna ele
cadastro.pop('turma')
print(cadastro)

    #(4) Retrona uma lista de pares chave-valor do dicionário
print(cadastro.items())

    #(5) Retorna uma lista das chaves do dicionário
print(cadastro.keys())

    #(6) Retorna uma lista dos valores do dicionário
print(cadastro.values())

#Leitura de valores com FOR

for chaves in cadastro.keys():
    print(cadastro[chaves])

for valores in cadastro.values():
    print(valores)

for chaves, valores in cadastro.items():
    print(chaves, valores)

#Exercício1 | Código que gere uma lista contendo o percentual de crescimento de bactérias por dia 

colonia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentual_crescimento = []

for i in range(1, len(colonia)):
    amostraAtual = colonia[i]
    amostraPassada = colonia[i - 1]
    percCrescimento = 100 * (amostraAtual - amostraPassada) / amostraPassada
    percentual_crescimento.append(percCrescimento)

print(percCrescimento)


#Exercicio2 | Programa que informa a nota de um aluno de acordo com as suas respostas. Ele deve pedir a resposta de um aluno para cada questao e verifica se é igual ao gabarito

notas = []
somaNotas = 0
acertos = 0
for i in range(3):
    nota = input(f"Digite a sua resposta da questao {i+1}: ")

    if i == 0 and nota == 'A':
        notas.append(10)
        acertos +=1
    elif i == 1 and nota == 'B':
        notas.append(10)
        acertos +=1
    elif i == 2 and nota == 'D':
        notas.append(10)
        acertos +=1
    else:
        notas.append(0)
       

somaNotas = sum(notas)
print("Resultado da prova:", somaNotas)
print("O total de acertos foi:", acertos)

