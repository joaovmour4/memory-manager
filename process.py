import random
import string

class Process:
    processes = []
    def __init__(self):
        while True:    
            tempID = random.choice(string.ascii_uppercase)
            if tempID not in Process.processes:
                self.id = tempID
                break
        self.size = random.randint(1, 5)
        self.time = random.randint(1, 3)
        # if self.posInit is not None:    
        #     self.insertDict(memory)
        # Process.processes.append(self.id)

    
    def removeProcess(self):
        Process.processes.remove(self.id)

    def addProcess(self):
        Process.processes.append(self.id)