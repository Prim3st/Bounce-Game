from tkinter import *
from __init__ import *
from ball import Ball
from paddle import Paddle
import time
import random

class Bricks:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 25, 25, fill=color, width=2)


playing = False


def start_game(event):
    global playing
    if playing is False:
        playing = True
        file1 = open("highscore.txt","r+")
        highscore = str(file1.read())
        file1.close()
        score.configure(text="Score: 00\n\nHighscore: " + highscore)
        canvas.delete("all")
        BALL_COLOR = ["red", "yellow", "green"]
        BRICK_COLOR = ["PeachPuff3", "dark slate gray", "rosy brown", "light goldenrod yellow", "turquoise3", "salmon",
                       "light steel blue", "dark khaki", "pale violet red", "orchid", "tan", "MistyRose2",
                       "DodgerBlue4", "wheat2", "RosyBrown2", "bisque3", "DarkSeaGreen1"]
        random.shuffle(BALL_COLOR)
        # Colour of the paddle
        paddle = Paddle(canvas, "blue")
        bricks = []
        for i in range(0, 5):
            b = []
            for j in range(0, 19):
                random.shuffle(BRICK_COLOR)
                tmp = Bricks(canvas, BRICK_COLOR[0])
                b.append(tmp)
            bricks.append(b)

        for i in range(0, 5):
            for j in range(0, 19):
                canvas.move(bricks[i][j].id, 25 * j, 25 * i)

        ball = Ball(canvas, BALL_COLOR[0], paddle, bricks, score)
        root.update_idletasks()
        root.update()

        time.sleep(1)
        while 1:
            if paddle.pausec !=1:
                try:
                    canvas.delete(m)
                    del m
                except:
                    pass
                if not ball.bottom_hit:
                    ball.draw()
                    paddle.draw()
                    root.update_idletasks()
                    root.update()
                    time.sleep(0.01)
                    if ball.hit==95:
                        # You won message and colour
                        canvas.create_text(250, 250, text="YOU WON !!", fill="yellow", font="Consolas 24 ")
                        root.update_idletasks()
                        root.update()
                        playing = False
                        break
                else:
                    # Game Over message and colour
                    file1 = open("highscore.txt","r+")
                    highscore = str(file1.read())
                    file1.close()
                    if highscore < str(ball.hit):
                        file1 = open("highscore.txt","w")
                        file1.write(str(ball.hit))
                        file1.close()
                    canvas.create_text(250, 250, text="GAME OVER!!\nYour score was: " + str(ball.hit), fill="red", font="Consolas 24 ")
                    root.update_idletasks()
                    root.update()
                    playing = False
                    break
            else:
                try:
                    if m==None:pass
                except:
                    # Pause message and colour
                    m=canvas.create_text(250, 250, text="Paused", fill="blue", font="Consolas 24 ")
                root.update_idletasks()
                root.update()

# Initial text in screen (x,y), and Start Button
root.bind_all("<Return>", start_game)
root.bind_all("<Left>", start_game)
root.bind_all("<Right>", start_game)
canvas.create_text(250, 250, text="Press button to start game!", fill="red", font="Consolas 18")
root.mainloop()
        