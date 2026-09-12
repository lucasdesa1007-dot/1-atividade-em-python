#esse é um programa simples de criação de usuario e login em Python.

resp = input("Deseja criar um novo usuário? (s/n): ")
if resp == "n":
  print("Fim do programa.")
elif resp == "s":
 usuario_criado = usuario = input("Digite o nome do usuário: ")
 senha_criada = senha = input("Digite a senha: ")
login_caixa = {
  "usuario": usuario_criado, "senha": senha_criada
           }
resp2 = input("Deseja fazer login? (s/n): ")
if resp2 == "n":
    print("Fim do programa.")
elif resp2 == "s":
  usuario_login = input("Digite o nome do usuário: ")
  senha_login = input("Digite a senha: ")
  if usuario_login == login_caixa["usuario"] and senha_login == login_caixa["senha"]:
    print("Login realizado com sucesso!")
  else:
    print("Usuário ou senha incorretos.")
