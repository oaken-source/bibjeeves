
'''
This module provides the graphical user interface of bibjeeves.
'''

import tkinter as tk

from bibjeeves.config import CACHE


class App(object):

    def __init__(self, master):
        menubar = MenuBar(master)

        panes = tk.PanedWindow(master, sashrelief=tk.RAISED)
        panes.pack(fill=tk.BOTH, expand=True)

        left = tk.LabelFrame(panes, text='left')
        right = tk.PanedWindow(panes, orient=tk.VERTICAL, sashrelief=tk.RAISED)
        top = tk.LabelFrame(right, text='top')
        bottom = tk.LabelFrame(right, text='bottom')

        if 'panes' not in CACHE:
            CACHE['panes'] = dict()

        panes.update_idletasks()

        if 'width' not in CACHE['panes']:
            CACHE['panes']['width'] = panes.winfo_width() // 5

        panes.paneconfigure(left, minsize=50, width=CACHE['panes']['width'])
        panes.paneconfigure(right, minsize=20)

        right.update_idletasks()

        if 'height' not in CACHE['panes']:
            CACHE['panes']['height'] = (right.winfo_height() * 3) // 4

        right.paneconfigure(top, minsize=20, height=CACHE['panes']['height'])
        right.paneconfigure(bottom, minsize=20)

        right.add(top)
        right.add(bottom)
        panes.add(left)
        panes.add(right)

        left.bind('<Configure>', self.on_horizontal_resize)
        top.bind('<Configure>', self.on_vertical_resize)
        master.bind('<Control-q>', self.quit)

    def on_horizontal_resize(self, event):
        CACHE['panes']['width'] = event.width

    def on_vertical_resize(self, event):
        CACHE['panes']['height'] = event.height

    def quit(self, event):
        event.widget.quit()


class MenuBar(object):

    def __init__(self, master):
        menu = tk.Menu(master)

        filemenu = tk.Menu(menu, tearoff=0)
        filemenu.add_command(label='open document', command=self.on_open_document)
        filemenu.add_command(label='close document', command=self.on_close_document)
        filemenu.add_separator()
        filemenu.add_command(label='exit', command=master.quit)
        menu.add_cascade(label='file', menu=filemenu)

        editmenu = tk.Menu(menu, tearoff=0)
        editmenu.add_command(label='find', command=self.on_find)
        menu.add_cascade(label='edit', menu=editmenu)

        master.config(menu=menu)

    def on_open_document(self):
        raise NotImplementedError('todo')

    def on_close_document(self):
        raise NotImplementedError('todo')

    def on_find(self):
        raise NotImplementedError('todo')


