
'''
This is the entry point of bibjeeves.
'''

from tkinter import Tk

from bibjeeves.config import update_cache
from bibjeeves.gui import App
from bibjeeves.providers import CiteSeerxProvider


def main():
    '''
    This is bibjeeves main function.
    '''
    root = Tk()
    app = App(root)

    root.mainloop()

    update_cache()


if __name__ == '__main__':
    main()
