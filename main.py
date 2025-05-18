"""
  Main module of the project
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import statics
from api.endpoints import abstracts_comparasion
from api.endpoints import algorithms
from api.endpoints import word_counting
from api.endpoints import filtering_results


app = FastAPI(title="Proyecto Final Análisis de algoritmos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    algorithms.router, prefix="/algorithmsExecution",
    tags=["Algorithms execution (Requirement 1)"])

app.include_router(
    statics.router, prefix="/articlesStatistics",
    tags=["Statistics (Requirement 2)"])

app.include_router(
    word_counting.router, prefix="/wordCounting",
    tags=["Co-word netword and wordclouds  (Requirement 3)"])

app.include_router(
    abstracts_comparasion.router, prefix="/abstractComparasion",
    tags=["Abstracts Comparasion (Requirement 5)"])

app.include_router(
    filtering_results.router, prefix="/filteringResults",
    tags=["Filtering results"])
