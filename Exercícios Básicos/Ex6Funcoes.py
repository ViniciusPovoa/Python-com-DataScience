import matplotlib #importação de biblioteca
from random import choice #Usado para apenas a importação de um método da biblioteca


estudantes = ["Joao", "Maria", "Jose"]
notas = [8.5, 9, 10]

help(choice)

estudante = choice(estudantes) #Escolha aleatoria do choice dentro de Estudante
print(estudante)

#Biblioteca Math com arredondamento para maior
import math

receita = 1000
unidade = 15

print(f" A empresa vendeu aproximadamente {math.ceil(receita/unidade)} unidades")

#Built-in Functions

notas = {'1 Trimestre': 9.5, '2 Trimestre': 10.0, '3 Trimestre': 8}
print(notas)

soma = 0
for nota in notas.values():
    soma = soma + nota
print('Soma total: ',soma)

somatorio = sum(notas.values())
print('Soma com método sum: ',somatorio)

qtdNotas = len(notas)
print('Quantidade de notas:', qtdNotas)

media = somatorio / qtdNotas
print(media)
media = round(media,1) #Arredonda 1 casa decimal
print(media)

 
#Criando funções
def media():
    calculo = (10 + 9 + 8) / 3
    print(calculo)

media()

#Função com Parâmetro
def media(nota1, nota2, nota3):
    calculo = (nota1 + nota2 + nota3) / 3
    print(calculo)

media(2, 3, 4)

#Funções com Built-in
notas = [2, 4, 5, 7]

def media(lista):
    calculo = sum(lista) / len(lista)
    print(calculo)

media(notas)

#Função com Return
def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo

resultado = media(notas)
print(resultado)

#Tuplas - 2 Returns

def boletim(lista):
    media = sum(lista) / len(lista)
    
    if media >= 6:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    return(media, situacao) #Isso é uma TUPLA
    
print(boletim(notas))

media, situacao = boletim(notas) #Puxa valores da Tupla separadamente

print(media)
print(situacao)

#Função Lambda -> Não precisa ser definida e consegue resolver um problema em uma linha

notas = float(input('Digite a nota do estudante'))

                #    |> X seria o parâmetro da função
qualitativo = lambda x: x + 0.5 
                    #     |> x + 0.5 seria o retorno da função
print(qualitativo(notas))
    
#Lâmbda com Média Ponderada
    
n1 = float(input('Digite a nota n1 do estudante'))
n2 = float(input('Digite a nota n2 do estudante'))
n3 = float(input('Digite a nota n3 do estudante')) 

mediaPonderada = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10
mediaEstudante = mediaPonderada(n1, n2, n3)
print(mediaEstudante)

#Map com Lâmbda

notas = [6.0, 7.0, 9.0, 5.5]
qualitativo = 0.5


notasAtualizadas = map(lambda x: x + qualitativo, notas)
notasAtualizadas = list(notasAtualizadas)

print(notasAtualizadas)


    



