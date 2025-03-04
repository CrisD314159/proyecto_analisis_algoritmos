"""
  This module uses python bibtexparser for the bib files handle
"""

import bibtexparser as bib


class ReaderImplementation:
    """
      This class is in charge of reading the bib files
    """

    def __init__(self):
        self.bib_files = []
