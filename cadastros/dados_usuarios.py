import sqlite3

def cadastrar_usuario(nome):

    conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")

    conn.execute("INSERT INTO usuarios(nome) VALUES(?)",
                 (nome,))

    conn.commit()
    conn.close()
    