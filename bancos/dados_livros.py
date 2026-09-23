import sqlite3 
conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")

#*livros*(id, titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)

conn.execute("CREATE TABLE livros (id INTEGER PRIMAY KEY AUTOINCREMENT, titulo TEXT NOT NULL," \
             "edicao INTEGER NOT NULL, disponivel BOOLEAN, ano_publicacao INTEGER" \
             "autor_id INTEGER REFERENCES autor(id) " \
             "editora_id INTEGER REFERENCES editora(id))")

def cadastrar_livros():
    # type: ignore