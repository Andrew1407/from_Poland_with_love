from Interpreter import PolishNotation
from WindowIOI import WindowIOI

class ConsoleIOI:
  __commands = {
    "exit": [".q", ".exit", ".quit", ".ex"],
    "help": [".h", ".help"],
    "interprete to Polish notation": [".tp", ".toPolish"],
    "interprete from Polish notation": [".fp", ".fromPolish"],
    "open window mode": [".wnd", ".w", ".window"]
  }

  def launch(self):
    self.__mode = "toPolish"
    print("Default interpretation: to Polish notation")
    print("Help (commands): .h")
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
      self.__calculate(_input)


  def __findCommand(self, _input, command):
    return _input in self.__commands[command]

      
  def __isWindowMode(self, _input):
    if not self.__findCommand(_input, "open window mode"):
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
    result = PolishNotation(_input, self.__mode)
    print("###############")
    print("Output result: ", result)
    print("###############")
