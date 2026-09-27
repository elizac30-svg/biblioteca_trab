def lista_usuarios():

    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    resultados = cursor.fetchall()

    if not resultados:
        print("\n[LISTA VAZIA]")

    else:
        for linha in resultados:
            print(f"\nid: {linha['id']} | nome: {linha['nome']}")

    conn.close()

def lista_autores():

    import sqlite3 as sqlite

    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")

    resultados = cursor.fetchall()

    if not resultados:
        print("\n[LISTA VAZIA]")

    else:
        for linha in resultados:
            print(f"\nid: {linha['id']} | nome: {linha['nome']}")

    conn.close()

def lista_editoras():

    import sqlite3 as sqlite
    
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM editoras")
    
    resultados = cursor.fetchall()
    
    if not resultados:
        print("\n[LISTA VAZIA]")
    
    else:
        for linha in resultados:
            print(f"\nid: {linha['id']} | nome: {linha['nome']}")
    
    conn.close()

def lista_livros():

    import sqlite3 as sqlite
        
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
        
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT livros.id, livros.titulo, livros.edicao, livros.disponivel,
               livros.ano_publicacao, 

               editoras.nome AS editora, autores.nome AS autor
        FROM livros
        JOIN editoras ON livros.editora_id = editoras.id
        JOIN autores ON livros.autor_id = autores.id
    """)
    resultados = cursor.fetchall()
        
    if not resultados:
        print("\n[LISTA VAZIA]")
        
    else:
        for linha in resultados:
            print(f"\nid: {linha['id']} | titulo: {linha['titulo']} | edicao: {linha['edicao']} " \
                  f" | disponivel: {linha['disponivel']} | ano_publicacao: {linha['ano_publicacao']} "
                  f"| \neditora: {linha['editora']} | autor: {linha['autor']}")
        
    conn.close()

def lista_emprestimos():

    import sqlite3 as sqlite
        
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
        
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT emprestimos.id, emprestimos.data_emprestimo,

           usuarios.nome AS usuario
    FROM emprestimos
    JOIN usuarios ON emprestimos.usuario_id = usuarios.id
    """)
        
    resultados = cursor.fetchall()
        
    if not resultados:
        print("\n[LISTA VAZIA]")
        
    else:
        for linha in resultados:
            print(f"\nid: {linha['id']} | data_emprestimo:{linha['data_emprestimo']} "
                f"| usuario: {linha['usuario']} ")
        
    conn.close()


def lista_emprestimo_livros():

    import sqlite3 as sqlite
        
    conn = sqlite.connect("biblioteca_trab/zbiblioteca.db")
    conn.row_factory = sqlite.Row
        
    cursor = conn.cursor()
    
    cursor.execute(""" 
        SELECT emprestimos_livros.data_devolucao, 
               emprestimos_livros.emprestimo_id,
               livros.titulo AS livro
        FROM emprestimos_livros 
        JOIN livros ON emprestimos_livros.livro_id = livros.id
    """) 
        
    resultados = cursor.fetchall()
        
    if not resultados:
        print("\n[LISTA VAZIA]")
        
    else:
        for linha in resultados:
            print(f"\ndata_devolucao: {linha['data_devolucao']} | emprestimo_id:{linha['emprestimo_id']} "
                f"| livro: {linha['livro']} ")
        
    conn.close()

#CABEI A LISTAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ( Candelabro )