"""
This script iterates through the files in a user's downloads folder on Windows and places each file in its appropriate
folder.

This script could be run to sort any files in any folder just instead of Downloads in folder_path write relative path of your folder
"""

import shutil
import getpass
from pathlib import Path
from config import EXTENSION_CONFIG as CATEGORIES


def move_file(file, destination):
    """Checks if the destination folder exists, creates it if it doesn't, then moves a file into it
    Parameters
    file : Path
        the path to a file
    destination : Path
        the path to the destination folder
    """

    if not destination.exists():
        destination.mkdir(parents=True, exist_ok=True)
    shutil.move(file, destination)


def sort_folder(folder_path):
    """Iterates through the files in the folder"""
    for file in folder_path.iterdir():
        if file.is_file():
            destination = folder_path / CATEGORIES.get(file.suffix, 'Others')
            move_file(file, destination)


if __name__ == '__main__':
    folder_path = Path("/Users", getpass.getuser(), "Downloads")
    print(f"Sorting {folder_path}") 
    sort_folder(folder_path)
    print("Done")