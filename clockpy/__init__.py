from time import time, sleep
import random

class Clockpy:
    def __init__(self):
        self.start = time()
        self.values = {'start': self.start, 'finish': self.start}


    def checkpoint(self):
        count = len(self.values.values())
        
        check = time() - self.start

        if count == 2:
            self.values[f'Checkpoint {count - 1}'] = check
        if count > 2:
            self.values[f'Checkpoint {count - 1}'] = check - self.values[f'Checkpoint {count - 2}']
        
        self.values['finish'] = self.values[f'Checkpoint {count - 1}']



teste = Clockpy()

for i in range(10):
    teste.checkpoint()