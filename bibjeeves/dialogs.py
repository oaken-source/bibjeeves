
'''
This module provides the dialogs used by bibjeeves.
'''

from os.path import join, dirname

from tkapp import TkDialog


class DocumentImportDialog(TkDialog):
    '''
    a dialog to produce documents from user input
    '''

    def __init__(self):
        '''
        constructor - position the dialog
        '''
        super(DocumentImportDialog, self).__init__()

        self.set_layout(join(dirname(__file__), 'gui/import_dialog.xml'))
