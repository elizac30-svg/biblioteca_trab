from listas import (lista_usuarios, lista_autores, lista_editoras, 
lista_livros, lista_emprestimos, lista_emprestimo_livros)
from cadastros.dados_usuarios import cadastrar_usuario
from cadastros.dados_autores import cadastrar_autor
from cadastros.dados_editoras import  cadastrar_editora
from cadastros.dados_livros import cadastrar_livro
from cadastros.dados_emprestimos import cadastrar_emprestimo
from cadastros.dados_emprestimos_livros import cadastrar_emprestimo_livro

import sqlite3

def menu():
    while(True):
        print("\n---- M E N U Z I N H O  de  O P Ç Õ E S  ! ! ! ----") 
        print("\n[1] - Opções de listas.")
        print("[2] - Opções de cadastro.")
        print("[3] - Sair.")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            while True:

                print("\n--MENU DAS LISTAS--")
                print("[1] - Listar Autores.")
                print("[2] - Listar Editoras.")
                print("[3] - Listar Usuários.")
                print("[4] - Listar Livros.")
                print("[5] - Listar Emprestimos.")
                print("[6] - Listar Livros dos Emprestimos.")
                print('[7] - Voltar para o Menu Inicial.')

                opcao_l = input("Digite a opção desejada: ")
            
                if opcao_l == '1':
                    lista_autores()
                elif opcao_l == '2': 
                    lista_editoras()
                elif opcao_l == '3':
                    lista_usuarios()
                elif opcao_l == '4':
                    lista_livros()
                elif opcao_l == '5':
                    lista_emprestimos()
                elif opcao_l == '6':
                    lista_emprestimo_livros()
                elif opcao_l == '7':
                    break
                else: 
                    print("\n[Opção Inválida]")

        elif opcao == '2':
            while True:

                print("\n---MENU DOS CADASTROS---")
                print("[1] - Cadastrar Autores.")
                print("[2] - Cadastrar Editoras.")
                print("[3] - Cadastrar Usuários.")
                print("[4] - Cadastrar Livros.")
                print("[5] - Cadastrar Empréstimos.")
                print("[6] - Cadastrar Livros dos Empréstimos.")
                print('[7] - Voltar para o Menu Inicial.')

                opcao_c = input("Digite a opção desejada: ")

                if opcao_c == '1':
                    nome = input("\nInsira o nome do Autor: ")
                    cadastrar_autor(nome)
                    print("\nAutor Cadastrado com Sucesso!")

                elif opcao_c == '2':
                    nome = input("\nInsira o nome da Editora: ")
                    cadastrar_editora(nome)
                    print("\nEditora Cadastrada com Sucesso!")

                elif opcao_c == '3':
                    nome = input("\nInsira o nome do Usuário: ")
                    cadastrar_usuario(nome)
                    print("\nUsuário Cadastrado com Sucesso!")

                elif opcao_c == '4':
                    titulo = input("\nInsira o Título do Livro: ")
                    edicao = int(input("Insira qual a Edição do Livro: "))
                    ano_publicacao = int(input("Insira o Ano de Publicação: "))
                    editora_id = input("Insira o Nome da Editora desejada: ")
                    autor_id = input("Insira o Nome do Autor desejado: ")
                    if cadastrar_livro(titulo, edicao, ano_publicacao, editora_id, autor_id):
                            print("\nLivro Cadastrado com Sucesso!")

                elif opcao_c == '5':
                    usuario_id = input("\nInsira o Usuário desejado: ")
                    if cadastrar_emprestimo(usuario_id):
                        print("\nEmpréstimo Cadastrado com Sucesso!")

                elif opcao_c == '6':
                    emprestimo_id = int(input("\nInsira o 'Id' do Empréstimo Desejado: "))
                    while True:
                        livro_id = input("Insira o Título do Livro Desejado: ")

                        if cadastrar_emprestimo_livro(emprestimo_id, livro_id):
                            print("\nLivro Adicionado ao Emprestimo com Sucesso!")

                        outro = input("\nDeseja adicionar outro livro? (s/n)\n")

                        if outro.lower() != 's':
                            break

                elif opcao_c == '7':
                    break

                else:
                    print("\n[Opção Inválida]")

        elif opcao == '3':
            break

            #easter eggs abaixo:

        elif opcao == '666':
            print("\nParabéns, você acaba de invocar Samara! (nossa amiga apelidada de capeta)")

        elif opcao == '67':
            print("\n Para seu diagnóstico e breve internação: CAPS (Centro de Atenção" \
            "Psicossocial): Unidades especializadas em saúde mental. Você pode buscar atendimento" \
            "diretamente na unidade mais próxima da sua casa (saiba que não é necessário um agendamento" \
            "prévio para o primeiro atendimento).")

        else:
            print("\n[Opção Inválida]")

menu()