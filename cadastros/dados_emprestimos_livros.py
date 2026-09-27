import sqlite3
from datetime import datetime, timedelta

def cadastrar_emprestimo_livro(emprestimo_id, data_emprestimo, titulo_livro):

    conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    data_devolucao = data_emprestimo + timedelta(days= 30) #assim a data de devolução fica automaticamente 
                                                           #para 30 dias depois da data de emprestimo

    cursor.execute("SELECT id FROM emprestimos WHERE id = ?",
    (emprestimo_id,))
    
    resultado = cursor.fetchone()
    if resultado is None:
        print("\n[Empréstimo não encontrado.]")
        conn.close()
        return False
    emprestimo_id = resultado['id']

    cursor.execute("SELECT id FROM livros WHERE titulo = ?",
    (titulo_livro,))

    resultado = cursor.fetchone()
    if resultado is None:
            print("\n[Empréstimo não encontrado.]")
            conn.close()
            return False
    livro_id = resultado['id']

    conn.execute("INSERT INTO emprestimos_livros(emprestimo_id, livro_id, data_devolucao) " \
                 "VALUES (?, ?, ?)",
                 (emprestimo_id, livro_id, data_devolucao))

    conn.execute("UPDATE livros SET disponivel = False WHERE id = ?", (livro_id,) )

    conn.commit()
    conn.close()