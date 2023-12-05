import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    '__init__.py',
    'config.yaml',
    'requirements.txt',
    'run_deployment.py',
    'run_pipeline.py',
    'app.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir , exist_ok=True)
        logging.info(f'Created directory : {filedir} for the file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            logging.info(f'Created empty file : {filename} at location {filepath} ')
            
    else: 
        logging.info(f'{filename} is Already Exists!')