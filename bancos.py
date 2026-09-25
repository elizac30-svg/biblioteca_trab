import sqlite3
conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db") 

def tab_autores():

    conn.execute("CREATE TABLE IF NOT EXISTS autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def tab_editoras():

    conn.execute("CREATE TABLE IF NOT EXISTS editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def tab_usuarios():

    conn.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def tab_livros():

    conn.execute("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL," \
             "edicao INTEGER NOT NULL, disponivel BOOLEAN, ano_publicacao INTEGER, " \
             "autor_id INTEGER REFERENCES autores(id), " \
             "editora_id INTEGER REFERENCES editoras(id))")

def tab_emprestimos():

    conn.execute("CREATE TABLE IF NOT EXISTS emprestimos(id INTEGER PRIMARY KEY AUTOINCREMENT, data_emprestimo DATE,"
                 "usuario_id INTEGER REFERENCES usuarios(id))")

def tab_emprestimos_livros():

    conn.execute("data_devolucao DATE, usuario_id INTEGER REFERENCES emprestimo(id), " \
                 "livro_id INTEGER REFERENCES livro(id) ")


tab_autores()
tab_editoras()
tab_usuarios()
tab_livros()

conn.commit()
conn.close()