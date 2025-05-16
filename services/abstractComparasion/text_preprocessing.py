"""
This module uses nltk to preprocess abstrac content
"""
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
stemmer = PorterStemmer()


class TextPreprocessing:
    """
    This class includes all the required methods to preproccess abstracts text
    """

    def __init__(self):
        self.preprocessed_abstracts = {}
        self.ensure_nltk_resources()

    def ensure_nltk_resources(self):
        """
        Verifies and downloads necessary NLTK resources if missing.
        """
        resources = ['stopwords', 'punkt', 'punkt_tab']
        for resource in resources:
            try:
                nltk.data.find(
                    f'corpora/{resource}') if resource == 'stopwords' else nltk.data.find(f'tokenizers/{resource}')
            except LookupError:
                print(f"Downloading NLTK resource: {resource}...")
                nltk.download(resource)

    def preprocess_text(self, text, title):
        """
          Preprocess all the texto from the abstracts
        """
        lowercase = self.lowercase_text(text)

        no_numbers = self.remove_numbers(lowercase)

        no_punctuation = self.remove_punctuation(no_numbers)

        no_white_spaces = self.remove_whitespace(no_punctuation)

        no_stopwords = self.remove_stopwords(no_white_spaces)

        stemmed = self.stem_words(no_stopwords)
        self.preprocessed_abstracts[title] = stemmed

    def lowercase_text(self, text):
        """Turns the provided texto to lower case"""
        return text.lower()

    def remove_numbers(self, text):
        """Removes the numbers from the provided text"""
        result = re.sub(r'\d+', '', text)
        return result

    def remove_punctuation(self, text):
        """Removes punctuation or specia chars from the provided text"""
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

    def remove_whitespace(self, text):
        """Removes whitespaces"""
        return " ".join(text.split())

    def remove_stopwords(self, text):
        """Removes conectors an irrelevant words"""
        stop_words = set(stopwords.words("english"))
        word_tokens = word_tokenize(text)
        filtered_words = [
            word for word in word_tokens if word not in stop_words]

        filtered_text = ' '.join(filtered_words)
        return filtered_text

    def stem_words(self, text):
        """Stemming for text processing"""
        word_tokens = word_tokenize(text)
        stems = [stemmer.stem(word) for word in word_tokens]
        stems_string = ' '.join(stems)
        return stems_string
