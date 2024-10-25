from .table import Table
from typing import List
from random import shuffle
import pandas as pd


class Openspace:
    def __init__(self, tables: List[Table], number_of_tables: int):
        self.tables = tables
        self.number_of_tables = number_of_tables
    
    def __str__(self):
        return f"A open space object with the following tables disposition:\n{' '.join([table.__str__() for table in self.tables])}"  #todo complete description
    
    def organize(self, names: List[str]):
        shuffle(names)
        for table_nb,table in enumerate(self.tables):
            for seat_nb in range(table.capacity):
                if table.has_free_spot():
                    assigned_student = names[table_nb + seat_nb]
                    table.assign_seat(assigned_student)
    
    def store(self, file_name: str):
        tables_disposition = [[student.occupant for student in table.seats] for table in self.tables ]
        table_names = [f"Table {i + 1}" for i,table in enumerate(self.tables)]
        tables_df = pd.DataFrame(tables_disposition).T
        tables_df.columns = table_names
        tables_df.to_csv(file_name)


