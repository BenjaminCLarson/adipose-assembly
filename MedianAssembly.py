__author__ = 'blarson2'

# !/usr/local/bin/python

import tkinter


def main():
    main_window = tkinter.Tk()
    label = tkinter.Label(main_window, text='Hello World')

    label.pack(side='left')
    tkinter.mainloop()

if __name__ == "__main__":
    main()