from process import Process
import random
from tkinter import *


class Memory:
    max = 20

    def __init__(self):
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
                if len(self.memory[i]) >= process.size and ' ' in self.memory[i]:
                    if len(self.memory[i]) == process.size:
                        self.memory[i] = [process.id for i in range(len(self.memory[i]))]
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
                self.processes.remove(process)
                self.memory[i] = [' ' for i in range(len(self.memory[i]))]
                process.removeProcess()
    
    def refresh(self):
        aux = random.randrange(len(self.processes))
        self.processes[aux].time -= 1
        if self.processes[aux].time <= 0:
            self.removeList(self.processes[aux])

    def printMemory(self, root, lbls):
        for i in range(len(self.memory)):
            lbl = Label(root, text=self.memory[i][0], width=len(self.memory[i]), borderwidth=1, relief='solid')
            lbls.append(lbl)
            lbl.grid(row=1, column=i, sticky=EW)
        for i in range(len(self.processes)):    
            lbl = Label(root, text=f'Processo: {self.processes[i].id}, Posições MP: {self.processes[i].mpPos}\
                        \nEspaço virtual alocado: {self.processes[i].size}', 
                        width=40, borderwidth=1, relief='solid', anchor='w')
            lbls.append(lbl)
            lbl.grid(row=i+1, column=15, padx=10, sticky=EW)
            

    def gridRemove(self, lbls):
        if len(lbls) != 0:
            for lbl in lbls:
                lbl.grid_remove()

    def compact(self):
        if len(self.memory) >= Memory.max/2:
            for segment in self.memory:
                if ' ' in segment:
                    self.memory.remove(segment)
            
