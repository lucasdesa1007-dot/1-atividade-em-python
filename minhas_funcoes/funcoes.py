# exemplo de funçoes:

def ola(nome):
    print(f"Olá, {nome}")


def somar(n1, n2):
    resultado = (n1 + n2)
    return resultado


if __name__ == "__main__":
    nome_inserido = input("Digite seu nome: ")
    ola(nome_inserido)

    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))

    resultado_da_soma = somar(n1, n2)

    print(f"a soma de {n1} + {n2} é {resultado_da_soma}.")
