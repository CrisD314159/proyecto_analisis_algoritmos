"""
  This module uses python bibtexparser for the bib files handle
"""

import os
import glob
import bibtexparser as bib
import re


class ReaderImplementation:
    """
      This class is in charge of reading the bib files
    """

    def __init__(self):
        self.bib_files = []
        self.titles = list()
        self.articles = []
        self.repeat_titles = []

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
        for file in self.bib_files:
            print(file)
            with open(file, encoding='utf-8') as bib_file:
                library = bib.load(bib_file)
            file_entries = library.entries

            for entry in file_entries:
                self.separate_entry_keys(entry)

        print(len(self.titles))
        print(len(self.articles))
        print(len(self.repeat_titles))

    def separate_entry_keys(self, entry):
        """
        Separates the key of a bib entry
        """
        try:

            article = {}
            # Extract authors if present
            if 'author' in entry:
                # Split authors by 'and' and strip whitespace
                authors = [author.strip()
                           for author in re.split(' and |,', entry['author'])]
                article['authors'] = authors

            if 'title' in entry:
                title = entry['title']
                self.titles.append(title)
                article['title'] = title

            if 'journal' in entry or 'publisher' in entry:
                journal = entry['journal'] if 'journal' in entry else entry['publisher']
                article['journal'] = journal

            if 'year' in entry:
                year = entry['year']
                article['year'] = year

            if self.verify_article_exists(article['title']):
                self.repeat_titles.append(article)
            else:
                self.articles.append(article)
        except Exception as e:
            print(e)
            print(e.args)
            print(entry)

    def verify_article_exists(self, title):
        """
        Verifies if an article exists in the list of articles
        """
        for article in self.articles:
            if article['title'] == title:
                return True

    def run(self):
        """
        Initializes the reading process
        """
        self.list_bib_files()
        self.read_bib_files()
