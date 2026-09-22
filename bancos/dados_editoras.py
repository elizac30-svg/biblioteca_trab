import sqlite3
conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")

conn.execute("CREATE TABLE editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def cadastrar_editoras(nome):

    conn.execute("INSERT INTO editoras(nome) VALUES(?)",
                 (nome))

    conn.commit()
    conn.close()
    