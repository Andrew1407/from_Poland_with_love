from tkinter import *
from Interpreter import PolishNotation

class WindowIOI:
  __interpreter = PolishNotation()

  def launch(self):
    self.__root = Tk()
    self.__root.resizable(False, False)
    self.__root.title("FROM POLAND WITH LOVE")
    self.__root.geometry("1000x250+400+300")
    self.__root.config(bg = "black")
    #fill GUI
    self.__swithModesMenu()
    self.__inputLabel()
    self.__inputField()
    self.__outputLabel()
    self.__outputBtn()
    #launch loop
    self.__root.mainloop()


  def __swithModesMenu(self):
    modes = ["toPolish", "fromPolish"]
    self.__variable = StringVar(self.__root)
    self.__variable.set(modes[0])
    opt = OptionMenu(self.__root, self.__variable, *modes)
    opt.config(width=60, font=('arial', 20), bg = "black", fg="aqua")
    opt.grid(padx=40, pady=40)
    opt.place(relx=.9, rely=.2, anchor="c")
    opt.config(height=1, width=9)


  def __inputLabel(self):
    label = Label(text = "Enter a case: ", font=("arial", 20), bg = "black", fg="aqua")
    label.place(relx=.1, rely=.2, anchor="c")   


  def __inputField(self):
    self.__message = StringVar()
    message_entry = Entry(textvariable=self.__message, font=("arial", 20), bg = "aqua")
    message_entry.place(relx=.4, rely=.2, anchor="c")


  def __outputLabel(self):
    self.__outResult = StringVar()
    outLabel = Label(font=("arial", 20), bg = "black", fg="aqua", textvariable=self.__outResult)
    outLabel.place(relx=.0, rely=.8, anchor="sw")


  def __outputBtn(self):
    convertBtn = Button(text="Interpret", bg="black", fg="aqua", font=("arial", 20), command=self.__onClick)
    convertBtn.place(relx=.7, rely=.2, anchor="c")
    convertBtn.config(height=1, width=7)

  #button callback
  def __onClick(self):
    #calculating result
    interpreter = self.__interpreter
    result = interpreter.interpret(self.__message.get(), self.__variable.get())
    self.__outResult.set(f"  Output result:\t{result}")
