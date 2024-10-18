def alumne_schema(fetchAlumne) -> dict:
    return {
        "NomAlumne": fetchAlumne[0],
        "cicle": fetchAlumne[1],
        "curs": fetchAlumne[2],
        "grup": fetchAlumne[3],
        "descAula": fetchAlumne[4]
    }

    
def alumnes_schema(fetchAlumnes) -> dict:
    return [alumne_schema(fetchAlumne) for fetchAlumne in fetchAlumnes]




