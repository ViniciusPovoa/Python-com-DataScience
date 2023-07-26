#Operandos Lógicos - and, or, not
t1 = t2 = True
f1 = f2 = False

#And - Só é verdade se os dois forem verdadeiro
print("And")
if t1 and t2:
    print("Expressao verdadeira")
else: 
    print("Expressao falsa")

#Or - É verdade quando um ou outro é verdadeiro
print("Or")
if f1 or f2:
    print('Expressao verdadeira')
else:
    print('Expressao falsa')
    
#Not - Nega tudo
print("Not")
if not f2:
    print('Expressao verdadeira')
else:
    print('Expressao falsa')
    
#In - Verifica se um determinado elemento está contido em um conjunto de elementos | Ex: Palavra dentro de um texto
lista = 'Jose, Vinicius, Horacio, Victor, Bruno, Gabriel, Lucas'
print(lista)
nome_1 = 'Vinicius'
nome_2 = 'Mariana'

if nome_2 in lista:
    print(f"{nome_2} esta na lista")
else:
    print(f"{nome_2} nao esta na lista")


#Exercicio1 - Lê 3 produtos e mostra qual deles é o mais barato para comprar

p1 = int(input("digite o preço do produto 1: "))
p2 = int(input("digite o preço do produto 2: "))
p3 = int(input("digite o preço do produto 3: "))

if p1 < p2 and p1 < p3:
    print('produto 1 é mais barato')
elif p2 < p1 and p2 < p3:
    print('produto 2 é mais barato')
elif p3 < p1 and p3 < p2:
    print('produto 3 é mais barato')
else:
    print('existem dois ou mais produtos com o mesmo preço')


#Exercicio2 - Lê 1 número e mostra se ele é par ou ímpar

n1 = int(input("digite o preço do produto 1: "))

if n1 % 2 == 0:
    print('numero par')
else:
    print('numero impar')

