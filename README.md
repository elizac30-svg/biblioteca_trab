# biblioteca_trab

*Alunas:* Eliza Cancelier Fragnani.  
          Analuz Ramos Barros.

Implementação do exemplo clássico da Biblioteca salvando os dados em um banco de dados sqlite.

As tabelas do projeto são:

*usuarios*(id, nome)
*autores*(id, nome)
*editoras*(id, nome)
*livros*(id, titulo, edicao, ano_publicacao, disponivel, editora_id, autor_id)
*emprestimos*(id, data_emprestimos, usuario_id)
*emprestimos_livros*(data_devolucao, emprestimo_id, livro_id)

Em dupla, implemente a aplicação com menu de opções de cadastro e listagem para cada tabela do modelo.

