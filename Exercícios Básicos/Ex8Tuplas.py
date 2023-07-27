
#Tuplas

estudantes = ["Vinicius", "Horacio", "Victor"]

from random import randint #Escolhe gerando um numero dentro de um intervalo


def geraCodigo():
    return str(randint(0,999))

codigoEstudantes = []

for i in range(len(estudantes)):
    codigoEstudantes.append((estudantes[i], estudantes[i][0] + geraCodigo()))


print(codigoEstudantes)


#List comprehension - maneira mais simples de criar listas


notas = [[8, 9, 10], [2,4,7], [5,9,20]]


def media(lista: list = [0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo
    
    
medias = [round(media(nota),1) for nota in notas]

print(medias)

#Lista de listas filtrando apenas os estudantes

nomes = [('Vinicius', 'J230'), ('Victor', 'M200')]
medias = [2.0, 8.0, 9.9]

#nomes = [exp for item in lista]

nomes = [nome[0] for nome in nomes]
print(nomes)

#Para conseguirmos parear as médias e nomes, basta utilizar a função zip()

estudantes = list(zip(nomes, medias))
print(estudantes)

#Lista de Candidatos á bolsa

candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
print(candidatos)

#Lista Comprehension com If e Else -> [resultadoIf if cond else resultadoElse for item in lista]

nomes = [('Vinicius', 'J230'), ('Victor', 'M200'), ('Lucas', 'K230')]
notas = [[8, 9, 10], [2,4,7], [5,9,20]]
medias = [9.0, 4.3, 11.3]

situacao = ['Aprovado' if media >= 6 else 'Reprovado' for media in medias]
print(situacao)


#Gerando listas de listas

cadastro = [x for x in  [nomes, notas, medias]]
print(cadastro)

listCompleta = [nomes, notas, medias, situacao]

print(listCompleta)

#Dict Comprehension
#Acessando a Tupla

listCompleta = [
    [('Vinicius', 'J230'), ('Victor', 'M200'), ('Lucas', 'K230')],
    [8, 9, 10],
    [2, 4, 7],
    [5, 9, 20],
    [9.0, 4.3, 11.3]
]

colunas = ["Notas", "Média Final", "Situação"]


cadastro = {}


#Associe cada coluna a uma sublista da lista listCompleta
for i in range(len(colunas)):
    cadastro[colunas[i]] = listCompleta[i + 1]

print(cadastro)


cadastro["Estudante"] = [listCompleta[0][i][0] for i in range(len(listCompleta[0]))] #Acessa o nome na Tupla
print(cadastro)


#Exercício 1 | Soma dos elementos de uma lista

lista = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]


def soma(lista: list = [0]) -> float:
    calculo = sum(lista)
    return calculo
    

for sublista in lista:
    print("Soma dos elementos:", sum(sublista))


#Exercício 2 | Usando Dict Comprehension pra juntar 2 listas

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

column = ['Meses', 'Valores']
listComp = [meses, despesa]

cadastro = {column[i]: listComp[i] for i in range(len(column))}
print(cadastro)


#Exercício 3 | Criando uma lista utilizando o List Comprehension

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

def glic(glicemia: list) -> str:
    if glicemia[0] < 70:
        return 'Hipoglicemia'
    elif 70 <= glicemia[0] <= 99:
        return 'Normal'
    elif 100 <= glicemia[0] < 125:
        return 'Alterada'
    else:
        return 'Diabetes'
    
#(i+1) -> O primeiro elemento da tupla é o índice 'i' incrementado em 1
#glic([valor]) -> é o resultado da função glic que recebe como argumento uma lista com um único elemento 'valor' -> retorna um dos seguintes strings 'Hipoglicemia','Normal...
#valor -> é o próprio valor presente na lista 'glicemia' obtido através do loop 'for i, valor in enumarate(glicemia)' 
#enumerate -> OBTÉM O ÍNDICE I E O VALOR CORRESPONDENTE "VALOR" EM CADA ITERAÇÃO DO LOOP
situacao = [(i+1, glic([valor]), valor) for i, valor in enumerate(glicemia)]

print('\n'.join(str(item) for item in situacao))
