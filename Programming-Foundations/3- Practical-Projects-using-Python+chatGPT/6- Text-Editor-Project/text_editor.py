""" A script to create a simple text editor """

import tkinter as tk

root = tk.Tk()

Sava_As_butten = tk.Button(text="Sava As...", width=10, height=1, fg="black", bg="gray")

frame = tk.Frame(master=Sava_As_butten, borderwidth=5)
label = tk.Label(master=frame, text="Python rocks!", foreground="White", background="black")
label.pack()


Open_File_butten = tk.Button(text="Open File", width=10, height=1, fg="black", bg="gray")
Text_Box = tk.Text()
frame.pack(side=tk.LEFT)
# entry = tk.Entry()
Sava_As_butten.pack()
Open_File_butten.pack()
Text_Box.pack()
# entry.pack()

root.mainloop()
