class Seat:
    def __init__(self, free:bool, occupant:str):
        self.free=free
        self.occupant=occupant
        if self.occupant:
            self.free=False

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

