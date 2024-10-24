from typing import List
class Seat:
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




