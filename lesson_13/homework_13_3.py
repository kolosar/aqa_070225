import xml.etree.ElementTree as ET
from pathlib import Path
import logging

"""Завдання 3:

Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console_handler)

xml_path = Path(__file__).parent / "groups.xml"



def find_group():
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                logging.info(f"Group: {group.find('number').text}, incoming: {incoming.text}")
                
            else:
                logging.infof("Group: {group.find('number').text}, incoming: Не знайдено")
                
if __name__ == "__main__":
    find_group()     

 