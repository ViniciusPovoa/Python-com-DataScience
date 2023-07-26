#Repete o bloco quantas vezes for necessária

#While - repete quantas vezes for necessário enquanto uma condição for True

i = 0

while i <= 10:
    print(i)
    i += 1


#Exercicio 1 - Calculo de Média de 3 alunos

somaNotas = 0

i = 1
while i <= 3:
    nA = int(input("Digite a nota A do aluno: "))
    nB = int(input("Digite a nota B do aluno: "))
    somaNotas += (nA + nB)
    i += 1

mediaTotal = somaNotas / 6  # Dividindo por 6, pois temos 3 notas A e 3 notas B

print(f"Média total: {mediaTotal}")


#For - Itera sobre um conjunto de dados  || Pode ser gerado com a função Range(inicio, fim, passo)

somaNotas = 0
for i in range(1, 4):
    nA = int(input("Digite a nota A do aluno: "))
    nB = int(input("Digite a nota B do aluno: "))
    somaNotas += (nA + nB)

mediaTotal = somaNotas / 6
print(f"Média total: {mediaTotal:.2f}")


for contador in range(1,4):
    nota1 = float(input('digite a 1 nota:'))
    nota2 = float(input('digite a 2 nota:'))
    print(f'Média: {(nota1 + nota2) / 2}')

#Exercicio Básico For e Break

for i in range(1,6):
    if i == 4:
        break
    print(i)


#Exercício1 | Colônia - A ultrapassar B, onde A tem taxa de crescimento de 3% e B 1.5%. A inicia com 4 elementos e B com 10 elementos.

txcrescA = 0.03
txcrescB = 0.015
dias = 0

a = 4
b = 10

while a < b:
    a = a + (a*txcrescA)
    b = b + (b*txcrescB)
    dias += 1
print(f"Levará {dias} dias para a colônia de bactéria A ultrapassar ou igualar a colônia de bactéria B")


#Exercício2 | Leia um conjunto de temperaturas Celsius e faça a média delas, se ler valor -273graus, deve ser finalizado (break).

tempA = int(input('Digite a temperatura A: '))
tempB = int(input('Digite a temperatura B: '))

if tempA == -273 or tempB == -273:
    print('Valores incorretos. -273 é a temperatura mais baixa possível.')
    exit()

mediaTemp = (tempA + tempB) / 2

if mediaTemp < -273:
    print('Média inválida. Verifique as temperaturas digitadas.')
else:
    print('Média das temperaturas:', mediaTemp)



#Exercicio 3 | Fatorial de números inteiros

fat = 1
n = 5
for i in range(1, n + 1):
    fat = fat * i

print(fat)

#com recursao
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
print(fatorial(5))


#Exercicio 4 | Tabuada de números inteiros de acordo com o número fornecido pela pessoa

n = int(input('Digite o valor para calcular a tabuada'))
contador = 0
resultado = 0
numeros = 0

for contador in range (1, 11):
    numeros += 1
    resultado = n * contador
    print(f"O resultado de {n} * {contador} é: {resultado}")


#Exercicio 5 | Peça um número inteiro, se ele for primo, printa que ele é primo

n = int(input('Digite o numero: '))
divInt = n % n #resto da divisao
countDiv = 0

for divisor in range(1, n + 1): #faz duas verificaçoes
    if n % divisor == 0: #se o resto for == 0
        countDiv += 1    #incrementa em countDiv 

if countDiv == 2:
    print('Eh um numero primo') 
else:
    print('Nao eh primo')
