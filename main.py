from memory import Memory
from process import Process
import os, time


memory = Memory()


while True:
    memory.insertMemory(Process())
    memory.printMemory()
    memory.refresh()
    memory.compact()
    time.sleep(1)
    os.system('cls')

