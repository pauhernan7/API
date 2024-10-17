def alumne_schema(alumne) -> dict:
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "CreatedAt": alumne[6],
        "UpdatedAt": alumne[7]
    }
    
def alumnes_schema(alumnes) -> dict:
    return [alumne_schema(alumne) for alumne in alumnes]




def alumne_schema_All(alumne) -> dict:
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "IdAula": alumne[6],
        "DescAula": alumne[7],
        "Edifici": alumne[8],
        "Pis": alumne[9],
        
    }
    
def alumnes_schema_All(alumnes) -> list:
    return [alumne_schema(alumne) for alumne in alumnes]
