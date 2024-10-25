from .table import Table
from typing import List
from random import shuffle
import pandas as pd


class Openspace:
    """ The Openspace class with the constractor __init__(self, tables: List[Table], number_of_tables: int), 
represents an open space with multiple tables for seating.
        This class manages a list of tables and allows for the organization of occupants into those tables. 
It provides functionality for shuffling names, assigning seats, and displaying the current seating arrangement.

    Attributes:
        tables (List[Table]): A list of Table objects representing the tables in the open space.
        number_of_tables (int): The total number of tables available.
        room_disposition (pd.DataFrame): A DataFrame representing the seating arrangement of occupants at each table.

    Methods:
        __str__(): Returns a string representation of the open space and its table disposition.
        organize(names: List[str]): Shuffles the given names and assigns them to available seats at the tables.
        store(file_name: str): Saves the current seating arrangement to a CSV file.
        display(): Displays the occupants of each table in a readable format.
     """
    def __init__(self, tables: List[Table], number_of_tables: int):
        self.tables = tables
        self.number_of_tables = number_of_tables
    def __str__(self):
        return f"A open space object with the following tables disposition:\n{' '.join([table.__str__() for table in self.tables])}"  #todo complete description
    
    def organize(self, names: List[str]):
        shuffle(names)
        count=0
        for table_nb,table in enumerate(self.tables):
            for seat_nb in range(table.capacity):
                if table.has_free_spot():
                    assigned_student = names[count]
                    table.assign_seat(assigned_student)
                    count+=1
        tables_disposition = [[student.occupant for student in table.seats] for table in self.tables ]
        table_names = [f"Table {i + 1}" for i in range(len(self.tables))]
        tables_df = pd.DataFrame(tables_disposition).T
        tables_df.columns = table_names
        self.room_disposition = tables_df
    
    def store(self, file_name: str):
        self.room_disposition.to_csv(file_name)

    def display(self):
        print('Open Space Table Assignments:')
        for i, table in enumerate(self.tables, 1):
            print(f'Table {i} with his occupants:')
            occupants = [seat.occupant for seat in table.seats if seat.occupant]
            print(','.join(occupants) if occupants else 'No occupants', end=' ')
            print() 
