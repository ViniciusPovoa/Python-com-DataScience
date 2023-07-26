#Vinícius Horácio Marques Póvoa - Ex. Básico em Python

#Manipulando variáveis
idadej = 5
idade = idadej + 20
print(idade)

#String em Python
nome = 'Vinicius'
sobrenome = "Povoa"
print(nome , sobrenome)


#Função Type - Informa o tipo de variável que o python está se referenciando (muito importante em DataScience)
i = 5
type(i)

#Exercicio Básico de Média 
qSeg = 5
qDoc = 16
qDir = 1

salarioSeg = qSeg * 3000
salarioDoc = qDoc * 6000
salarioDir = qDir * 12500

totalEmpregados = qSeg + qDoc + qDir
print("O total de empregados eh", totalEmpregados)

totalSalario  = salarioSeg + salarioDoc + salarioDir
print("O total salario eh", totalSalario)

mediaSalarial = totalSalario / totalEmpregados
print("A média salarial eh", mediaSalarial)


#Diferença entre o salário mais alto e mais baixo

diferencaSalarial = salarioDir - salarioSeg
print("A diferenca salarial eh", diferencaSalarial)

#Exponencianção
exponenciacao = 2**3
print("A exponenciacao de 2^3 eh", exponenciacao)

#Módulo (%) - Acha o resto de uma divisão
restoDiv = 7%3
print("O resto da divisao de 7/3 eh", restoDiv)

#Divisão inteira - //
divInt = 7%3
print("O resto da divisão inteira eh", divInt)

#Manipulando Strings

s1 = 'Alura'
s2 = "Alura"
print("\n", type(s1),type(s2))

#Métodos - São funções que estão associadas a objetos -> obj.metodo()

texto = ' Vinicius Horacio Marques Puvua '
print(texto.upper()) #coloca tudo em maiusculo
print(texto.strip()) #tira os caracteres de espaço
print(texto.replace('\nPuvua', 'Povoa')) #substitui as palavras -> (antigo , novo)
texto = texto.strip().replace('\nPuvua', 'Povoa').upper() #atualiza o valor da variavel texto (sobrecarga de métodos)
print("\nValor atualizado: ", texto)

