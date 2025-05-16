"""
This module is used to vectorize, 
calculate matrix length, hierarchical clustering 
and dendrogram ploting
"""
import os
from scipy.cluster.hierarchy import dendrogram
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")


class TextVectorization:
    """
    Class used to vectorize, 
    calculate matrix length and hierarchical clustering
    """

    def __init__(self):
        pass

    def transform_text(self, preprocessed_abstracts):
        """
        Method used to vectorize, calculate matrix length, hierarchical clustering 
        """
        texts = list(preprocessed_abstracts.values())

        titles = list(preprocessed_abstracts.keys())

        vectorizer = TfidfVectorizer()

        x = vectorizer.fit_transform(texts)

        distances = pdist(x.toarray(), metric='euclidean')

        z_ward = linkage(distances, method='ward')

        z_average = linkage(distances, method='average')

        return self.plot_dendogram(z_ward, z_average, titles)

    def plot_dendogram(self, z_ward, z_average, titles):
        """
        Method used to plot a dendrogram
        """
        results = {
        }

        project_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../../images'))
        research_files_dir = os.path.join(project_dir, "abstracts_dendograms")
        os.makedirs(research_files_dir, exist_ok=True)

        # Ward dendrogram
        file_path = os.path.join(research_files_dir, "ward_dendogram.png")
        plt.figure(figsize=(12, 6))
        dendrogram(z_ward, labels=titles)
        plt.title("Dendrograma - Ward")
        plt.savefig(file_path)
        plt.close()
        results["ward_dendogram"] = file_path

        # Average dendrogram
        file_path = os.path.join(
            research_files_dir, "average_dendogram.png")
        plt.figure(figsize=(12, 6))
        dendrogram(z_average, labels=titles)
        plt.title("Dendrograma - Average")
        plt.savefig(file_path)
        plt.close()
        results["average_dendogram"] = file_path

        return results
