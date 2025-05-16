"""
Router for word counting an co word network results
"""
import os
from fastapi import APIRouter, HTTPException
from reader_resources.reader_implementation import ReaderImplementation
# Ensure this is a function in statistics.py
from services.word_counting.word_counting import execute_wordcounting
from utils.utils import Utils


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
        resultados = {}

        for key, path in rutas.items():
            if isinstance(path, str) and os.path.exists(path):
                resultados[key] = {
                    "name": key,
                    "image": Utils.image_to_base64(path)
                }

        # Retornar las rutas de los archivos, por ejemplo:
        return {"response": list(resultados.values())}

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
