import tkinter as tk
import tkinter.messagebox as tkm
import random

window = tk.Tk()
window.geometry("300x200")
window.title("Guess the word")
window.configure(bg = "#4b7f13")
with open ("words_en.txt") as file:
    data = file.read()
words = data.split()

secret_word = (random.choice(words))
letters =[]

def new_game():
    global secret_word
    global letters
    letters = []
    secret_word = (random.choice(words))
    lable_word["text"] = ("Here will be the word",)
    





def check_letter():
    letter = (entry_letre.get())
    letters.append(letter)
    print(letter)
    show_word = ""
    for char in secret_word:
        if char in letters:
            show_word += char
        else:
            show_word += "*"       
    entry_letre.delete(0,"end")
    lable_word["text"] = show_word
    if show_word == secret_word:
            tkm.showinfo(title="You win",message="You win congragelation you win nothing.")
            new_game()
lable_word = tk.Label(window,text="Here will be word",font=("Arial Black",15),bg="red")
lable_word.place(x=70,y=20)

entry_letre = tk.Entry(window,width=8,font=("Impact",10),bg="blue")
entry_letre.place(x=130,y=80)

entry_buton = tk.Button(window,text="Check the letter",bg="brown",command=check_letter)
entry_buton.place(x=100,y=120)












































window.mainloop()
