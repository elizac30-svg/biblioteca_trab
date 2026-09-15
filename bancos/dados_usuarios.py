import sqlite3
conn = sqlite3.connect("biblioteca_db/biblioteca.db")

conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def cadastrar_usuarios(nome):

    conn.execute("INSERT INTO usuarios(nome) VALUES(?)",
                (nome) )

    conn.commit()
    conn.close ()