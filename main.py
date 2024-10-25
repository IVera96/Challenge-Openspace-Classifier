from utils.openspace import Openspace
from utils.table import Table
from random import shuffle
import pandas as pd



df = pd.read_excel('bouman_8.xlsx')
names_list = list(df['Students'])
shuffle(names_list)
tables_list = [Table(4, []) for table in range(6)]

open_space = Openspace(tables_list, 6)
print(open_space)
open_space.organize(names_list)
open_space.store('openspace.csv')