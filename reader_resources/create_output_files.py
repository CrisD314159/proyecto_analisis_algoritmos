"""
  This module contains the class use to generate the output .bib files
"""

import os
import bibtexparser as bib


class OutputFiles:
    """
    A class that creates the output .bib files
    """

    @staticmethod
    def create_output_file(articles, file_name):
        """
        This method creates a .bib file with the articles in the articles list
        """
        # Get the absolute path of the project directory
        project_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..'))

        # Create the path to the output_files directory
        research_files_dir = os.path.join(project_dir, "output_files")

        # Concats the file name with the .bib extension
        bib_file_path = os.path.join(
            research_files_dir, f'{file_name}.bib')

        # Creates a new database an stores the articles in it
        bib_database = bib.bibdatabase.BibDatabase()
        bib_database.entries = articles

        # Dumps the database to a string
        bib_string = bib.dumps(bib_database)

        # Writes the string to a .bib file
        with open(bib_file_path, "w", encoding="utf-8") as bibfile:
            bibfile.write(bib_string)
        print(f"File {file_name}.bib created")
