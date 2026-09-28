import os.path
import csv 

file_name = "storage/database.csv"

class FileDatabase:

    def __init__(self,file_name):
        self.filename = file_name
        if not os.path.exists(file_name):
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Age", "City"])

    def read_data(self):
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def write_data(self,data:list):
        if len(data) != 3:
            raise ValueError("algum dos campos está vazio e não pode realizar a inserção na base de dados")
        
        with open(self.file_name, "a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)



file_db = FileDatabase(file_name)

file_db.read_data()