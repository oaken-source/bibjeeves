
'''
This module provides the widgets used in the bibjeeves gui.
'''

import tkinter as tk

from bibjeeves.config import CACHE


class MenuBar(object):
    '''
    this is the menubar of bibjeeves
    '''

    def __init__(self, master):
        '''
        constructor - produce the menu bar with entries and add it to the master
        '''
        menu = tk.Menu(master)

        filemenu = tk.Menu(menu, tearoff=0)
        filemenu.add_command(label='import document', command=self.on_import_document)
        filemenu.add_command(label='close document', command=self.on_close_document)
        filemenu.add_separator()
        filemenu.add_command(label='exit', command=master.quit)
        menu.add_cascade(label='file', menu=filemenu)

        editmenu = tk.Menu(menu, tearoff=0)
        editmenu.add_command(label='find', command=self.on_find)
        menu.add_cascade(label='edit', menu=editmenu)

        master.config(menu=menu)

    def on_import_document(self):
        raise NotImplementedError('todo')

    def on_close_document(self):
        raise NotImplementedError('todo')

    def on_find(self):
        raise NotImplementedError('todo')


class ThreePaneWindow(object):
    '''
    this is the resizable top level layout of bibjeeves
    '''

    def __init__(self, master):
        '''
        constructor - set up the nested PanedWindows
        '''
        level1 = tk.PanedWindow(master, sashrelief=tk.RAISED)
        level1.pack(fill=tk.BOTH, expand=True)

        level2 = tk.PanedWindow(level1, orient=tk.VERTICAL, sashrelief=tk.RAISED)

        self.left = tk.Frame(level1)
        self.top = tk.Frame(level2)
        self.bottom = tk.Frame(level2)

        if 'layout' not in CACHE:
            CACHE['layout'] = dict()

        level1.update_idletasks()

        if 'panes_hsplit' not in CACHE['layout']:
            CACHE['layout']['panes_hsplit'] = level1.winfo_width() // 5

        level1.paneconfigure(self.left, minsize=50, width=CACHE['layout']['panes_hsplit'])
        level1.paneconfigure(level2, minsize=20)

        level2.update_idletasks()

        if 'panes_vsplit' not in CACHE['layout']:
            CACHE['layout']['panes_vsplit'] = (level2.winfo_height() * 3) // 4

        level2.paneconfigure(self.top, minsize=20, height=CACHE['layout']['panes_vsplit'])
        level2.paneconfigure(self.bottom, minsize=20)

        level2.add(self.top)
        level2.add(self.bottom)
        level1.add(self.left)
        level1.add(level2)

        self.left.bind('<Configure>', self.on_panes_hsplit_configure)
        self.top.bind('<Configure>', self.on_panes_vsplit_configure)

    def on_panes_hsplit_configure(self, event):
        '''
        called when the horizontal panes are resized to update the cache
        '''
        CACHE['layout']['panes_hsplit'] = event.width

    def on_panes_vsplit_configure(self, event):
        '''
        called when the vertical panes are resized to update the cache
        '''
        CACHE['layout']['panes_vsplit'] = event.height

