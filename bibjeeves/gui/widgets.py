
'''
This module provides the widgets used in the bibjeeves gui.
'''

import tkinter as tk
import tkinter.ttk as ttk

from bibjeeves.config import CACHE


class MenuBar(tk.Menu):
    '''
    this is the menubar of bibjeeves
    '''

    def __init__(self, app, master, **kwargs):
        '''
        constructor - produce the menu bar with entries and add it to the master
        '''
        super(MenuBar, self).__init__(master, **kwargs)

        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label='import document', command=app.on_import_document)
        filemenu.add_command(label='close document', command=app.on_close_document)
        filemenu.add_separator()
        filemenu.add_command(label='exit', command=app.root.quit)
        self.add_cascade(label='file', menu=filemenu)

        editmenu = tk.Menu(self, tearoff=0)
        editmenu.add_command(label='find', command=app.on_find)
        self.add_cascade(label='edit', menu=editmenu)

        master.config(menu=self)

class ThreePaneWindow(tk.PanedWindow):
    '''
    this is the resizable top level layout of bibjeeves
    '''

    def __init__(self, app, master, **kwargs):
        '''
        constructor - set up the nested PanedWindows
        '''
        super(ThreePaneWindow, self).__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)

        right = tk.PanedWindow(self, orient=tk.VERTICAL, **kwargs)

        self.left = tk.Frame(self)
        self.top = tk.Frame(right)
        self.bottom = tk.Frame(right)

        if 'layout' not in CACHE:
            CACHE['layout'] = dict()

        self.update_idletasks()

        if 'panes_hsplit' not in CACHE['layout']:
            CACHE['layout']['panes_hsplit'] = self.winfo_width() // 5

        self.paneconfigure(self.left, minsize=50, width=CACHE['layout']['panes_hsplit'])
        self.paneconfigure(right, minsize=20)

        right.update_idletasks()

        if 'panes_vsplit' not in CACHE['layout']:
            CACHE['layout']['panes_vsplit'] = (right.winfo_height() * 3) // 4

        right.paneconfigure(self.top, minsize=20, height=CACHE['layout']['panes_vsplit'])
        right.paneconfigure(self.bottom, minsize=20)

        right.add(self.top)
        right.add(self.bottom)
        self.add(self.left)
        self.add(right)

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


class Listbox(tk.Listbox):
    '''
    hold the list of currently opened documents
    '''

    def __init__(self, app, master, **kwargs):
        '''
        constructor - create the widget and fill it with items from the cache
        '''
        super(Listbox, self).__init__(master, **kwargs)

        scrollbar = ttk.Scrollbar(master, command=self.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.pack(fill=tk.BOTH, expand=True)
        self.config(yscrollcommand=scrollbar.set)


class TreeCanvas(tk.Canvas):
    '''
    render the citation tree of the current document
    '''

    def __init__(self, app, master, **kwargs):
        '''
        constructor - create the widget
        '''
        super(TreeCanvas, self).__init__(master, **kwargs)

        self.pack(fill=tk.BOTH, expand=True)


class Infobox(tk.Text):
    '''
    render information about the currently selected document
    '''

    def __init__(self, app, master, **kwargs):
        '''
        constructor - create the widget
        '''
        super(Infobox, self).__init__(master, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)
