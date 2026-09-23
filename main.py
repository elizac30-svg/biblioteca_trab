from listas import lista_usuarios
from cadastros.dados_usuarios import cadastrar_usuarios

resposta = input("testeeeee")

if resposta == '1':
    lista_usuarios ()

elif resposta == '2':
            nome = input("Nome do cliente: ")
            cadastrar_usuarios(nome)

else:
    print("\n[Opção Inválida]")

