import sqlite3
conn = sqlite3.connect("biblioteca_db/biblioteca.db")

conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def cadastrar_autor (nome):

    conn.execute("INSERT INTO AUTORES(nome) VALUES(?)", 
                 (nome))
    
    conn.commit ()
    conn.close ()
