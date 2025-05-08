from wordgenerator import word_generator
from tkinter import *
from tkinter import messagebox
import time

wordlist = ""
timestart = ""
def generate(min, max, num, count, text):
    global wordlist, timestart
    wordlist = ""
    text.configure(state='normal')
    text.delete("1.0", END)
    if min in ["", 0] or max in ["", 0] or num in ["", 0] or count in ["",0]:
        return
    list = word_generator(min,max,count,num)
    for word in list: 
        wordlist += word + " "
    text.insert(END, wordlist)
    text.configure(state='disabled')
    timestart = time.time()

def check(given, text, textvar):
    global wordlist, timestart
    currword = ""
    for letter in wordlist:
        if letter != ' ':
            currword += letter
        else:
            break
    if currword.lower() == given.get().lower():
        wordlist = wordlist[len(currword) + 1:]
        text.configure(state='normal')
        text.delete('1.0', '1.0 + ' + str(len(currword) + 1) + ' chars')
        text.configure(state='disabled')
        textvar.set('')
        if wordlist == '':
            length = time.time() - timestart
            wpm = 15 / (length / 60)
            messagebox.showinfo("WPM", f"That took you {length} seconds. Your WPM is {int(wpm)}.") 
        return "break"
    

window = Tk()
window.resizable(False,False)
window.title("Type Game")
window.geometry('500x200')
text = Text(window, wrap=WORD, height=6, width=50)
text.pack()
button = Button(window, text="Start", command=lambda: generate(3, 5, 4, 15, text))
button.pack(side=BOTTOM)
textvar = StringVar()
enter = Entry(window, textvariable=textvar)
enter.bind("<space>", (lambda event: check(enter, text, textvar)))
enter.bind("<Return>", (lambda event: check(enter, text, textvar)))
enter.focus_set()
enter.pack(side=BOTTOM)

window.mainloop()
