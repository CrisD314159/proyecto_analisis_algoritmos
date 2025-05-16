"""
This module generates statistics from the scrapped articles

Top 15 authors

Year distribution

Top 15 journal

Top 15 publisher

"""

import os
import ast
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use("Agg")


def extract_statistics(articles):
    """
    Generates statistics for the scrapped articles and returns paths to the generated files.
    """
    file_paths = {
    }

    project_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../images'))
    research_files_dir = os.path.join(project_dir, "statisticsFiles")
    os.makedirs(research_files_dir, exist_ok=True)

    df = pd.DataFrame(articles)
    df['authors'] = df['authors'].apply(safe_parse_authors)
    df['first_author'] = df['authors'].apply(
        lambda x: x[0] if isinstance(x, list) and x else None)

    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce')

    # Top 15 autores
    top_authors = df['first_author'].value_counts().head(15)
    path_img = os.path.join(research_files_dir, "top_15_autores.png")
    top_authors.plot(kind="bar", title="Top 15 Autores (Primer autor)")
    plt.ylabel("Cantidad de productos")
    plt.tight_layout()
    plt.savefig(path_img)
    plt.close()
    file_paths["top_15_autores"] = path_img

    # Año por tipo
    year_by_type = df.groupby(
        ['ENTRYTYPE', 'year']).size().unstack(fill_value=0)
    path_img = os.path.join(
        research_files_dir, "publicaciones_por_ano_y_tipo.png")
    year_by_type.T.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.title("Publicaciones por Año y Tipo de Producto")
    plt.xlabel("Año")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(path_img)
    plt.close()
    file_paths["publicaciones_ano_tipo"] = path_img

    # Cantidad total por tipo
    type_counts = df['ENTRYTYPE'].value_counts()
    path_img = os.path.join(research_files_dir, "cantidad_por_tipo.png")
    type_counts.plot(
        kind="bar", title="Cantidad por Tipo de Producto", color="skyblue")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(path_img)
    plt.close()
    file_paths["cantidad_tipo"] = path_img

    # Top journals
    if 'journal' in df.columns:
        top_journals = df['journal'].value_counts().head(15)
        path_img = os.path.join(research_files_dir, "top_15_journals.png")
        top_journals.plot(kind="bar", title="Top 15 Journals", color="green")
        plt.ylabel("Cantidad")
        plt.tight_layout()
        plt.savefig(path_img)
        plt.close()
        file_paths["top_15_journals"] = path_img

    # Top publishers
    if 'publisher' in df.columns:
        top_publishers = df['publisher'].value_counts().head(15)
        path_img = os.path.join(research_files_dir, "top_15_publishers.png")
        top_publishers.plot(
            kind="bar", title="Top 15 Publishers", color="orange")
        plt.ylabel("Cantidad")
        plt.tight_layout()
        plt.savefig(path_img)
        plt.close()
        file_paths["top_15_publishers"] = path_img

    print(f"Estadísticas exportadas en la carpeta '{research_files_dir}'")

    return file_paths


def safe_parse_authors(value):
    """
    Ensures the string value for authors 
    """
    if isinstance(value, list):
        return value
    try:
        return ast.literal_eval(value)
    except Exception:
        return []
