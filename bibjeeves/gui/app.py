
'''
This module provides the graphical user interface of bibjeeves.
'''

import importlib
from os.path import join, dirname
import tkinter as tk
import xml.etree.ElementTree as et


def get_class(name):
    modulename, clsname = name.rsplit('.', 1)
    module = importlib.import_module(modulename)
    return getattr(module, clsname)


def get_attributes(attributes, prefix):
    if prefix is None:
        return {key: value for key, value in attributes.items() if '.' not in key}
    else:
        return {key.rsplit('.', 1)[-1]: value for key, value in attributes.items() if key.rsplit('.', 1)[0] == prefix}


class TkApp(object):

    def __init__(self):
        '''
        constructor - hook into tk
        '''
        self.root = None

    def _materialize(self, xml, master=None):
        '''
        materialize an xml tree into a tkinter layout
        '''
        if xml.tag == 'tkinter.Menu.command':
            master.add_command(**get_attributes(xml.attrib, None))
        elif xml.tag == 'tkinter.Menu.separator':
            master.add_separator()
        else:
            instance = get_class(xml.tag)(master, **get_attributes(xml.attrib, None))
            if isinstance(master, tk.PanedWindow):
                master.add(instance)
            elif not isinstance(instance, tk.Menu) and master is not None:
                instance.pack(**get_attributes(xml.attrib, 'pack'))
            for child in xml.getchildren():
                c = self._materialize(child, instance)
            if isinstance(instance, tk.Menu) and isinstance(master, tk.Menu):
                master.add_cascade(menu=instance, **get_attributes(xml.attrib, 'cascade'))
            elif isinstance(instance, tk.Menu):
                master.config(menu=instance)
            return instance

    def set_layout(self, xml):
        '''
        materialize the layout from xml
        '''
        self.root = self._materialize(et.fromstring(open(xml).read().strip()))

    def set_menu(self, xml):
        '''
        materialize a menu from xml and bind commands to app instance methods
        '''
        menu = self._materialize(et.fromstring(open(xml).read().strip()), self.root)

    def run(self):
        '''
        start the main loop
        '''
        self.root.mainloop()


class BibjeevesApp(TkApp):
    '''
    this class represents the gui context of bibjeeves
    '''

    def __init__(self):
        '''
        constructor - initinalize layout
        '''
        super(BibjeevesApp, self).__init__()

        self.set_layout(join(dirname(__file__), 'main.xml'))
        self.set_menu(join(dirname(__file__), 'menu.xml'))

        # setup keybindings
        self.root.bind('<Control-q>', lambda _: self.root.quit())

    def on_import_document(self):
        '''
        invoked when import document is clicked
        '''
        raise NotImplementedError('todo')

    def on_close_document(self):
        '''
        invoked when close document is clicked
        '''
        raise NotImplementedError('todo')

    def on_find(self):
        '''
        invoked when find is clicked
        '''
        raise NotImplementedError('todo')

    def on_quit(self):
        '''
        invoked when quit is clicked
        '''
        self.root.quit()
