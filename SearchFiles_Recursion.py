# coding=UTF-8
'''
We can search directory  in the directory tree.
--------------------------------------
file
file
folder
｜----file
｜----file
｜----file
file 
file 
folder
｜----file
｜----file
｜----foder
     ｜----file
     ｜----file
'''

import os, sys
from os.path import join, isfile, isdir

#Official os.walk()
def originOsWalk(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            print("file:"+join(root, f))
        for d in dirs:
            print("directory:"+join(root, d))

#Practice  a simple version: os.walk       
def ScanDir(path):
    files = os.listdir(path)
    for f in files:
        abspath=join(path, f)
        SearchFile(abspath)

def SearchFile(abspath):
        
    if isfile(abspath):
        print("file:", abspath)

    elif isdir(abspath):
        print("directory:", abspath)
        ScanDir(abspath)

#Run above of two functions
def Run(num, OriPath):
    #https://docs.python.org/2/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python
    functions = {
        'a': originOsWalk,
        'b': ScanDir
    }
    func = functions.get(num,'invalid number')
    func(OriPath)
'''
 python SearchFiles_Recursion.py a 
                                    : originOsWalk
 python SearchFiles_Recursion.py b
                                    :   ScanDir
'''
OriPath = r"C:\Users\yug\Downloads"
if len(sys.argv)>1:
    num = sys.argv[1]
    Run(num, OriPath)





 
 
 
       




