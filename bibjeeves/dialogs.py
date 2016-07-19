
'''
This module provides the dialogs used by bibjeeves.
'''

import tkinter as tk
import tkinter.ttk as ttk

from bibjeeves.config import CACHE
from bibjeeves.providers import CiteSeerxProvider


class DocumentImportDialog(tk.Toplevel):
    '''
    a dialog to produce documents from user input
    '''

    provider = CiteSeerxProvider()

    def __init__(self, master, **kwargs):
        '''
        constructor - position the dialog
        '''
        super(DocumentImportDialog, self).__init__(master, **kwargs)

        self.transient(master)
        self.grab_set()

        self.resizable(False, False)

        if 'layout' not in CACHE:
            CACHE['layout'] = dict()

        if 'dialog_x' in CACHE['layout'] and 'dialog_y' in CACHE['layout']:
            self.geometry('+%i+%i' % (CACHE['layout']['dialog_x'], CACHE['layout']['dialog_y']))

        self.bind('<Configure>', self.on_configure)
        self.bind('<Escape>', lambda *_: self.destroy())

        self.update_idletasks()

        CACHE['layout']['dialog_x'] = self.winfo_x
        CACHE['layout']['dialog_y'] = self.winfo_y

    def ask_document(self):
        '''
        produce a document from user input
        '''
        self.f0 = tk.Frame(self)
        self.f0.pack(padx=10, pady=5)

        f1 = tk.Frame(self.f0)
        f1.pack(pady=5)

        l1 = tk.Label(f1, text='text')
        l1.pack()
        self.text_edit = tk.Entry(f1)
        self.text_edit.pack()

        f2 = tk.Frame(self.f0)
        f2.pack(pady=5)

        l2 = tk.Label(f2, text='title')
        l2.pack()
        self.title_edit = tk.Entry(f2)
        self.title_edit.pack()

        f3 = tk.Frame(self.f0)
        f3.pack(pady=5)

        l3 = tk.Label(f3, text='author')
        l3.pack()
        self.author_edit = tk.Entry(f3)
        self.author_edit.pack()

        f4 = tk.Frame(self.f0)
        f4.pack(pady=5, fill=tk.X, side=tk.BOTTOM)

        b1 = tk.Button(f4, text='abort', command=self.destroy)
        b1.pack(side=tk.LEFT)
        b2 = tk.Button(f4, text='search', command=self.on_search_clicked)
        b2.pack(side=tk.RIGHT)

        self.master.wait_window(self)

    def on_configure(self, event):
        '''
        invoked when the dialog is moved to store its preferred position in the cache
        '''
        if event.widget == self:
            CACHE['layout']['dialog_x'] = event.x
            CACHE['layout']['dialog_y'] = event.y

    def on_search_clicked(self):
        '''
        invoked when the search button in is clicked
        '''
        text = self.text_edit.get() or None
        title = self.text_edit.get() or None
        author = self.author_edit.get() or None

        self.update_idletasks()

        documents = self.provider.query(text, title, author)
