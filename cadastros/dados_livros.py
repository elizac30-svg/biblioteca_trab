import sqlite3

def cadastrar_livros(titulo, edicao, ano_publicacao, nome_editora, nome_autor):

    conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT id FROM editoras WHERE nome = ?",
    (nome_editora,) )

    resultado = cursor.fetchone()
    if resultado is None:
            print("Empréstimo não encontrado.")
            conn.close()
            return
    editora_id = resultado['id']

    cursor.execute("SELECT id FROM autores WHERE nome = ?",
    (nome_autor,))

    resultado = cursor.fetchone()
    if resultado is None:
            print("Empréstimo não encontrado.")
            conn.close()
            return
    autor_id = resultado['id']

    conn.execute("INSERT INTO livros (titulo, edicao, ano_publicacao, "
                 "editora_id, autor_id) VALUES (?, ?, ?, ?, ?)", 
                (titulo, edicao, ano_publicacao, editora_id, autor_id))

    conn.commit()
    conn.close()