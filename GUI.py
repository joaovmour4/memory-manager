from memory import Memory
from process import Process
import os, time
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
        memory.insertMemory(Process())
        memory.printMemory(root)
        memory.refresh()
        memory.compact()
        time.sleep(1)

root = Tk()

memory = Memory()

Button(root, text='Executar', command=start).grid(column=10, row=10, sticky=W, padx=5, pady=2)  
Button(root, text='Pause', command=stop).grid(column=11, row=10, sticky=W, padx=5, pady=2)

root.mainloop()