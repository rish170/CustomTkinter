from customtkinter import *

root = CTk()
set_appearance_mode("dark") #light,dark,system
set_default_color_theme("green")
stat = "D"
root.title("App")
root.geometry("600x350")

def entry_op():
    op_str = "Hello " + entry.get()
    label = CTkLabel(root, text=op_str)
    entry.configure(state=DISABLED)
    label.pack()

def clear_entry():
    entry.configure(state=NORMAL)
    entry.delete(0, END)


entry = CTkEntry(root,
                 placeholder_text="Enter Your Name",
                 corner_radius=30,
                 text_color="blue",
                 placeholder_text_color="darkblue",
                 fg_color=("light blue", "grey"), # lighttheme, darktheme
                 state=NORMAL) 


submit_b = CTkButton(root, text="Submit", command=entry_op)
clear_b = CTkButton(root, text="Clear", command=clear_entry)

entry.pack(pady=30)
submit_b.pack(pady=1)
clear_b.pack(pady=15)

root.mainloop()