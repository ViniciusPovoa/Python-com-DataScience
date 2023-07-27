#Treinando exceções

notas = {'Vinicius': [9,10,8], 'Victor': [4, 6, 8]}

try:
    nome = input("Digite o nome do estudante para exportar as notas")
    resultado = notas[nome]
except Exception as e: #mesma coisa do catch
    print(f"Erro: estudante não matriculado na turma")

else:  #se passar do try, segue para o else normalmente
    print(resultado)
    
finally: #fluxo que roda (com ou sem exceção)
    print('A consulta foi encerrada.')


#Raise - Raise 'nomedoerro' mensagem()

def media(lista: list) -> float:
    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas")
    calculo = sum(lista) / len(lista)
    return calculo

try:
    notas = [5, 6, 7, 8]
    resultado = media(notas)
except TypeError:
    print('Não foi possível calcular a média do estudante')
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print('A consulta foi encerrada')
    
 



