from process import Process
import random

class Memory:
    max = 20
    def __init__(self) -> None:
        self.memory = []
        self.processes = []
    
    def lenMemory(self):
        size = 0
        for i in range(len(self.memory)):
            size += len(self.memory[i])
        return size
    
    def insertMemory(self, process):
        if self.lenMemory() + process.size <= Memory.max:
            self.memory.append([process.id for i in range(process.size)])
            self.processes.append(process)
            process.addProcess()
        else:
            for i in range(len(self.memory)):
                if len(self.memory[i]) >= process.size and self.memory[i][0] == ' ':    
                    if len(self.memory[i]) == process.size:
                        for elemento in self.memory[i]:
                            elemento = process.id
                    else:
                        aux = len(self.memory[i]) - process.size
                        for j in range(aux):
                            self.memory[i].pop(-1)
                        self.memory[i] = [process.id for i in range(len(self.memory[i]))]
                        self.memory.insert(i+1, [' ' for i in range(aux)])
                    self.processes.append(process)
                    process.addProcess()
                    break
        
        
    
    def removeList(self, process):
        for i in range(len(self.memory)):
            if self.memory[i][0] == process.id:
                self.memory[i] = [' ' for i in range(len(self.memory[i]))]
                self.processes.remove(process)
                process.removeProcess()
    
    def refresh(self):
        aux = random.randrange(len(self.processes))
        self.processes[aux].time -= 1
        if self.processes[aux].time <= 0:
            self.removeList(self.processes[aux])
    
    def printMemory(self):
        print(self.memory)
        print(Process.processes)
            
