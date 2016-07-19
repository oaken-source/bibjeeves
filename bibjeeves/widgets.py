
'''
This module provides the widgets used in the bibjeeves gui.
'''

import tkinter as tk
import tkinter.ttk as ttk

from bibjeeves.config import CACHE


class DocumentListbox(tk.Listbox):
    '''
    hold the list of currently opened documents
    '''

    def __init__(self, master, **kwargs):
        '''
        constructor - create the widget and fill it with items from the cache
        '''
        super(DocumentListbox, self).__init__(master, **kwargs)

    def add_document(self, document):
        '''
        insert a new top level document to the list
        '''
        self.insert(tk.END, document)


class DocumentCanvas(tk.Canvas):
    '''
    render the citation tree of the current document
    '''

    def __init__(self, master, **kwargs):
        '''
        constructor - create the widget
        '''
        super(DocumentCanvas, self).__init__(master, **kwargs)


class CacheAwarePanedWindow(tk.PanedWindow):

    pass
