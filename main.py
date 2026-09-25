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
        print("\n---- M E N U Z I N H O  de  O P Ç Õ E S  ! ! ! ----")
        print("\n[1] - Opções de listas.")
        print("[2] - Opções de cadastro.")
        print("[3] - Sair )")


menu()