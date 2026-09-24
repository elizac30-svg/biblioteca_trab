def lista_usuarios():

    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    resultados = cursor.fetchall()

    if not resultados:
        print("[LISTA VAZIA]")

    else:
        for linha in resultados:
            print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close()

def lista_autores():

    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")

    resultados = cursor.fetchall()

    if not resultados:
        print("[LISTA VAZIA]")

    else:
        for linha in resultados:
            print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close()

