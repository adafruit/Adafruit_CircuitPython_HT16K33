#!/usr/bin/env python3
from os import environ, system
from posixpath import isdir, isfile
from time import sleep
import subprocess

HOME = environ["HOME"]
print("HOME = {0}".format(HOME))

FROM_DIR = "{0}/Downloads/OS/Circuitpython/Libraries/bundle/lib".format(HOME)
TO_DIR = "{0}/Downloads/OS/Circuitpython/Libraries/lib".format(HOME)
ORIGINAL_DIR = "/media/hybotics/DISPLAYPY/lib/"

LIST = subprocess.getoutput("dir {0}".format(ORIGINAL_DIR)).strip()
print("LIST = '{0}'".format(LIST))
print()

LIST = LIST.split()
print("LIST = '{0}'".format(LIST))
print()

print("FROM_DIR = '{0}'".format(FROM_DIR))
print("TO_DIR = '{0}'".format(TO_DIR))
print()
sleep(5)

for FILE in LIST:
    FILE = FILE.strip()
    print("FILE = '{0}'".format(FILE))
    FN = ("{0}/{1}").format(FROM_DIR, FILE)

    print("FN = '{0}'".format(FN))

    if (isdir(FN)):
        print("COPYING DIRECTORY '{0}' to '{1}'".format(FN, TO_DIR))
        command = "cp -rf {0} {1}".format(FN, TO_DIR)
        #print("command = '{0}'".format(command))
        system(command)
    elif (isfile(FN)):
        print("COPYING FILE '{0}' to '{1}'".format(FN, TO_DIR))
        command = "cp {0} {1}".format(FN, TO_DIR)
        #print("command = '{0}'".format(command))
        system(command)
    else:
      print("File is not a directory or file!")

    print()
    sleep(1)
