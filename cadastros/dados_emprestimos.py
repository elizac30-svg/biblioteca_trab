import sqlite3
from datetime import datetime

def cadastrar_emprestimo(nome_usuario):

    conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    data_emprestimo = datetime.now().isoformat() #gera a data automaticamente 

    cursor.execute("SELECT id FROM usuarios WHERE nome = ?",
    (nome_usuario,))

    resultado = cursor.fetchone()
    if resultado is None:
            print("\n[Empréstimo não encontrado.]")
            conn.close()
            return False
    usuario_id = resultado['id']

    conn.execute("INSERT INTO emprestimos(data_emprestimo, usuario_id) VALUES (?, ?)",
                 (data_emprestimo, usuario_id))

    conn.commit()
    conn.close

    return True