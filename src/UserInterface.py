from HillCipher import HillCipher
import tkinter as tk
from tkinter import *

'''
bugs

* encode/decode button should be disabled unless there is more than one character in the entry. Use entry.validate()
  to set state of buttons to tk.ACTIVE / tk.DISABLED
  
* need more padding around button text

* it lets you enter non ascii lower case.  in this case encoding cannot be reversed with decoding

* add label to say wether result is decoded or encoded text
 
'''


class UserInterface:
    def __init__(self, parent):

        self.minlength = 2

        self.parent = parent

        self.entryLabel = Label(parent, text="Type in a word, click on the option you want and the Hill Cipher will do the rest :", font = ("Courier",15))
        self.entryLabel.pack(anchor=CENTER)

        validator = parent.register(self.validate)
        self.entry = Entry(parent, bd=5, validatecommand=(validator, '%P', '%S', '%d'), validate='key')
        self.entry.pack(anchor=CENTER)

        self.encodeButton = tk.Button(parent, text ="Encode", font = ("Courier",20) , relief = RIDGE,  command = self.encodeButton, state = DISABLED)
        self.encodeButton.place(relx=0.2, rely=0.35, anchor=CENTER)
        self.encodeButton.config(width = 6)

        self.decodeButton = tk.Button(parent, text = "Decode", font = ("Courier",20) ,relief = RIDGE, command = self.decodeButton, state = DISABLED)
        self.decodeButton.place(relx=0.8, rely=0.35, anchor=CENTER)
        self.decodeButton.config(width = 6)

        self.exitButton = tk.Button(parent, text ="Exit",  font = ("Courier",20) ,relief = RIDGE,  command = self.exit)
        self.exitButton.pack(side = BOTTOM)

        self.infoButton = tk.Button(parent, text = "INFO", command = self.info, font = ("Courier",15))
        self.infoButton.place(relx=0.07, rely=0.85, anchor=CENTER)

        self.resultEn = StringVar()
        self.resultLabelEn = tk.Label(master=window, textvariable=self.resultEn, anchor=CENTER)
        self.resultLabelEn.config(font = ("Courier",25))
        self.resultLabelEn.pack()

        self.resultDe = StringVar()
        self.resultLabelDe = tk.Label(master=window, textvariable=self.resultDe, anchor=CENTER)
        self.resultLabelDe.config(font=("Courier", 25))
        self.resultLabelDe.pack()

        self.cipher = HillCipher()

    def encodeButton(self):
        resultEn = self.cipher.encode(self.entry.get())
        self.resultEn.set("Encoded word :" + resultEn)

    def decodeButton(self):
        resultDe = self.cipher.decode(self.entry.get())
        self.resultDe.set("Decoded word :" + resultDe)

    def exit(self):
        self.parent.destroy()

    def info(self):
        infoWindow = tk.Tk()
        frame = Frame(infoWindow)
        infoWindow.title("What is the Hill Cipher ?")
        T = Text(infoWindow)
        T.pack()
        T.insert(END,"In classical cryptography, the Hill cipher is a polygraphic substitution cipher based on linear algebra. Invented by Lester S. Hill in 1929, it was the first polygraphic cipher in which it was practical (though barely) to operate on more than three symbols at once.")
        infoWindow.geometry("5500x70")
        infoWindow.mainloop()

    def validate(self, value, char, action):
        print("entered: ", value)
        print("length: ", len(value))
        if len(value) >= self.minlength:
            self.encodeButton.config(state=ACTIVE)
            self.decodeButton.config(state=ACTIVE)
        else:
            self.encodeButton.config(state=DISABLED)
            self.decodeButton.config(state=DISABLED)

        if action == 0:
            return True
        elif self.cipher.isValidCharacter(char):
            return True
        else:
            return False




window = tk.Tk()

frame = Frame(window)
frame.pack()

# naming the window
window.title("Hill Cipher")
window.geometry("780x150")

UserInterface(window)

window.mainloop()




