from tkinter import *

From PIL import ImageTk, Image
root=Tk()

root.title(“Dice Game")
root.geometry("600x400")

root.configure(background = "hotpink1")
img = ImageTk.PhotoImage(Imaage.open (dice1.1.jpg))

player1 = Label(root, text = "Player 1", bg = "deep sky blue", fg = "DarkSlateGray1")
player1.place(relx = 0.1, rely = 0.3 , anchor =  CENTER)

player2 = Label(root, text = "Player 2", bg = "DarkOrchid3", fg = "deep pink")
player2.place(relx = 0.9, rely = 0.3 , anchor =  CENTER)

player_!_score_label = Label(root , bg = "firebrick2", fg = "red")
player_!_score_label.place(relx = 0.1, rely = 0.4 , anchor = CENTER)

player_2_score_label = Label(root , bg = "magenta4", fg = "purple1")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor = CENTER)

random_dice_label = Label(root , bg = "choclate3", fg = "goldenrod3")
random_dice_label.place(relx = 0.5, rely = 0.5 , anchor = CENTER)

root.mainloop()
Dilean
