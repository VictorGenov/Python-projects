import tkinter as tk
import random as rd

secret_number = (rd.randint(1,100))
atems = 7
def guess(event):
    global atems
    number = entry.get()
    if number == "":
        label["text"] = ("Type a number pls or I will be in you nightmares")
    else:
        number = int(number)
        if atems > 0:
            atems -= 1 
            label_atems["text"] = text=f"Number of attempts: {atems}"
            if number == secret_number:
                label["text"] = ("Congrats I will not be in your nightmares!")
                reseat_buton.configure(state=tk.NORMAL)
                cheak_buton.configure(state=tk.DISABLED)
            if number < secret_number:
                label["text"] = ("The secreat number is greater than yours")
            if number > secret_number:
                label["text"] = ("The screat number is leser than yours")
                
            entry.delete(0,"end")
        else:
            label["text"] = ("Get redy for the worst bed time in your life.")

def play_again():
    global atems,secret_number
    secret_number = (rd.randint(1,100)) 
    atems = 7
    label_atems["text"] = (f"Number of atems: {atems}")
    label["text"] = ("Guse the number from 1 to 100")
    entry.delete(0,"end")
    reseat_buton.configure(state=tk.DISABLED)
    cheak_buton.configure(state=tk.NORMAL) 
     
    
window = tk.Tk()
window.geometry("300x150")
window.title("Guse the number")

label = tk.Label(window,text="Guse the number from 1 to 100.")
label.place(x=30,y=0)
label_atems = tk.Label(window,text="Number of attempts:")
label_atems.place(x=30,y=30)
entry = tk.Entry(window,bg="red")
entry.place(x=30,y=50)
entry.focus_set()
cheak_buton = tk.Button(window,text="Check",width=17,command=lambda e="<Return>":
guess(e))
cheak_buton.place(x=30,y=80)
reseat_buton = tk.Button(window,text="Play again",width=17,command=play_again,state=tk.DISABLED)
reseat_buton.place(x=30,y=110)
window.bind("<Return>",guess)







window.mainloop()
