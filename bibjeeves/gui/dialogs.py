
'''
This module provides the dialogs used by bibjeeves.
'''

import tkinter as tk
import tkinter.ttk as ttk

from bibjeeves.config import CACHE


class DocumentImportDialog(tk.Toplevel):
    '''
    a dialog to produce documents from user input
    '''

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
        f0 = tk.Frame(self)
        f0.pack(padx=10, pady=5)

        f1 = tk.Frame(f0)
        f1.pack(pady=5)

        l1 = tk.Label(f1, text='text')
        l1.pack()
        e1 = tk.Entry(f1)
        e1.pack()

        f2 = tk.Frame(f0)
        f2.pack(pady=5)

        l2 = tk.Label(f2, text='title')
        l2.pack()
        e2 = tk.Entry(f2)
        e2.pack()

        f3 = tk.Frame(f0)
        f3.pack(pady=5)

        l3 = tk.Label(f3, text='author')
        l3.pack()
        e3 = tk.Entry(f3)
        e3.pack()

        f4 = tk.Frame(f0)
        f4.pack(pady=5, fill=tk.X)

        b1 = tk.Button(f4, text='abort', command=self.destroy)
        b1.pack(side=tk.LEFT)
        b2 = tk.Button(f4, text='next')
        b2.pack(side=tk.RIGHT)

        self.master.wait_window(self)

    def on_configure(self, event):
        '''
        invoked when the dialog is moved to store its preferred position in the cache
        '''
        if event.widget == self:
            CACHE['layout']['dialog_x'] = event.x
            CACHE['layout']['dialog_y'] = event.y
