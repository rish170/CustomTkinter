from customtkinter import *

root = CTk()
root.title("App")
root.geometry("700x400")

def color_pick(choice):
    # Combobox creates an event with a command and gives output from the selection in the GUI
    output_label.configure(text=choice, text_color=choice)

def color_pick2():
    # Using button to get the inputted value of combobox
    output_label.configure(text=combo_box.get(), text_color=combo_box.get())

def color_yellow():
    combo_box.set("Yellow")
    output_label.configure(text=combo_box.get(), text_color=combo_box.get())

label = CTkLabel(root, text="Pick a colour:", font=("", 20))

label.pack(pady=30)
color = ["Red", "Green", "Blue"]

combo_box = CTkComboBox(root,
                        values=color,
                        command=None, # Use color_picker instead of None to see event input
                        height=35,
                        width=200,
                        font=("", 30),
                        dropdown_font=("", 30),
                        corner_radius=50,
                        border_width=5,
                        dropdown_fg_color="red",
                        dropdown_hover_color="maroon",
                        dropdown_text_color="black",
                        fg_color="red",
                        button_hover_color="maroon",
                        text_color="black",
                        button_color="crimson",
                        border_color="crimson",
                        justify=CENTER,
                        state=NORMAL) 
combo_box.pack()

output_label = CTkLabel(root, text="", font=("", 25, "bold"))
output_label.pack(pady=20)

button = CTkButton(root, text="Pick a color", command=color_pick2)
button.pack(pady=20)

custom_button = CTkButton(root, text="Pick Yello", command=color_yellow)
custom_button.pack(pady=20)

root.mainloop()