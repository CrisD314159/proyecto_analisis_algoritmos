"""
This module contains all the results related to sorting algoruthms execution
"""
from fastapi import APIRouter, HTTPException
from reader_resources.reader_implementation import ReaderImplementation

router = APIRouter()


@router.get("/")
def get_algorithms():
    """
    Returns results for algorithms execution
    """
    try:
        reader = ReaderImplementation()
        reader.read_bib_files()
        rutas = reader.plot_results()

        # Retornar las rutas de los archivos, por ejemplo:
        return {
            "algorithms_results": list(rutas.values())
        }

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
