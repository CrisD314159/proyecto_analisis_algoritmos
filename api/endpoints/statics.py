"""
Router for statistics service
"""

from fastapi import APIRouter, HTTPException
from reader_resources.reader_implementation import ReaderImplementation
# Ensure this is a function in statistics.py
from services.statistics.generate_statistics import extract_statistics
from utils.utils import Utils


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
            "authors": Utils.image_to_base64(rutas["top_15_autores"]),
            "anio": Utils.image_to_base64(rutas["publicaciones_ano_tipo"]),
            "cantidad_tipo": Utils.image_to_base64(rutas["cantidad_tipo"]),
            "journals": Utils.image_to_base64(rutas["top_15_journals"])
        }

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
