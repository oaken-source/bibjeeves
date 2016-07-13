
'''
This module provides the graphical user interface of bibjeeves.
'''

from tkapp import TkApp


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

        # setup keybindings
        self.root.bind('<Control-q>', lambda _: self.root.quit())

        self.materialize()

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
