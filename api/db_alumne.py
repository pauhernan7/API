from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from alumne")
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumnes


def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from alumne where IdAlumne = %s"
        cur.execute(query, (id,))
       
        alumnes = cur.fetchone()

    
    except Exception as e:
        print("ERROR", e)
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        cur.close()
        conn.close()
        
    
    return alumnes


def create(IdAula,NomAlumne,Cicle,Curs,Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into alumne (IdAula,NomAlumne,Cicle,Curs,Grup) VALUES (%s,%s,%s,%s,%s);"
        values=(IdAula,NomAlumne,Cicle,Curs,Grup)
        cur.execute(query,values)
    
        conn.commit()
        alumne_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return alumne_id



def update(IdAlumne, IdAula, NomAlumne, cicle, curs, grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """UPDATE alumne 
                   SET IdAula = %s, NomAlumne = %s, cicle = %s, curs = %s, grup = %s 
                   WHERE IdAlumne = %s;"""
        values = (IdAula, NomAlumne, cicle, curs, grup, IdAlumne)
        cur.execute(query, values)
        conn.commit()
        affected_rows = cur.rowcount
        
        if affected_rows == 0:
            return {"status": -1, "message": "No s'ha trobat l'alumne amb aquest ID"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
    finally:
        conn.close()

    return {"status": 0, "message": "Actualización exitosa", "affected_rows": affected_rows}


def delete_alumne(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM alumne WHERE IdAlumne = %s;"
        cur.execute(query,(id,))
        deleted_recs = cur.rowcount
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    return deleted_recs




def readAll():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM alumne, aula where alumne.IdAula = aula.IdAula"
        cur.execute(query)
    
        alumnes_id = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"{e}"}
    
    finally:
        if cur: cur.close()
        if conn: conn.close()
    
    return alumnes_id