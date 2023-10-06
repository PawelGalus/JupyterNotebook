from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

# Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Create a Scrollbar
my_scroll = tb.Scrollbar(my_frame, orient='vertical', bootstyle="danger round")
my_scroll.pack(side="right", fill='y')

# Create A Text Widget
my_text = Text(my_frame, width=30, height=25,
               yscrollcommand=my_scroll.set, wrap="none", font=("Helvetica", 18))
my_text.pack()

# Config the scrollbar
my_scroll.config(command=my_text.yview)

root.mainloop()