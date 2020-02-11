# Python ver 3.8.0
#
# Author:  Tori Jesser
#
# Purpose:    Demonstrate OOP, Tkinter GUI module,
#             using Tkiner Parent and Child relationships.
#
# Tested OS: this code was written and tested to work with Windows 10.

import os 
from tkinter import *
from tkinter import filedialog
import tkinter as tk


import dir_drill_main
import dir_drill_gui



def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def openDirectory(self):
    directory = filedialog.askdirectory()
    print(self.txt_entry1.insert(INSERT,directory))

   
    
         
