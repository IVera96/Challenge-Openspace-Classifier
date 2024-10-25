from typing import List
class Seat:
    """The Seat class with the constractor __init__(self, free: bool, occupant: str), represents a seat in a table.

    Attributes:
        free (bool): Indicates whether the seat is free or occupied.
        occupant (str): The name of the person occupying the seat. 
                        If the seat is free, this is None.

    Methods:
        __str__(): Returns a string that includes the seat's free state and the occupant's name (if any).
        set_occupant(self, name: str): Assigns a name to the seat's occupant if it is free.
        remove_occupant(self): Removes the current occupant from the seat, marking it as free.
    """

    def __init__(self, free:bool, occupant:str):
        self.free=free
        self.occupant=occupant
        if self.occupant:
            self.free=False
    
    def __str__(self):
       return f"A seat object with free state: {self.free} and occupied by {self.occupant}"

    def set_occupant(self,name:str):
        if self.free:
            self.occupant=name
        else:
            print(f'This seat is taken by {self.occupant}')

    def remove_occupant(self):
        if not self.free:
            previous_occupant=self.occupant
            self.occupant=None
            self.free=True
            return previous_occupant

        else:
            print('The seat is already empty')


class Table:
    """ The class Table with the constractor __init__(self,capacity: int, seats: List[Seat]), represents a table with a specific capacity and assigned seats.

    Attributes:
        capacity (int): The maximum number of occupants the table can accommodate.
        seats (List[Seat]): A list of Seat objects representing the seats at the table.

    Methods:
        __init__(capacity: int, seats: List[Seat]): Initializes a new Table instance with a given capacity and seats.
        __str__(): Returns a string representation of the table, including its capacity and occupants.
        has_free_spot() -> bool: Checks if there are any free spots available at the table.
        assign_seat(name: str): Assigns a name to a free seat at the table.
        left_capacity() -> int: Returns the number of free spots remaining at the table.
    """
    def __init__(self,capacity: int, seats: List[Seat]): #Todo: create fall-back if len(seats) > capacity
        self.capacity = capacity
        self.seats = seats
    def __str__(self):
        message = f"and with the following members: {', '.join([seat.occupant for seat in self.seats])}\n" if len(self.seats) else "empty at the moment\n"
        return f"A Table object with a capacity of {self.capacity}, {message}"


    def has_free_spot(self) -> bool:
        return self.letf_capacity() > 0

    def assign_seat(self, name: str):
        if self.has_free_spot():
            seat = Seat(True, name)
            self.seats.append(seat)
        else:
            print('Sorry, this table is currently full!')
    
    def letf_capacity(self) -> int:
        return self.capacity - len(self.seats)




