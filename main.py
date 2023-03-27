from memory import Memory
from process import Process
import os, time


memory = Memory()


while True:
    memory.insertMemory(Process())
    memory.printMemory()
    memory.refresh()
    time.sleep(0.5)
    os.system('cls')

