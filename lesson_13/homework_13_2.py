import json
from pathlib import Path
import logging

"""Завдання 2:

Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""
logging.basicConfig(filename='json__kolosar.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


parent_dir = Path('lesson_13/work_with_json')

for file in parent_dir.iterdir():
    if file.is_file() and file.suffix == ".json":
        try:
            with open(file, "r", encoding="utf-8") as f:
                json.load(f)
            print(f"[OK] {file.name} - валідний JSON.")
        except json.decoder.JSONDecodeError:
            content = ""
            logging.error(f"{file.name} - невалідний JSON.")
        
