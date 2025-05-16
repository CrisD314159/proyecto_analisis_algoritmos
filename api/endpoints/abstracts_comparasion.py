"""
This module contains all the endpoints for the abstract comparassion
"""
from fastapi import APIRouter, HTTPException
from services.abstractComparasion.text_preprocessing import TextPreprocessing
from services.abstractComparasion.dendrogram_ploting import TextVectorization
from reader_resources.reader_implementation import ReaderImplementation
from utils.utils import Utils

router = APIRouter()


@router.get("/")
def get_abstracts_comparasion():
    """
    This method returns the results form the abstract comparasion 
    """
    try:
        reader = ReaderImplementation()
        articles = reader.read_bib_files()

        preprocessing = TextPreprocessing()
        for article in articles:
            if 'abstract' in article:
                preprocessing.preprocess_text(
                    article['abstract'], article['title'])
        preprocessed_abstracts = preprocessing.preprocessed_abstracts

        dendrogram = TextVectorization()
        results = dendrogram.transform_text(
            preprocessed_abstracts=preprocessed_abstracts)

        return {"ward": Utils.image_to_base64(results["ward_dendogram"]),
                "average": Utils.image_to_base64(results["average_dendogram"])}

    except (IOError, ValueError) as e:
        return HTTPException(status_code=500, detail=str(e))
