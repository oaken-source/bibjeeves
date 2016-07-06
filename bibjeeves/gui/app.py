
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
        menubar = MenuBar(self, self.root)

        panes = ThreePaneWindow(self, self.root)

        listbox = Listbox(self, panes.left)
        treecanvas = TreeCanvas(self, panes.top)
        infobox = Infobox(self, panes.bottom)

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

    def on_import_document(self):
        raise NotImplementedError('todo')

    def on_close_document(self):
        raise NotImplementedError('todo')

    def on_find(self):
        raise NotImplementedError('todo')
