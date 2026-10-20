import os.path
import csv 


class FileDatabase:

    def __init__(self,file_name,model):
        self.path_file_name = f'database/{file_name}.csv'
        columns = list(model.model_fields.keys())
        if not os.path.exists(self.path_file_name):
            with open(self.path_file_name, "w", encoding="UTF-8",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(columns)

    def read_data(self):
        with open(self.path_file_name, "r",encoding="UTF-8",newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def write_data(self,data:list):
        if len(columns) != len(data):
            raise ValueError("algum dos campos está vazio e não pode realizar a inserção na base de dados")
        
        with open(self.path_file_name, "a",encoding="UTF-8",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)
