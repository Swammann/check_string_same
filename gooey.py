#
#
#

import tkinter as tk
from tkinter import filedialog, Text
import os
import sys

root = tk.Tk()
files = []


def addFile():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='C:/Users/smigg/PycharmProjects', title='Select File',
                                          filetypes=(('all files', '*.*'), ('text', '*.txt'), ('CSV', '*.csv')))

    if len(files) <= 1:
        files.append(filename)
        print(filename)
    else:
        files.clear()
        files.append(filename)
        print(filename)

    for file in files:
        label = tk.Label(frame, text=file, bg='gray')
        label.pack()

def checkSame():
    def readString(path_list, index):
        string = []
        in_string = None
        print()
        fname = path_list[index]
        with open(fname, 'r') as f:
            in_string = f.read()
            nstring = input('how many strings do you want to read: ')
            splitline = in_string.split(',')
            for i in range(int(nstring)):
                string.append(splitline[i])
            f.close()
        return string

    def spaceStrip(string_list):
        strip_list = []
        for line in string_list:
            strip = line.strip()
            strip_list.append(strip)
        return strip_list

    def checkString(string_1, string_2):
        same = None
        for i in range(len(string_1)):
            if string_1[i] == string_2[i]:
                same = 'These files contain matching strings'
            else:
                same = "These files don't contain any matching strings"
        print()
        return print(same)

    try:
        string1 = readString(files, 0)
        string2 = readString(files, 1)
        string1 = spaceStrip(string1)
        string2 = spaceStrip(string2)
        checkString(string1, string2)
    except (OSError, UnboundLocalError) as err:
        print('\n -- Error with file open -- \n')
        print(err)
        sys.exit(1)


window = tk.Canvas(root, height=300, width=500, bg='#00563f')
window.pack()

frame = tk.Frame(root, bg='#FFFFFF')
frame.place(relwidth=.8, relheight=0.8,
            relx=0.1, rely=0.1)

openFile = tk.Button(root, text='open file', padx=20, pady=5,
                     fg='#FFFFFF', bg='#00555f', command=addFile)
check = tk.Button(root, text='check strings', padx=20, pady=5,
                  fg='#FFFFFF', bg='#00555f', command=checkSame)
openFile.pack()
check.pack()

root.mainloop()
