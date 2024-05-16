from tkinter import *
from wordgenerator import word_generator

def generate(min, max, num, count, window):
    if min in ["", 0] or max in ["", 0] or num in ["", 0] or count in ["",0]:
        return
    list = word_generator(min,max,count,num)
    str1 = ""
    for word in list: 
        str1 += word + "\n"
    text = Text(window)
    text.insert(END, str1)
    text.grid(row=8,column=2)


window = Tk()
window.resizable(False,False)
window.title("Word Generator")

Label(window, text="Minimum Word Length").grid(row=0)
Label(window, text="Maximum Word Length").grid(row=1)
Label(window, text="Number of Word Terminators").grid(row=2)
Label(window, text="Number of Words").grid(row=3)
e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e1.grid(row=0, column=3)
e2.grid(row=1, column=3)
e3.grid(row=2, column=3)
e4.grid(row=3, column=3)
button = Button(window, text="Generate", command=lambda: generate(e1.get(), e2.get(), e3.get(), e4.get(),window))
button.grid(row=4, column=3)
Label(window, text="Words:").grid(row=7, column=2)


window.mainloop()