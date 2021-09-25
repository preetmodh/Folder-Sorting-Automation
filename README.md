# Folder-Sorting-Automation
Automating the process of sorting files in a user's download folder (but can be configured to sort any folder) on Windows by file type.

This script iterates through the files in the downloads folder and moves them to their respective sub-folders. If the 
sub-folder does not exist, it is created then the files are moved into it.

## Prerequisites
This script requires Python to be installed for it to run. To install Python, click [here.](https://www.python.org/downloads/)

## Usage
From a terminal, navigate into the project directory.
```
$ cd Folder-Sorting-Automation
```
To run the script:
```
$ python folder_sorter.py
```

To have the script run automatically, configure it in Windows Task Scheduler according to [this tutorial.](https://datatofish.com/python-script-windows-scheduler/)