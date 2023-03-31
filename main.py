from memory import Memory
from process import Process
import time
import threading
from tkinter import *

condition = False

def start():
    global condition
    if not condition:
        condition = True
        thread = threading.Thread(target=execute)
        thread.start()


def stop():
    global condition
    condition = False

def execute():
    while condition:
        memory.gridRemove(lbls)
        memory.insertMemory(Process())
        memory.printMemory(root, lbls)
        memory.refresh()
        memory.compact()
        time.sleep(1)

root = Tk()

root.title('Gerenciador de memória')
root.option_readfile("optionDB.txt")
root.geometry('800x450')
root.resizable(False,False)

memory = Memory()
lbls = []
Label(root, text='Memória Virtual').grid(row=0, column=0, columnspan=8, padx=15)
Label(root, text='Processos').grid(row=0, column=15)
Button(root, text='Executar', command=start).grid(column=16, row=10, sticky=W, padx=5, pady=2)  
Button(root, text='Pause', command=stop).grid(column=17, row=10, sticky=W, padx=5, pady=2)

root.mainloop()