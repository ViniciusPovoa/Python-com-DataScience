
#Exercício 1 | Achando o maior e o menor valor em uma lista

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

#Tamanho da lista
listaTam = len(lista)
print(listaTam)


#Maior e menor valor
if len(lista) > 0:
    # Inicializando as variáveis como primeiro elemento da lista
    maior = lista[0]
    menor = lista[0]

    # Percorra a lista para encontrar o maior e o menor valor
    #Número assume cada valor da lista
    for numero in lista:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    # Imprima os resultados fora do loop
    print("Maior valor:", maior)
    print("Menor valor:", menor)
else:
    print("A lista está vazia.")

#Exercício 2 | Ache os múltiplos de 3 da lista

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

#Achar os múltiplos de 3

for numero in lista:
    if numero % 3 == 0:
        print(f'{numero} Eh multiplo')


#Exercício 3 | Removendo maior e menor valor de uma lista

lista = []

for i in range(1, 6):
    n1 = int(input('Digite o valor: '))
    lista.append(n1)

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
   
print("Valores digitados:", lista)
print(f'Valores a serem removidos : Menor {menor} | Maior {maior}')
lista.remove(menor)
lista.remove(maior)

print(lista)


#Exercício 4 - Listas de Listas

notasTurma = ['Vinicius', 9.0, 10.0, 5.0, 'Victor', 10.0, 7.0, 6.0]

nomes = []
notasJuntas = []

for i in range(len(notasTurma)):
    if i % 4 == 0:
        nomes.append(notasTurma[i])
    else:
        notasJuntas.append(notasTurma[i])
        
print(nomes)
print(notasJuntas)

#Criando Listas de Listas

notas = []

for i in range(0, len(notasJuntas), 3): #Pula de três em 3 na lista
    notas.append([notasJuntas [i], notasJuntas[i+1], notasJuntas[i+2]])

print(notas)






        
