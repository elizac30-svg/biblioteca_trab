'''adicionar
    if resultado is None:
        print("Empréstimo não encontrado.")
        conn.close()
        return'''

import sqlite3
from datetime import datetime

def cadastrar_emprestimos(data_emprestimo, usuario_id, nome_usuario):

    conn = sqlite3.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    data_emprestimo = datetime.now().isoformat()

    cursor.execute("SELECT id FROM usuarios WHERE nome = ?",
    (nome_usuario))

    resultado = cursor.fechone()
    usuario_id = resultado['id']

    conn.execute("INSERT INTO emprestimos(data) VALUES (?, ?)",
                 (data_emprestimo, usuario_id))

    conn.commit()
    conn.close