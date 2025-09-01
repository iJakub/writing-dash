#iJ

import tkinter as tk
from tkinter import PhotoImage
from idlelib.tooltip import Hovertip
import pyperclip


root = tk.Tk()
root.title('Dashes')

#Configuration
examples_file = "examples_en.txt"
always_on_top = True
background_color = "#191919"
widget_color = "#393939"
button_size = 80
window_size_x = 5 + (button_size+5)*3
window_size_y = 5 + (button_size+5)

if always_on_top == "True":
	root.attributes('-topmost', True)
else:
	root.attributes('-topmost', False)
root.update()

root.geometry(f"{window_size_x}x{window_size_y}")
root.minsize(window_size_x, window_size_y)
root.maxsize(window_size_x, window_size_y)

root.configure(bg=background_color)

examples = []
with open(examples_file, 'r', encoding='utf-8') as file:
    for example in file:
        example = example.replace('\\n', '\n')
        examples.append(example.strip())
print(examples)

def copy(text):
    pyperclip.copy(text)

em_dash = tk.Button(root, text='—', font='Helvetica 18 bold', command=lambda: copy(em_dash.cget('text')), bg=widget_color, fg="white")
em_dash.place(x=5, y=5, width=button_size, height=button_size)
em_dash_examples = Hovertip(em_dash,str(examples[0]), hover_delay=200)

en_dash = tk.Button(root, text='–', font='Helvetica 18 bold', command=lambda: copy(en_dash.cget('text')), bg=widget_color, fg="white")
en_dash.place(x=5+button_size+5, y=5, width=button_size, height=button_size)
en_dash_examples = Hovertip(en_dash,examples[1], hover_delay=200)

hyphen = tk.Button(root, text='-', font='Helvetica 18 bold', command=lambda: copy(hyphen.cget('text')), bg=widget_color, fg="white")
hyphen.place(x=5+button_size*2+10, y=5, width=button_size, height=button_size)
hyphen_examples = Hovertip(hyphen,examples[2], hover_delay=200)

root.mainloop()