#Ageel  10/27/2019
#100 Days of Python 
#Day 69 - File Handling

import os

f = open("C:\\Users\\Ageel\\Documents\\CodePy\\100py\\Week011\\demofile.txt","w")
#print(f.read(20))
#print(f.readline())
#print(f.readline())
f.write("Now we are writing to the file")
f.close()

f = open("C:\\Users\\Ageel\\Documents\\CodePy\\100py\\Week011\\demofile3.txt","w")
f.write("Now we are writing to the file3")
f.close()

os.remove("C:\\Users\\Ageel\\Documents\\CodePy\\100py\\Week011\\demofile2.txt")

f = open("C:\\Users\\Ageel\\Documents\\CodePy\\100py\\Week011\\demofile2.txt","x")
f.write("Now we are writing to the file2")
f.close()

