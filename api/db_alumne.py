import csv
import io
from client import db_client
from fastapi import UploadFile

def read(orderby: str | None = None,  contain: str | None = None, skip: int = 0, limit: int | None = None):
    try:
        conn = db_client()
        cur = conn.cursor()

        query = "SELECT alumne.NomAlumne, alumne.Cicle, alumne.Curs, alumne.Grup, aula.DescAula FROM alumne JOIN aula ON alumne.idAula = aula.idAula"
        params = []

        if contain:
            query += " WHERE alumne.NomAlumne LIKE %s"
            params.append(f"%{contain}%")

        if orderby:
            if orderby.lower() == "asc":
                query += " ORDER BY alumne.NomAlumne ASC"
            elif orderby.lower() == "desc":
                query += " ORDER BY alumne.NomAlumne DESC"

        if limit:
            query += " LIMIT %s"
            params.append(limit)
        if skip:
            query += " OFFSET %s"
            params.append(skip)

        cur.execute(query, tuple(params))
        alumnes = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"{e}"}
    
    finally:
        if cur: cur.close()
        if conn: conn.close()
    
    return alumnes




def alumnesCSV(file: UploadFile):
    try:
        contents = file.file.read()
        csv_reader = csv.reader(io.StringIO(contents.decode("utf-8")), delimiter=',')
        
        next(csv_reader)

        conn = db_client()
        cur = conn.cursor()

        for row in csv_reader:
            descAula, edifici, pis, nomAlumne, cicle, curs, grup = row

            cur.execute("SELECT idAula FROM Aula WHERE DescAula = %s", (descAula,))
            
            aula = cur.fetchone()
            
            if not aula:
                cur.execute("""
                    INSERT INTO Aula (DescAula, Edifici, Pis, createdAt, updatedAt)
                    VALUES (%s, %s, %s, NOW(), NOW())
                """, (descAula, edifici, pis))
                conn.commit()
                cur.execute("SELECT idAula FROM Aula WHERE DescAula = %s", (descAula,))
                aula = cur.fetchone()

            idAula = aula[0]

            cur.execute("""
                SELECT * FROM Alumne WHERE NomAlumne = %s AND Cicle = %s AND Curs = %s AND Grup = %s
            """, (nomAlumne, cicle, curs, grup))
            alumne = cur.fetchone()

            if not alumne:
                cur.execute("""
                    INSERT INTO Alumne (NomAlumne, Cicle, Curs, Grup, idAula, createdAt, updatedAt)
                    VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
                """, (nomAlumne, cicle, curs, grup, idAula))
                conn.commit()

        return {"message": "Càrrega realitzada correctament"}
    
    except Exception as e:
        return {"status": -1, "message": f"Error en la càrrega: {e}"}
    
    finally:
        if cur: cur.close()
        if conn: conn.close()


