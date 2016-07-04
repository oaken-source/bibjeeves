
'''
This module provides the graphical user interface of bibjeeves.
'''

import tkinter as tk


class App(object):

    def __init__(self, master):
        menubar = tk.Menu(master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='search', command=self.search)
        filemenu.add_separator()
        filemenu.add_command(label='exit', command=master.quit)
        menubar.add_cascade(label='file', menu=filemenu)

        master.config(menu=menubar)

    def search(self):
        pass
