from tkinter import *
from tkinter import scrolledtext, BOTH, ttk, END, StringVar
from random import choice

# window params
root = Tk()
root.title('Passgen')
root.geometry('350x350')

# symbols for password
symbols = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@<>'

# generating of password
def generating():
	num_value = int(symnum_entry.get()) #getting value of number of symbols
	return ''.join([choice(symbols) for i in range(num_value)])

# password output
def show():	
	console.configure(state='normal')  # enable insert
	console.insert(END, generating() + '\n')
	console.yview(END)  # autoscroll
	console.configure(state='disabled')  # disable editing	

# number of symbols label
symnum_lbl = Label(root, text = 'Number of symbols')
symnum_lbl.pack(side = 'top')

# number of symbols entry
symnum_entry = Entry(root, width = 15)
symnum_entry.pack(side = 'top')

# generating button
gen_button = Button(root, text = 'Generate', width = 10, height = 1, command = show)
gen_button.pack(side = 'top')

# top separator
ttk.Separator(root, orient=HORIZONTAL).pack(fill=BOTH)

# output field
console = scrolledtext.ScrolledText(root, height = 15, state = 'disable')
console.pack(side = 'top')

# down separator
ttk.Separator(root, orient=HORIZONTAL).pack(fill=BOTH)

root.mainloop()