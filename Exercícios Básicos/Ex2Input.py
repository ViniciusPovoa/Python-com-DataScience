#Coleta de Dados - Input

anoEntrada = input('\nEscreva o ano de ingresso do estudante') #le o anoentrada como str
print('Ano de entrada {anoEntrada}')

anoEntrada = int(input('\nEscreva o ano de ingresso do estudante')) #força o tipo a ser int
print('Ano de entrada {anoEntrada}')

#Exercicio1 - Solicita 3 números, soma e printa eles

a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))
soma = a + b + c
print(soma)

#Exercicio2 - Solicita 2 números, e divide eles. Dominador não pode ser = 0
try:
    a = input("Digite o valor de A: ")
    b = input("Digite o valor de B: ")

    if not a.isnumeric() or not b.isnumeric():
        print("Digite apenas valores numéricos.")
    else:
        a = int(a)
        b = int(b)

        if b == 0: 
            print("O denominador não pode ser zero")
        else:
            divInt = a / b
            print("A divisão é:", divInt)

except ValueError:
    print("Digite apenas valores numéricos.")

#Ex.if
if 2 < 7:
    print('Condicao verdadeira')
else:
    print('Condicao falsa')   

#Média de Aprovação
novaMedia= int(input("Digite o valor da media"))

if novaMedia > 6:
    print('Aprovado')
else:
    print('Reprovado')    

if 4 <= novaMedia <= 6:
    print("Pode fazer a recuperação.")


#Elif - União da estrutura do Else + If -> Mesmo que Else if
if novaMedia > 6:
    print('Aprovado')
elif 4 <= novaMedia <= 6:
    print("Pode fazer a recuperação.")
else:
    print('Reprovado')   