# Python ver 3.8.0
#
# Author:  Tori Jesser
#
# Purpose:    Demonstrate OOP, Tkinter GUI module,
#             using Tkiner Parent and Child relationships.
#
# Tested OS: this code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

import drill_main



def load_gui(self):

    self.txt_entry1 = tk.Entry(self.master,text='')
    self.txt_entry1.grid(row=0,column=1,rowspan=1,columnspan=6,padx=(15,0),pady=(45,0),sticky=N+E+W)
    self.txt_entry2 = tk.Entry(self.master,text='')
    self.txt_entry2.grid(row=1,column=1,rowspan=1,columnspan=6,padx=(15,0),pady=(10,0),sticky=N+E+W)
    

    self.btn_browse = tk.Button(self.master,width=14,height=1,text='Browse...')
    self.btn_browse.grid(row=0,column=0,padx=(15,0),pady=(45,0),sticky=W)
    self.btn_browse1 = tk.Button(self.master,width=14,height=1,text='Browse...')
    self.btn_browse1.grid(row=1,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_check = tk.Button(self.master,width=14,height=2,text='Check for files...')
    self.btn_check.grid(row=2,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_close = tk.Button(self.master,width=14,height=2,text='Close Program')
    self.btn_close.grid(row=2,column=4,padx=(350,0),pady=(10,0),sticky=E)
    
    
