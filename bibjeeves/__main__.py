
'''
This is the entry point of bibjeeves.
'''

from bibjeeves.config import update_cache
from bibjeeves.gui.app import BibjeevesApp


def main():
    '''
    This is bibjeeves main function.
    '''
    # produce the app object
    app = BibjeevesApp()

    # start and block until the gui terminates
    app.run()

    # if the cache has changed, write it back to disk.
    update_cache()


if __name__ == '__main__':
    main()
