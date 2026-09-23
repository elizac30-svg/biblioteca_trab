import sqlite3
conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db") #obs: tá assim pq daí cria dentro da pasta,
                                                         #e o z é pra ficar no fim e organizar.
conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def cadastrar_autor(nome):

    conn.execute("INSERT INTO autores(nome) VALUES(?)", 
                 (nome))
    
    conn.commit()
    conn.close()
