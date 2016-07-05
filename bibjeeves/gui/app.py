
'''
This module provides the graphical user interface of bibjeeves.
'''

import tkinter as tk

from bibjeeves.gui.widgets import MenuBar, ThreePaneWindow


class App(object):
    '''
    this class represents the gui context of bibjeeves
    '''

    def __init__(self):
        '''
        constructor - hook into tk and initinalize the widgets
        '''
        # create tk context
        self.root = tk.Tk()

        # place widgets
        self.menubar = MenuBar(self.root)
        self.panes = ThreePaneWindow(self.root)

        # global key bindings
        self.root.bind('<Control-q>', lambda _: self.root.quit())

    def run(self):
        '''
        start the tk main loop and start processing events
        '''
        self.root.mainloop()
