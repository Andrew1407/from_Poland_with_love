from Interpreter import PolishNotation
from WindowIOI import WindowIOI
from os import system
import pyperclip

class ConsoleIOI:
  __interpreter = PolishNotation()
  __commands = {
    "exit": [".q", ".exit", ".quit", ".ex"],
    "help": [".h", ".help"],
    "interprete to Polish notation": [".tp", ".toPolish"],
    "interprete from Polish notation": [".fp", ".fromPolish"],
    "paste example from clipboard": [".c", ".p", ".cp"],
    "clear": [".cl", ".clr", ".cls", ".clear"],
    "window mode": [".w", ".wnd", ".window"]
  }

  def launch(self):
    self.__mode = "toPolish"
    print("Default interpretation: to Polish notation")
    print("Help (commands): .h (.help)")
    self.__mainLoop()


  def __mainLoop(self):
    while True:
      _input = input("Enter a case/command: ")
      if self.__isExitOption(_input):
        return
      if self.__isWindowMode(_input):
        continue
      if self.__showHelpList(_input):
        continue
      if self.__setMode(_input):
        continue
      if self.__clear(_input):
        continue
      if self.__clipboardPaste(_input):
        continue
      self.__calculate(_input)


  def __findCommand(self, _input, command):
    return _input in self.__commands[command]

      
  def __isWindowMode(self, _input):
    if not self.__findCommand(_input, "window mode"):
      return False
    WindowIOI().launch()
    return True


  def __isExitOption(self, _input):
    return self.__findCommand(_input, "exit")


  def __showHelpList(self, _input):
    if not self.__findCommand(_input, "help"):
      return False
    print("\nCommands:")
    for x in self.__commands:
      print(f"{x}: {', '.join(self.__commands[x])}")
    print()
    return True


  def __setMode(self, _input):
    if self.__findCommand(_input, "interprete to Polish notation"):
      self.__mode = "toPolish"
      print("Mode's switched: to Polish")
      return True
    elif self.__findCommand(_input, "interprete from Polish notation"):
      self.__mode = "fromPolish"
      print("Mode's switched: from Polish")
      return True


  def __calculate(self, _input):
    interpreter = self.__interpreter
    result = interpreter.interpret(_input, self.__mode)
    pyperclip.copy(result)
    print("###############")
    print("Output result: ", result)
    print("###############")


  def __clear(self, _input):
    if not self.__findCommand(_input, "clear"):
      return False
    system("clear")
    return True


  def  __clipboardPaste(self, _input):
    if not self.__findCommand(_input, "paste example from clipboard"):
      return False
    example = pyperclip.paste()
    self.__calculate(example)
    return True
