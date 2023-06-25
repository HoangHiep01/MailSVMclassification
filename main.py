from tkinter import *
import tkinter as tk
from tkinter import filedialog
from Mail_classification import MailClassification

engine = MailClassification()

def readFile(filedir):
	if ".txt" in filedir:
		with open(filedir, 'r') as file:
			message = file.read()
		return message
	else:
		 messageBox("Erorr", False)

def displayOnTextInput(message):
	textInput.delete(0.0, END)
	textInput.insert(0.0, message)
	engine.set_mail(message)

def displayOnTextLabel(message):
	textLabel.configure(text= f"{message}")
	textLabel.text = f"{message}"

def openFile():
	root.filedir = filedialog.askopenfilename(	initialdir="../test/", 
												title="Choose File", 
												filetypes=(("All Files","*.*"),("text","*.txt"))
											)
	message = "Erorr!"
	message = readFile(root.filedir)
	displayOnTextInput(message)


def classificationMail():
	engine.set_mail(textInput.get(1.0,END))
	result = engine.clasification_email()
	displayOnTextLabel(result)

root = Tk()
# root.iconbitmap("../icon/logo.ico")
root.title("Spam mail classification")
root.geometry("1250x500")

frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)


textInput = Text(root, width=100, height=50)

textLabel = Label(frame, text="Select or text Mail")
chooseMailBtn = Button(frame, text="Select file", command=openFile)
classificationBtn = Button(frame, text="Classification", command=classificationMail)
exitBtn = Button(frame, text="Exit", command=root.quit)


textInput.pack(side=TOP, ipadx=5, ipady=5)

textLabel.pack(side=TOP, ipadx=5, ipady=5)
chooseMailBtn.pack(side=tk.LEFT, padx= 10)
classificationBtn.pack(side=tk.LEFT, padx= 10)
exitBtn.pack(side=tk.LEFT, padx= 10)

root.mainloop()