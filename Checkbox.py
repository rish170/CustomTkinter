from customtkinter import *

root = CTk()
set_appearance_mode("dark") #light,dark,system
set_default_color_theme("green")
stat = "D"
root.title("App")
root.geometry("600x350")
check_var = StringVar(value="off") # Use check_var.get() to get value for on/off condition
text_var = StringVar(value="Play a Game")


def check_game():
    if check_var.get() == "on":
        onlabel = CTkLabel(root, text="Game ON")
        onlabel.pack()
        text_var.set("Awsome") 
    else:
        offlabel = CTkLabel(root, text="Game OFF")
        offlabel.pack()

    

def check_clear():
    check.deselect()
    text_var.set("play a Game")


check = CTkCheckBox(root,
                    text="play a Game?",
                    variable=check_var,
                    onvalue="on",
                    offvalue="off",
                    checkbox_width=60,
                    checkbox_height=35,
                    font=("Helvetica", 25),
                    corner_radius=55,
                    fg_color="red",
                    hover_color="maroon",
                    text_color="red",
                    hover=True,
                    textvariable=text_var)


check_b = CTkButton(root, text="Game", command=check_game)
checkclear = CTkButton(root, text="Check Clear", command=check_clear) # deselect
checktoggle = CTkButton(root, text="Check Toggle", command=check.toggle)
checkselect = CTkButton(root, text="Check Select", command=check.select)


check.pack(pady=25)
check_b.pack()
checkclear.pack()
checktoggle.pack()
checkselect.pack()

root.mainloop()