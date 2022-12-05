from tkinter import *

root = Tk()
# Title of the game
root.title("Bounce")
root.geometry("500x670")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
# The cover image of the game.
coverImage = PhotoImage(file = "images/atari.png")
# Background colour.
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="black")
canvas.pack(padx=10, pady=10)
canvas.create_image( -90, 30, image = coverImage, anchor = "nw")
file1 = open("highscore.txt","r+")
highscore = str(file1.read())
file1.close()
score = Label(height=50, width=80, text="Score: 00\n\n Highscore: " + highscore, font="Consolas 14 bold")
score.pack(side="right")
root.update()