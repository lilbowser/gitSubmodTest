"""
A test project for experimenting with git submodule and subtree

If we want the main project to be in a folder along side modules:
import sys
sys.path.append("..") # Adds higher directory to python modules path.
"""
from modules.module1 import mod

if __name__ == '__main__':
    mod.pr()
    print("Submod test!")