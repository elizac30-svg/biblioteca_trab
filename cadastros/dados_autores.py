import sqlite3

def cadastrar_autor(nome):

    conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db") #obs: tá assim pq daí cria dentro da pasta,
                                                             #e o z é pra ficar no fim e organizar.
    conn.execute("INSERT INTO autores(nome) VALUES(?)", 
                 (nome,))
    
    conn.commit()
    conn.close()
