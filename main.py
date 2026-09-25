from listas import lista_usuarios
from cadastros.dados_usuarios import cadastrar_usuarios

'''*usuarios*(id, nome)
*autores*(id, nome)
*editoras*(id, nome)
*livros*(id, titulo, edicao, ano_publicacao, disponivel, editora_id, autor_id)
*emprestimos*(id, data_emprestimos, usuario_id)
*emprestimos_livros*(data_devolucao, emprestimo_id, livro_id)'''

def menu():
    while(True):
        print("\n---- M E N U Z I N H O  de  O P Ç Õ E S  ! ! ! ----") #menu 0
        print("\n[1] - Opções de listas.")
        print("[2] - Opções de cadastro.")
        print("[3] - Sair )")

        opcao = input("Digite a opção desejada: ")
        #obs para Luz: Apenas um teste, modifique depois e faz o resto como quiser *figuriha q eu to pensando*

        if opcao == '1':
            while True:

                print("\nmenuh lá das listinha") #menu 1
                print("finge que existem opções aqui")
                opcao_l = input("responde ai: ")
            
                if opcao_l == '1':#depois de executar volta pro mennu 1 por causa do while True:
                    print("blablabla")
                elif opcao_l == '2': #isso faz voltar para o menu 0
                    break
                else: 
                    print("\ncoiso inavlido, ache uma bola de cristal para adivinhar as alternativas seu " \
                    "burro, nao tem ainda pq? eoenn")

        elif opcao == '2':
            while True:

                print("só pra falar q tem as opcoes lá")
                opcao_c = input('AAAaa?: ')
                if opcao_c == '1':
                    break
                else:
                    print("banana")

        elif opcao == '3':
            break

        elif opcao == '67':
            print("\nPara se diagnostico de problemas mentais e breve internamento: " \
            "CAPS (Centro de Atenção Psicossocial): Unidades do SUS especializadas em " \
            "saúde mental. Você pode buscar atendimento diretamente na unidade mais próxima " \
            "da sua casa (saiba que não é necessário um agendamento prévio para o primeiro acolhimento).")

        elif opcao == '666':
            print("\nParabéns! Você acaba de invocar Samara!")

        else:
            print("\nO SEU ACÉFALO DESPROVIDO DE INTELIGENCIA, SEU CORNO, ISSO NAO "
                  "TA NAS OPÇÕES, SABE LER NAO O ESTRUPICIO!!!??????")

menu()