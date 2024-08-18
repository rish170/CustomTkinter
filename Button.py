from customtkinter import *

root = CTk()
set_appearance_mode("dark") #light,dark,system
set_default_color_theme("green")
stat = "D"
root.title("App")
root.geometry("600x350")

def theme_toggle():
    global stat
    if stat == "D":
        stat = "L"
        set_appearance_mode("light")
    else:
        stat="D"
        set_appearance_mode("dark")


button = CTkButton(root,
                   text="click",
                   command=theme_toggle,
                   width=10,
                   height=10,
                   font=('Helvetica', 15),
                   text_color="black",
                   fg_color="powder blue",
                   hover_color='light green',
                   corner_radius=5,
                   border_width=5,
                   border_spacing=10,
                   border_color='blue',) # Disabled/normal


button.pack(pady=50)

root.mainloop()