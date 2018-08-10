from tkinter import *

# Creates a blank window no ability to be resized
root = Tk()
root.resizable(width=False, height=False)

canvas = Canvas(root, width=140, height=100)
bot = Frame(root)
canvas.pack()
bot.pack()

rock = Button(bot, text = "Rock", width = 20)
paper = Button(bot, text = "Paper", width = 20)
scissors = Button(bot, text = "Scissors", width = 20)

rock.grid(row = 1)
paper.grid(row = 2)
scissors.grid(row = 3)

# runs the GUI in an infinite loop untill you close the window
root.mainloop()