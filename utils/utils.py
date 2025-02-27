"""
  This file contains utility functions that are used in the project.
"""

import os
import glob
import shutil


class Utils:
    """
        Utility functions for the project.
    """

    def __init__(self):
        self.project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
        self.destination_folder = os.path.join(
            self.project_root, "researchFiles")

    def move_downloaded_files(self):
        """
        Moves downloaded files from the Downloads folder to the specified destination folder.
        """

        file_type = ['bib']

        # Get user's downloads folder
        downloads_folder = os.path.join(
            os.path.expanduser('~'), 'Downloads')

        # Use glob to find files with the specified extension
        pattern = os.path.join(downloads_folder, f"*.{file_type}")
        for file_path in glob.glob(pattern):
            file_name = os.path.basename(file_path)
            destination = os.path.join(
                self.destination_folder, file_name)

            # Move the file
            shutil.move(file_path, destination)
            print(f"Moved {file_name} to {self.destination_folder}")
