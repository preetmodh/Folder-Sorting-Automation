import sys
from pathlib import Path

python_exe_path = sys.executable
python_script_path = Path('folder_sorter.py').resolve()
f= open("python_script.bat","w+")
f.write(f'"{python_exe_path}" "{python_script_path}"')
f.close()