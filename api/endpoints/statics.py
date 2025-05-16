"""
Router for statistics service
"""

from fastapi import APIRouter, HTTPException
from reader_resources.reader_implementation import ReaderImplementation
# Ensure this is a function in statistics.py
from services.statistics.generate_statistics import extract_statistics


router = APIRouter()


@router.get("/")
def get_statistics():
    """
    Returns statistics for research articles
    """
    try:
        reader = ReaderImplementation()
        abstracts = reader.read_bib_files()
        rutas = extract_statistics(abstracts)

        # Retornar las rutas de los archivos, por ejemplo:
        return {
            "imagenes": list(rutas.values())
        }

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
