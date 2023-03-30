import random
import string

class Process:
    processes = []
    memoryP = 0
    def __init__(self):
        while True:    
            tempID = random.choice(string.ascii_uppercase)
            if tempID not in Process.processes:
                self.id = tempID
                break
        self.size = random.randint(1, 7)
        self.time = random.randint(1, 2)
        self.memoryP = Process.memoryP
        Process.memoryP += self.size+1

    
    def removeProcess(self):
        Process.processes.remove(self.id)

    def addProcess(self):
        Process.processes.append(self.id)