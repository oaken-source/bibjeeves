
'''
This module provides the graphical user interface of bibjeeves.
'''

import tkinter as tk

from bibjeeves.gui.widgets import MenuBar, ThreePaneWindow, Listbox, TreeCanvas, Infobox


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
        menubar = MenuBar(self.root)
        panes = ThreePaneWindow(self.root)

        listbox = Listbox(panes.left)
        treecanvas = TreeCanvas(panes.top)
        infobox = Infobox(panes.bottom)

        self._setup_keybindings()

    def _setup_keybindings(self):
        '''
        bind relevant keys to functions
        '''
        self.root.bind('<Control-q>', lambda _: self.root.quit())

    def run(self):
        '''
        start the tk main loop and start processing events
        '''
        self.root.mainloop()
