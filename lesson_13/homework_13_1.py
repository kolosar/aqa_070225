import csv
from pathlib import Path

def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)
    
def remove_duplicates(data1, data2):
    result = []
    
    for row in data1 + data2:
        if row not in result:
            result.append(row)
            
    return result
        
def write_csv(data, result_csv):
    with open(result_csv, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        for row in data:
            writer.writerow(row)
    
if __name__ == "__main__":
    
    my_csv = Path(__file__).parent / "r-m-c.csv"
    my_csv_2 = Path(__file__).parent / "random-michaels.csv"
    result_csv = Path(__file__).parent / "result_kolosar.csv"
    
    #Зчитування данних
    data1 = read_file(my_csv)
    data2 = read_file(my_csv_2)
    
    #Видалення дуплікатів 
    unique_rows = remove_duplicates(data1, data2)
    
    #Запис у файл
    write_csv(unique_rows, result_csv)
   