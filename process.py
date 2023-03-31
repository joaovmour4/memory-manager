import random
import string

class Process:
    processes = []
    mp = 0
    def __init__(self):
        while True:    
            tempID = random.choice(string.ascii_uppercase)
            if tempID not in Process.processes:
                self.id = tempID
                break
        self.size = random.randint(1, 4)
        self.time = random.randint(1, 2)
        temp = random.randint(1, 5)
        self.mpPos = [i for i in range(Process.mp, Process.mp + temp)]
        Process.mp += temp
        if Process.mp >= 99:
            Process.mp = 0

    
    def removeProcess(self):
        Process.processes.remove(self.id)

    def addProcess(self):
        Process.processes.append(self.id)