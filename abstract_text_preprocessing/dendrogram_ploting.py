"""
This module is used to vectorize, 
calculate matrix length, hierarchical clustering 
and dendrogram ploting
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram


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

        self.plot_dendogram(z_ward, z_average, titles)

    def plot_dendogram(self, z_ward, z_average, titles):
        """
        Method used to plot a dendrogram
        """
        # Ward dendrogram
        plt.figure(figsize=(12, 6))
        dendrogram(z_ward, labels=titles)
        plt.title("Dendrograma - Ward")
        plt.show()

        # Average dendrogram
        plt.figure(figsize=(12, 6))
        dendrogram(z_average, labels=titles)
        plt.title("Dendrograma - Average")
        plt.show()
