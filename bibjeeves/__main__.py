
'''
This is the entry point of bibjeeves.
'''

from tkinter import Tk

from bibjeeves.gui import App
from bibjeeves.providers import CiteSeerxProvider


def main():
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
