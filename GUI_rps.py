from tkinter import *
import random


class UI:

    def __init__(self, master):
        top = Frame(master, width=140, height=100)
        top.grid_propagate(0)
        bot = Frame(master)
        top.pack()
        bot.pack()

        label1 = Label(top, text="Lets Play!", )
        label1.place(x=70, y=50, anchor="center")

        rock = Button(bot, text="Rock", width=20, command=lambda: play("Rock")).grid(row=1)
        paper = Button(bot, text="Paper", width=20, command=lambda: play("Paper")).grid(row=2)
        scissors = Button(bot, text="Scissors", width=20, command=lambda: play("Scissors")).grid(row=3)

        def play(val):
            lose = {"Scissors": "Rock", "Paper": "Scissors", "Rock": "Paper"}
            comp = random.choice(["Rock", "Scissors", "Paper"])

            if comp == val:
                label1.configure(text="You Drew!\nYou played:" + val + "\nComputer played: " + comp)
                top.config(bg="SystemButtonFace")
                label1.config(bg="SystemButtonFace")
            elif comp != lose[val]:
                label1.configure(text="You Won!\nYou played:" + val + "\nComputer played: " + comp)
                top.config(bg="green")
                label1.config(bg="green")
            elif comp == lose[val]:
                label1.configure(text="You Lost!\nYou played:" + val + "\nComputer played: " + comp)
                top.config(bg="red")
                label1.config(bg="red")

# Creates a blank window no ability to be resized
root = Tk()
root.resizable(width=False, height=False)
window = UI(root)

# runs the GUI in an infinite loop untill you close the window
root.mainloop()