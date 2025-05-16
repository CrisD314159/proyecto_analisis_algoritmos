"""
Router for the filtering results
"""

from fastapi import APIRouter, HTTPException
from reader_resources.reader_implementation import ReaderImplementation
# Ensure this is a function in statistics.py


router = APIRouter()


@router.get("/")
def get_filtering_results():
    """
    Returns the filtering results
    """
    try:
        reader = ReaderImplementation()
        reader.read_bib_files()
        results = reader.print_results()

        # Retornar las rutas de los archivos, por ejemplo:
        return {
            "articles":  f"{results['articles']} articles found",
            "journals":  f"{results['journals']} journals found",
            "keywords":  f"{results['keywords']} keywords found",
            "authors":  f"{results['authors']} authors found",
            "reapeated":  f"{results['reapeated']} reapeated found"
        }

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
