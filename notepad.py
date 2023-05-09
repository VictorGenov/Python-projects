import tkinter as tk
import tkinter.filedialog as tkf
import tkinter.messagebox as tkm

window = tk.Tk()
window.title("NotePad")
window.geometry("300x300")
file_name = ""

def write_to_file(file_name):
    content = content_text.get(1.0,"end")
    with open(file_name,"w") as file:
        file.write(content)

def open_file():
    global file_name
    content_text.delete(1.0,"end")
    file_name = tkf.askopenfilename()
    with open(file_name) as file:
        content_text.insert(1.0,file.read())
    file_label["text"] = "File:" + file_name

def new_file():
    global file_name
    if tkm.askokcancel(title="Deliting",message="Are you sure? Unsaved text will be deleted."):
        file_name = ""
        content_text.delete(1.0,"end")
    file_label["text"]="File:" + file_name

def save_file():
    global file_name
    if file_name == "":
        save_as_file()
        tkm.showinfo(title="Saving",message="Saving file to:"+ file_name)
    else:
        write_to_file(file_name)

content_text = tk.Text(window,wrap="word",bg="red")
content_text.place(x=0,y=0,relwidth=1,relheight=1)

main_menu = tk.Menu(window)
window.configure(menu = main_menu)
file_menu = tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="File",menu=file_menu)

new_file_icon = tk.PhotoImage(file='new_file.gif')
open_file_icon = tk.PhotoImage(file='open_file.gif')
save_file_icon = tk.PhotoImage(file='save_file.gif')

file_menu.add_command(label="New",image = new_file_icon,compound="left",command=new_file)
file_menu.add_command(label="Open",image = open_file_icon,compound="left",command=new_file)
file_menu.add_command(label="Save",image = save_file_icon,compound="left",command=new_file)
file_menu.add_command(label="Save_as",image = save_file_icon,compound="left",command=new_file)

file_label = tk.Label(window,text='File:'+file_name)
file_label.place(relx=0,rely=1,anchor="sw")

window.mainloop()
