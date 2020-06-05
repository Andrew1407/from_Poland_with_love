from Memoizator import Memoizator

operationsPriorities = {
  "(": 0,
  "+": 1,
  "-": 1,
  "*": 2,
  "/": 2,
  "^": 3
}

class PolishNotation:
  # [CONTRUCTOR]
  def __init__(self):
    self.__memoizator = Memoizator()
    self.__result = list()
    self.__operationsStack = list()
    self.__inputList = list()

  
  # [INTERPRETATION]
  def interpret(self, inputStr, interpretation = "toPolish"):
    self.__set_inputList(inputStr, interpretation)
    memoized = self.__memoizator.memoized(inputStr, self.__inputList)
    if memoized:
      return memoized
    self.__calculate(interpretation)
    valuesQuantity = len(self.__inputList) - len(self.__operationsStack)
    self.__memoizator.addExpression(self.__inputList, self.__result, valuesQuantity)
    return self.__getResult()


  ## applies appropriate input decomposition
  def __set_inputList(self, inputStr, interpretation):
    self.__cleanLists()
    if interpretation == "toPolish":
      self.__set_inputList_toPolish(inputStr)
    elif interpretation == "fromPolish":
      self.__set_inputList_fromPolish(inputStr)


  ## main calculations
  def __calculate(self, interpretation):
    if interpretation == "toPolish":
      self.__toPolishNotation()
    elif interpretation == "fromPolish":
      self.__fromPolishNotation()
      self.__result = self.__result[0].split(" ")


  ## fills { __inputList } decomposing {inputStr}
  def __set_inputList_toPolish(self, inputStr):
    inputList = inputStr.split(" ")
    # print(inputList)
    for x in inputList:
      if "(" in x or ")" in x:
        if self.__hasMinus(x):
          x = x[1 : -1]
          if not ("(" in x or ")" in x):
            self.__inputList.append(x)
            continue

        x_list1 = list()
        x_list2 = list()
        while "(" in x:
          x_list1.append("(")
          x = x[1 :]
        while ")" in x:
          x_list2.append(")")
          x = x[: -1]

        self.__inputList += [*x_list1, x, *x_list2]
      else:
        self.__inputList.append(x)


  ## fills {__inputList} splitting {inputStr} 
  def __set_inputList_fromPolish(self, inputStr):
    self.__inputList = inputStr.split(" ")
    

  ## operaion defining
  def __isOperation(self, x):
    for operation in operationsPriorities:
      if x == operation: return True
    return False

  ## checks oprerand for minus value
  def __hasMinus(self, operand):
    if not ("-" in operand):
      return False
    if operand.index("-") < 2:
      return True
    return False


  ## checks operand for operation presence
  def __hasOperation(self, operand):
    for x in operand:
      if self.__hasMinus(operand):
        continue
      if self.__isOperation(x):
        return True
    return False


  ## stacks cleanig
  def __cleanLists(self):
    self.__result = list()
    self.__operationsStack = list()
    self.__inputList = list() 


  ## needs to push operations in the stack
  ## in brackets scope
  def __checkPriority(self, x):
    #if the stack list is empty
    if not self.__operationsStack:
      return
    prevOperation = self.__operationsStack[-1]
    prevOperationPriority = operationsPriorities[prevOperation]
    x_Priority = operationsPriorities[x]
    if prevOperationPriority >= x_Priority and \
      x_Priority in [1, 2]:
      self.__result.append(prevOperation)
      self.__operationsStack.pop(-1)

  ## generates string and pushes it into {__result}
  def __pushResult(self, op1, op2):
    opt = self.__operationsStack[-1]
    if len(self.__operationsStack) < 2:
      self.__result.append(" ".join([op1, opt, op2]))
      return
    optPrev = self.__operationsStack[-2]
    optPriority = operationsPriorities[opt]
    optPriorityPrev = operationsPriorities[optPrev]
    #brackets wrapping
    if optPriority > optPriorityPrev:
      if self.__hasOperation(op2):
        op2 = f"({op2})"
      else:
        op1 = f"({op1})"
    elif optPriority == 3 and \
      optPriorityPrev == 3:
      if self.__hasOperation(op2):
        op2 = f"({op2})"
      else:
        op1 = f"({op1})"

    self.__result.append(" ".join([op1, opt, op2]))


  ## pop from the stack all the operands
  ## in {__operationsStack} in brackets
  def __closedBracket(self):
    index = -1
    while True:
      operation = self.__operationsStack[index]
      if operation == "(":
        break
      index -= 1

    #lists data updating
    valuesFromStack = self.__operationsStack[index + 1 :]
    valuesFromStack.reverse()
    self.__result += valuesFromStack
    self.__operationsStack = self.__operationsStack[: index]


  # [POLISH NOTATION]
  ## converts to Polish format
  def __toPolishNotation(self):
    for x in self.__inputList:
      if self.__isOperation(x):
        self.__checkPriority(x)
        self.__operationsStack.append(x)
      elif x == ")":
        self.__closedBracket()
      else:
        self.__result.append(x)

    if len(self.__operationsStack) > 1:
      self.__operationsStack.reverse()

    #final result
    self.__result += self.__operationsStack
    while "(" in self.__result:
      self.__result.remove("(")


  ## converts from Polish format
  def __fromPolishNotation(self):
    for x in self.__inputList:
      if self.__isOperation(x):
        self.__operationsStack.append(x)
        op2 = self.__result.pop(-1)
        op1 = self.__result.pop(-1)
        self.__pushResult(op1, op2)
      else:
        self.__result.append(x)


  # [FINAL RESULT GETTER]
  def __getResult(self):
    result = " ".join(self.__result)
    return result
