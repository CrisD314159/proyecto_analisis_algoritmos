"""
Router for word counting an co word network results
"""

from fastapi import APIRouter, HTTPException
from reader_resources.reader_implementation import ReaderImplementation
# Ensure this is a function in statistics.py
from services.word_counting.word_counting import execute_wordcounting


router = APIRouter()


@router.get("/")
def get_statistics():
    """
    Returns results for co-word network
    """
    try:
        reader = ReaderImplementation()
        abstracts = reader.read_bib_files()
        rutas = execute_wordcounting(abstracts)

        # Retornar las rutas de los archivos, por ejemplo:
        return {
            "word_counting_results": list(rutas.values())
        }

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
