import itertools
import threading
import time
import sys
import os
from game import game

clear = lambda: os.system('clear')
done = False

ots1 = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
ots2 = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
titlemenu = "( -_-) Главное меню HANKMAN (-_- )"
stage = "<play>"
stage1 = "<exit>"

titlemenu = titlemenu.center(64)
stage = stage.center(64)
stage1 = stage1.center(64)
ots1 = ots1.center(64)
ots2 = ots2.center(64)

print(ots1)
print(titlemenu)
print("\n")
print(stage)
print(stage1)
print(ots2)

menu = input()

if menu == "play":
    time.sleep(1)
    game()
elif menu == "exit":
    clear()
