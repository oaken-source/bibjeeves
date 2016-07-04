
'''
This is the entry point of bibjeeves.
'''

import tkinter as Tk

from bibjeeves.config import update_cache
from bibjeeves.gui import App
from bibjeeves.providers import CiteSeerxProvider


def main():
    '''
    This is bibjeeves main function.
    '''
    # produce the app object
    root = Tk.Tk()
    app = App(root)

    # start the main loop
    root.mainloop()

    # if the cache has changed, write it back to disk.
    update_cache()


if __name__ == '__main__':
    main()
