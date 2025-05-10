"""
This module generates statistics from the scrapped articles

Top 15 authors

Year distribution

Top 15 journal

Top 15 publisher

"""

import os
import ast
import pandas as pd
import matplotlib.pyplot as plt


def generate_statistics(articles):
    """
    Generates statistics for the scrapped articles
    """
    project_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))

    # Create the path to the output_files directory
    research_files_dir = os.path.join(project_dir, "statisticsFiles")

    os.makedirs(research_files_dir, exist_ok=True)

    # Cargar artículos como DataFrame
    df = pd.DataFrame(articles)

    # Convertir autores de string a lista
    df['authors'] = df['authors'].apply(safe_parse_authors)
    df['first_author'] = df['authors'].apply(
        lambda x: x[0] if isinstance(x, list) and x else None)

    # Asegurar año como número
    if 'year' in df.columns:
        df['year'] = pd.to_numeric(df['year'], errors='coerce')

        # ------------------------
        # 1. Top 15 autores
        # ------------------------
    top_authors = df['first_author'].value_counts().head(15)
    top_authors.to_csv(f"{research_files_dir}/top_15_autores.csv")
    top_authors.plot(kind="bar", title="Top 15 Autores (Primer autor)")
    plt.ylabel("Cantidad de productos")
    plt.tight_layout()
    plt.savefig(f"{research_files_dir}/top_15_autores.png")
    plt.clf()

    # ------------------------
    # 2. Año de publicación por tipo de producto
    # ------------------------
    year_by_type = df.groupby(
        ['ENTRYTYPE', 'year']).size().unstack(fill_value=0)
    year_by_type.to_csv(
        f"{research_files_dir}/publicaciones_por_ano_y_tipo.csv")
    year_by_type.T.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.title("Publicaciones por Año y Tipo de Producto")
    plt.xlabel("Año")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(f"{research_files_dir}/publicaciones_por_ano_y_tipo.png")
    plt.clf()

    # ------------------------
    # 3. Cantidad total por tipo de producto
    # ------------------------
    type_counts = df['ENTRYTYPE'].value_counts()
    type_counts.to_csv(f"{research_files_dir}/cantidad_por_tipo.csv")
    type_counts.plot(
        kind="bar", title="Cantidad por Tipo de Producto", color="skyblue")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(f"{research_files_dir}/cantidad_por_tipo.png")
    plt.clf()

    # ------------------------
    # 4. Top 15 journals
    # ------------------------
    if 'journal' in df.columns:
        top_journals = df['journal'].value_counts().head(15)
        top_journals.to_csv(f"{research_files_dir}/top_15_journals.csv")
        top_journals.plot(
            kind="bar", title="Top 15 Journals", color="green")
        plt.ylabel("Cantidad")
        plt.tight_layout()
        plt.savefig(f"{research_files_dir}/top_15_journals.png")
        plt.clf()

        # ------------------------
        # 5. Top 15 publishers
        # ------------------------
    if 'publisher' in df.columns:
        top_publishers = df['publisher'].value_counts().head(15)
        top_publishers.to_csv(f"{research_files_dir}/top_15_publishers.csv")
        top_publishers.plot(
            kind="bar", title="Top 15 Publishers", color="orange")
        plt.ylabel("Cantidad")
        plt.tight_layout()
        plt.savefig(f"{research_files_dir}/top_15_publishers.png")
        plt.clf()

    print(f"Estadísticas exportadas en la carpeta '{research_files_dir}'")


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
