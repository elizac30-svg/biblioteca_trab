import sqlite3 
conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")

conn.execute("CREATE TABLE livros (id INTEGER PRIMAY KEY AUTOINCREMENT, )")