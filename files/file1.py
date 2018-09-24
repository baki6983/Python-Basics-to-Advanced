import os
import sys

print ("The current working directory is", os.path.abspath("files/readMe.txt"))
try:
#  f=open("files/readMe.txt","r")
#  for i in f:
#     print(i)
 f=open("files/readMe.txt","a")
 f.write("Its from append mode")
 f1 = open("myfile.txt", "x")
except:
 print ("Could not read file:")

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

print(os.path.dirname(sys.executable))

