"""
  This file contains utility functions that are used in the project.
"""

import os
import glob
import shutil
import json


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
        for file in file_type:
            pattern = os.path.join(downloads_folder, f"*.{file}")
            for file_path in glob.glob(pattern):
                file_name = os.path.basename(file_path)
                destination = os.path.join(self.destination_folder, file_name)

                # Ensure the destination directory exists
                os.makedirs(self.destination_folder, exist_ok=True)

                # Move the file
                shutil.move(file_path, destination)
                print(f"Moved {file_name} to {self.destination_folder}")

    def list_chrome_profiles(self):
        """
        Lists all available Chrome profiles on macOS and returns their paths
        """
        # Path to Chrome profiles on macOS
        base_path = os.path.expanduser(
            "~/Library/Application Support/Google/Chrome")

        try:
            # Check if the directory exists
            if not os.path.exists(base_path):
                print(f"Chrome directory not found at {base_path}")
                return []

            # Get all profile directories
            profiles = []

            # Always add Default profile if it exists
            default_profile = os.path.join(base_path, "Default")
            if os.path.exists(default_profile) and os.path.isdir(default_profile):
                profiles.append({"name": "Default", "path": default_profile})

            # Add numbered profiles
            for item in os.listdir(base_path):
                if item.startswith("Profile ") and os.path.isdir(os.path.join(base_path, item)):
                    profile_path = os.path.join(base_path, item)
                    profiles.append({"name": item, "path": profile_path})

            # Try to get profile names from Preferences files
            for profile in profiles:
                pref_file = os.path.join(profile["path"], "Preferences")
                if os.path.exists(pref_file):
                    try:
                        with open(pref_file, 'r', encoding='utf-8') as f:
                            prefs = json.load(f)
                            if "profile" in prefs and "name" in prefs["profile"]:
                                profile["display_name"] = prefs["profile"]["name"]
                    except (json.JSONDecodeError, UnicodeDecodeError, IOError) as e:
                        print(
                            f"Error reading preferences for {profile['name']}: {e}")

            # Print available profiles
            if profiles:
                print("Available Chrome profiles:")
                for i, profile in enumerate(profiles):
                    display_name = profile.get("display_name", "No Name")
                    print(f"{i+1}. {profile['name']} ({display_name})")
                    print(f"   Path: {profile['path']}")
            else:
                print("No Chrome profiles found.")

            return profiles

        except Exception as e:
            print(f"Error listing Chrome profiles: {e}")
            return []
