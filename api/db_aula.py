import client 

def verificar_aula(IdAula):
    conn = client.db_client()
    cur = conn.cursor()

    query = "SELECT IdAula FROM aula WHERE IdAula = %s"
    cur.execute(query, (IdAula,))
    
    if cur.fetchone() is None:
        return False
    else:
        return True