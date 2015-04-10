# -*- coding: utf-8 -*-

##https://keijist.wordpress.com/2011/01/04/python-3-%E3%81%A7%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E9%96%8B%E3%81%8F%E3%83%80%E3%82%A4%E3%82%A2%E3%83%AD%E3%82%B0%E3%81%AE%E4%BD%9C%E6%88%90/
import tkinter
import tkinter.filedialog

import csv

tk = tkinter.Tk()

tk.withdraw()# 小ウィンドウを表示しないようにする。

inputargs = { "initialdir" : "c:/",
"filetypes" : [("すべてのファイル", "*.*")],
"title" : "INPUT file"
}
outputargs = { "initialdir" : "c:/",
"filetypes" : [("すべてのファイル", "*.*")],
"title" : "OUTPUT file"
}
inputfilename = tkinter.filedialog.askopenfilename(**inputargs)
print (inputfilename)
outputfilename = tkinter.filedialog.asksaveasfilename(**outputargs)
print (outputfilename)
outputfile = open(outputfilename, mode="w",encoding="cp932")

with open(inputfilename,"r",encoding="cp932") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if row[0]=="test":
            outputfile.write(row[1])
outputfile.close()
