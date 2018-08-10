from tkinter import *
import random

root = Tk()
root.resizable(width=False, height=False)

top = Frame(root, width=140, height=100)
bot = Frame(root)
top.pack()
bot.pack()

def play(val):
    lose = {"s": "r", "p": "s", "r": "p"}
    comp = random.choice(["r", "s", "p"])

    #if comp == lose[val]:


# Creates a blank window no ability to be resized


rock = Button(bot, text = "Rock", width = 20, command = lambda: play('r'))
paper = Button(bot, text = "Paper", width = 20, command = lambda: play('p'))
scissors = Button(bot, text = "Scissors", width = 20, command = lambda: play('s'))

rock.grid(row = 1)
paper.grid(row = 2)
scissors.grid(row = 3)

# runs the GUI in an infinite loop untill you close the window
root.mainloop()