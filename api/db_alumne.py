from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT alumne.NomAlumne, alumne.cicle, alumne.curs, alumne.grup, aula.descAula FROM alumne JOIN aula ON alumne.IdAula = aula.IdAula;")
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumnes


