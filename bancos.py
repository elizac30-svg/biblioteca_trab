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

tab_autores()
tab_editoras()
tab_usuarios()
tab_livros()

conn.commit()
conn.close()