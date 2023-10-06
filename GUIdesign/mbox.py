from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# Main App Icon
root.iconbitmap('images/codemy.ico')
# Message Box Icon
root.iconbitmap(default='images/codemy.ico')
root.geometry('700x350')

def clicker():
    # Create a dialog
    # yesno, ok, okcancel, show_info, show_error, show_question,
    # show_warning, yesnocancel, retrycancel
    mb = Messagebox.yesno("Display Some Message Here", "Here is the Title")
    
    # Display button click
    my_label.config(text=f'You clicked {mb}')

my_button = tb.Button(root, text="Click Me!", bootstyle='danger', command=clicker)
my_button.pack(pady=40)

my_label = tb.Label(root, text='', font=("Helvetica", 18))
my_label.pack(pady=20)

root.mainloop()