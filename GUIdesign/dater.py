from tkinter import *
from token import COMMA
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
root.iconbitmap('images/codemy.ico')
root.geometry('500x350')

def datey():
    # Grab the Date
    my_label.config(text=f"You picked: {my_date.entry.get()}")
    
def thing():
    cal = Querybox()
    my_label.config(text=f"You picked: {cal.get_date()}")

my_date = tb.DateEntry(root, bootstyle="danger", firstweekday=0, startdate=date(2023, 2, 14))
my_date.pack(pady=50)

my_button = tb.Button(root, text="Get Date", bootstyle="danger outline", command=datey)
my_button.pack(pady=20)

my_button2 = tb.Button(root, text="Get Calendar", bootstyle="success outline", command=thing)
my_button2.pack(pady=20)

my_label = tb.Label(root, text="You picked: ")
my_label.pack(pady=20)

root.mainloop()