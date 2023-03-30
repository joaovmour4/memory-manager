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
                self.memory[i] = [' ' for i in range(len(self.memory[i]))]
                self.processes.remove(process)
                process.removeProcess()
    
    def refresh(self):
        aux = random.randrange(len(self.processes))
        self.processes[aux].time -= 1
        if self.processes[aux].time <= 0:
            self.removeList(self.processes[aux])
    
    # def printMemory(self):
    #     print(f'Memória virtual: {self.memory}')
    #     print('Memória principal: ')
    #     for i in self.processes:
    #         print(f'Endereços {i.memoryP} a {i.memoryP+i.size} : {i.id}')

    def printMemory(self, root):
        lbls = []
        row = 1
        col = 0
        if len(lbls) == 0:
            for elemento in self.processes:
                lbl = Label(root, text=f'{elemento.id}',
                            width=5, height=1, borderwidth=1, relief='solid')
                lbls.append(lbl)
                lbl.grid(row=row, column=col, columnspan=elemento.size, pady=2, padx=10)
                col += 1
                if col >= 5:
                    col = 0
                    row += 1
        else:
            for elemento in lbls:
                elemento.grid_remove()

            for i in range(len(self.processes)):
                    lbls[i]['text'] = f'{self.processes[i].id}'
                    lbl.grid(row=row, column=col, columnspan=self.processes[i].size, pady=2, padx=1)
                    col += 1
                    if col >= 5:
                        col = 0
                        row += 1

    def compact(self):
        if len(self.memory) >= Memory.max/2:
            for segment in self.memory:
                if ' ' in segment:
                    self.memory.remove(segment)
            
