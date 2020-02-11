# Python ver 3.8.0
#
# Author:  Tori Jesser
#
# Purpose:    Demonstrate OOP, Tkinter GUI module,
#             using Tkiner Parent and Child relationships.
#
# Tested OS: this code was written and tested to work with Windows 10.

import tkinter as tk
from tkinter import *
from tkinter import filedialog


import dir_drill_main
import dir_drill_func


def load_gui(self):

    self.txt_entry1 = tk.Entry(self.master,text='',width=60)
    self.txt_entry1.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(15,0),pady=(45,0),sticky=N+E+W)
    

    self.btn_browse = tk.Button(self.master,width=20,height=1,text='Browse...',command=lambda: dir_drill_func.openDirectory(self))
    self.btn_browse.grid(row=0,column=0,padx=(15,0),pady=(45,0),sticky=W)

    
    
