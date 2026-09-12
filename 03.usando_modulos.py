from bibiotecas.bibiotecas import *
from minhas_funcoes.funcoes import *

nome_inserido = input("Digite seu nome: ")
ola(nome_inserido)

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

resul_soma = somar(n1, n2)

print(f"a soma de {n1} + {n2} é {resul_soma}.")

somar(n1, n2)
