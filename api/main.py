from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel

import db_aula 
import alumne
import db_alumne



app = FastAPI()

class alumnes(BaseModel):    
    IdAula: int
    nomAlumne: str
    cicle: str
    curs: str
    grup:  str


@app.get("/")
def read_root():
    return {"Students API"}


@app.get("/alumne/list", response_model=List[dict])  
def read_alumnes():
    
    pdb = db_alumne.read()

    alumnes_sch = alumne.alumnes_schema(pdb)

    return alumnes_sch

    return alumne.alumnes_schema(db_alumne.read())


@app.get("/alumne/show/{id}", response_model=dict)
def read_alumne_id(id:int):
    alumne_data = db_alumne.read_id(id)
    if (alumne_data) is not None:
        alumne_id = alumne.alumne_schema(alumne_data)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return alumne_id



@app.post("/alumne/add")
async def create_alumnes(data: alumnes):
    IdAula = data.IdAula
    nomAlumne = data.nomAlumne
    cicle = data.cicle
    curs = data.curs
    grup = data.grup
    
    if db_aula.verificar_aula(IdAula):
        alumne_id = db_alumne.create(IdAula,nomAlumne,cicle,curs,grup)
        return {
            "msg": "Afegit correctement",
            "id film": alumne_id,
            "NomAlumne": nomAlumne
        }
    else:
        raise HTTPException(status_code=404, detail="Aula no trobada")


@app.put("/alumne/update/{id}")
def update_alumne(id: int, data: alumnes):
    IdAula = data.IdAula
    NomAlumne = data.nomAlumne
    cicle = data.cicle
    curs = data.curs
    grup = data.grup
    
   
    if db_aula.verificar_aula(IdAula):
        resultat = db_alumne.update(id, IdAula, NomAlumne, cicle, curs, grup)
        
       
        if resultat['status'] != 0:
            raise HTTPException(status_code=500, detail=resultat['message'])
    else:
        raise HTTPException(status_code=404, detail="Aula no trobada")

    return {
        "msg": f"Alumne amb ID {id} actualitzat!"
    }



@app.delete("/alumne/delete/{id}")
def delete_alumne(id:int):
    deleted_alumne = db_alumne.delete_alumne(id)
    if deleted_alumne == 0:
       raise HTTPException(status_code=404, detail="Items to delete not found") 
    return {
                "msg": f"Alumne amb ID {id} eliminat!"
            }



@app.get("/alumne/listAll")
def llegeix_alumnes_all():
    alumnes_all = db_alumne.readAll()
    return alumne.alumnes_schema_All(alumnes_all)



