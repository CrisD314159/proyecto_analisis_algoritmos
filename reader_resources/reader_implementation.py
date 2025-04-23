"""
  This module uses python bibtexparser for the bib files handle
"""

import os
import glob
import re
import uuid
import bibtexparser as bib
from reader_resources.algorithms_execution import AlgorithmsExecution
from reader_resources.create_output_files import OutputFiles
from reader_resources.abstract_processing import AbstractProcessing


class ReaderImplementation:
    """
      This class is in charge of reading the bib files
    """

    def __init__(self):
        self.bib_files = []
        self.titles = []
        self.authors = []
        self.journals = []
        self.keywords = []
        self.articles = []
        self.abstracts_words = []
        self.repeated_articles = []

    def list_bib_files(self, directory='researchFiles'):
        """
        Lists all .bib files in the specified directory

        Args:
            directory (str): The directory to search in, default is 'researchFiles'

        Returns:
            list: A list of paths to .bib files
        """
        # Get the absolute path of the project directory
        project_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..'))

        # Create the path to the researchFiles directory
        research_files_dir = os.path.join(project_dir, directory)

        # Check if directory exists
        if not os.path.isdir(research_files_dir):
            raise FileNotFoundError(
                f"Directory {research_files_dir} not found")

        # Find all .bib files in the directory
        bib_file_paths = glob.glob(os.path.join(research_files_dir, '*.bib'))
        self.bib_files = bib_file_paths

    def read_bib_files(self):
        """
        Reads each of the bib files indentified in the list_bib_files method
        """
        self.list_bib_files()

        for file in self.bib_files:

            with open(file, encoding='utf-8') as bib_file:
                library = bib.load(bib_file)
            file_entries = library.entries

            for entry in file_entries:
                # One entry equals one article
                # Separates and filters every entry from the article
                self.separate_entry_keys(entry)

        # PLOT AND OUTPUT FILE GENERATION
        # self.print_results()    # Prints the filter results
        # self.generate_output_files()  # Generates the output files
        # self.plot_results()     # Generates a bar graph for the execution results
        self.process_abstracts()

    def separate_entry_keys(self, entry):
        """
        Separates the key of a bib entry
        """
        try:

            # Creates an entire new filteren article
            article = {
                "ENTRYTYPE": "Filtered Article",
                "ID": str(uuid.uuid4())
            }

            # Extract authors if present
            if 'author' in entry:
                # Split authors by 'and' and strip whitespace
                authors = [author.strip()
                           for author in re.split(' and |,', entry['author'])]
                article['authors'] = str(authors)
                self.inject_authors(authors)  # Injected to plotter

            if 'title' in entry:
                title = entry['title']
                article['title'] = title
                self.inject_titles(title)

            if 'journal' in entry or 'publisher' in entry:
                journal = entry['journal'] if 'journal' in entry else entry['publisher']
                article['journal'] = journal
                self.inject_journals(journal)  # Injected to plotter

            if 'keywords' in entry:
                keywords = [keyword.strip()
                            for keyword in re.split(',', entry['keywords'])]
                article['keywords'] = str(keywords)
                self.inject_keywords(keywords)  # Injected to plotter

            if 'year' in entry:
                year = entry['year']
                article['year'] = year

            if 'abstract' in entry:
                abstract = entry['abstract']
                words = AbstractProcessing.separate_white_spaces(
                    abstract=abstract)
                self.abstracts_words = self.abstracts_words + words

            # Prevents a duplicated article
            if self.verify_article_exists(article['title']):
                self.repeated_articles.append(article)
            else:
                self.articles.append(article)
        except Exception as e:
            print(e)

    def verify_article_exists(self, title):
        """
        Verifies if an article exists in the list of articles
        """
        for article in self.articles:
            if article['title'] == title:
                return True

    def inject_keywords(self, keywords):
        """
        Injects keywords into the articles
        """
        for keyword in keywords:
            if keyword not in self.keywords:
                self.keywords.append(keyword.strip())

    def inject_titles(self, title):
        """
        Injects titles into the articles
        """
        if title not in self.titles:
            self.titles.append(title.strip())

    def inject_authors(self, authors):
        """
        Injects authors into the articles
        """
        for author in authors:
            if author not in self.authors:
                self.authors.append(author.strip())

    def inject_journals(self, journal):
        """
        Injects journals into the articles
        """
        if journal not in self.journals:
            self.journals.append(journal)

    def plot_results(self):
        """
        Executes all the algorithms for the filtered results
        and then plots the results 
        """
        AlgorithmsExecution.execute_algorithms(
            self.titles,
            'TITLE')
        AlgorithmsExecution.execute_algorithms(
            self.authors,
            'AUTHOR')
        AlgorithmsExecution.execute_algorithms(
            self.journals,
            'JOURNAL')
        AlgorithmsExecution.execute_algorithms(
            self.keywords,
            'KEYWORDS')

    def generate_output_files(self):
        """
        Generates the output files
        1 bib file for filtered articles
        1 bib file for the repeated files
        """
        OutputFiles.create_output_file(self.articles, "filtered_articles")
        OutputFiles.create_output_file(
            self.repeated_articles, "repeated_articles")
        print("Output files created")

    def process_abstracts(self):
        "Process an plots the abstract words"
        abstract = AbstractProcessing()
        abstract.filter_keywords(self.abstracts_words)

    def print_results(self):
        """
        Prints the obtained results
        """
        print(len(self.titles), " Titles Filtered")
        print(len(self.articles), " Articles Filtered")
        print(len(self.journals), " Journals Filtered")
        print(len(self.keywords), " Keywords Filtered")
        print(len(self.authors), " Authors Filtered")
        print(len(self.repeated_articles), " Repeated Articles")
