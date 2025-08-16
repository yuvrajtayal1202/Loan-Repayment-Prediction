import os
import sys
import logging
import pathlib 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'CNN_Clasifier'

list_of_files = [
    '.github/workflows/.gitkeep',
    'src/components/__init__.py',
    'src/utils/__init__.py',
    'src/config/__init__.py',
    'src/config/configuration.py',
    'src/pipeline/__init__.py',
    'src/entity/__init__.py',
    'src/constant/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trial.ipynb',
    'template/index.html'
]

for file_path in list_of_files:
    file_path = pathlib.Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if(file_dir):
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating directory; {file_dir} for file: {file_name}')
        
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f'creating empty file: {file_path}')
            
    else:
        logging.info(f'{file_name} Already exists!')