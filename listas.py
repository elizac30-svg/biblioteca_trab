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

def lista_editoras():

    import sqlite3 as sqlite
    
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM editoras")
    
    resultados = cursor.fetchall()
    
    if not resultados:
        print("[LISTA VAZIA]")
    
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | nome: {linha['nome']}")
    
    conn.close()

def lista_livros():

    import sqlite3 as sqlite
        
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
        
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM livros")
        
    resultados = cursor.fetchall()
        
    if not resultados:
        print("[LISTA VAZIA]")
        
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | titulo: {linha['titulo']} | edicao: {linha['edicao']} " \
                  f" | disponivel: {linha['disponivel']} | ano_publicacao {linha['ano_publicacao']} "
                  f"| editora_id{linha['editora_id']} | autor_id{linha['autor_id']}")
        
    conn.close()

def emprestimo():

    import sqlite3 as sqlite
        
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
        
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM emprestimo")
        
    resultados = cursor.fetchall()
        
    if not resultados:
        print("[LISTA VAZIA]")
        
    else:
        for linha in resultados:
            print(f"id: {linha['id']} | data_emprestimos:{linha['data_emprestimos']} "
                f"| usuario_id: {linha['usuario_id']} ")
        
    conn.close()


def emprestimo_livros():

    import sqlite3 as sqlite
        
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
        
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM emprestimo")
        
    resultados = cursor.fetchall()
        
    if not resultados:
        print("[LISTA VAZIA]")
        
    else:
        for linha in resultados:
            print(f"data_devolucao: {linha['data_devolucao']} | emprestimo_id:{linha['emprestimo_id']} "
                f"| livro_id: {linha['livro_id']} ")
        
    conn.close()

#CABEI A LISTAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ( Candelabro )