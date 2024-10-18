from fastapi import FastAPI,HTTPException
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


import alumne
import db_alumne



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class tablaAlumne(BaseModel):
    NomAlumne: str
    cicle: str
    curs: str
    grup: str

class alumnes(BaseModel):    
    IdAula: int
    nomAlumne: str
    cicle: str
    curs: str
    grup:  str


@app.get("/")
def read_root():
    return {"Students API"}


@app.get("/alumne/list", response_model=List[tablaAlumne])  
def read_alumnes():
    
    pdb = db_alumne.read()

    alumnes_sch = alumne.alumnes_schema(pdb)

    return alumnes_sch

    return alumne.alumnes_schema(db_alumne.read())





