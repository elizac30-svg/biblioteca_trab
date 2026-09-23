import sqlite3

def cadastrar_editoras(nome):

    conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")

    conn.execute("INSERT INTO editoras(nome) VALUES(?)",
                 (nome,))

    conn.commit()
    conn.close()
    