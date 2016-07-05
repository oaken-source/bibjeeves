
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
        self.root = tk.Tk()

        self.menubar = MenuBar(self.root)
        self.panes = ThreePaneWindow(self.root)

        self.root.bind('<Control-q>', self.quit)

    def run(self):
        '''
        main loop
        '''
        self.root.mainloop()

    def quit(self, event):
        '''
        bound to ctrl+q
        '''
        event.widget.quit()

