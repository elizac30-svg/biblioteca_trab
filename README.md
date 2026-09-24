# biblioteca_trab

*Alunas:* Eliza Cancelier Fragnani.  
          Analuz Ramos Barros.

Implementação do exemplo clássico da Biblioteca salvando os dados em um banco de dados sqlite.

As tabelas do projeto são:

*usuarios*(id, nome)
*autores*(id, nome)
*editoras*(id, nome)
*livros*(id, titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)
*emprestimos*(id, data, usuario_id)
*emprestimos_livros*(emprestimo_id, livro_id, data_devolucao)

Em dupla, implemente a aplicação com menu de opções de cadastro e listagem para cada tabela do modelo.

