import os # os is a Python module for operating system related functionality
from pathlib import Path # pathlib is a Python module for working with files and directories
import logging # logging is a Python module for logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'textSummarizer' # name of the project

list_of_files = [
    ".github/workflows/.gitkeep", # useful for writing CICD deployment YAML files
    f"src/{project_name}/__init__.py", #  constructor file that serves as an indicator to the Python interpreter that a directory should be treated as a Python package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # utilities written in common.py
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb" # experiments for our Text Generation model
]

# logic to write the creation of the files
for filepath in list_of_files:
    filepath = Path(filepath) # detects the OS and parses the filepath
    filedir, filename = os.path.split(filepath) # retrieve the directory and the filename

    # logic to create the directory if it is not already present
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # creates the directory if it is not already present
        logging.info(f"Created directory: {filedir} for file: {filename}")

    # logic to create the file if it is not already present
    if not os.path.isfile(filepath) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filename}")

    else:
        logging.info(f"File already exists: {filename}")

