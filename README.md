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

## To Automate on start-up
### 1.) run the create_bat_file(``` python create_bat_file.py ```) , it will create a ``` python_script.bat ``` file.
<br />

### 2.) then search Task Schedular in windows search and open it.
### 3.) after opening click on create task on the right side
<div>
<img  src="https://github.com/preetmodh/Folder-Sorting-Automation/blob/main/task_schedular_images/task schedular.JPG?raw=true" alt="Logo">
</div>
<br />

### 4.) in general tab type the name of the task, it can be any name.
<div>
<img   src="https://github.com/preetmodh/Folder-Sorting-Automation/blob/main/task_schedular_images/name.JPG?raw=true" alt="Logo">
</div>
<br />

### 5.) in trigger tab select begin task:at startup, and in advanced settings delay task for 30 seconds.
<div>
<img   src="https://github.com/preetmodh/Folder-Sorting-Automation/blob/main/task_schedular_images/trigger.JPG?raw=true" alt="Logo">
</div>
<br />

### 6.) in action tab select action as start a program and choose the python_script.bat file that was created as program/script.
<div>
<img   src="https://github.com/preetmodh/Folder-Sorting-Automation/blob/main/task_schedular_images/action.JPG?raw=true" alt="Logo">
</div>
<br />

### 7.) in conditions tab uncheck all the checboxes given
<div>
<img   src="https://github.com/preetmodh/Folder-Sorting-Automation/blob/main/task_schedular_images/conditions.JPG?raw=true" alt="Logo">
</div>
<br />

## 8.) Done, now whenever your pc turns on the folder will be automatically sorted.
<br />
<br />
<br />

