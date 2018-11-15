# coding=UTF-8
'''
Pratice a simple version: os.walk
--------------------
file
file
folder
----file
----file
----file
file 
file 
folder
-----file
-----file
-----foder
     ----file
     ----file

'''
import os 

def ScanDir(path):
    files = os.listdir(path)
    for f in files:
        abspath=os.path.join(path,f)
        SearchFile(abspath)


def SearchFile(abspath):
        
    if os.path.isfile(abspath):
        print("file:",abspath)

    elif os.path.isdir(abspath):
        print("folder:",abspath)
        ScanDir(abspath)

OriPath = r"C:\Users\yug\Downloads"
ScanDir(OriPath)
 
 
       




