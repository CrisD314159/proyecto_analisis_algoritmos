"""
This module contains all the results related to sorting algoruthms execution
"""
from fastapi import APIRouter, HTTPException
from reader_resources.reader_implementation import ReaderImplementation
from utils.utils import Utils

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
            "title": Utils.image_to_base64(rutas["title_bar_plotting"]),
            "author": Utils.image_to_base64(rutas["author_bar_plotting"]),
            "journal": Utils.image_to_base64(rutas["journal_bar_plotting"]),
            "keywords": Utils.image_to_base64(rutas["keywords_bar_plotting"])
        }

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
