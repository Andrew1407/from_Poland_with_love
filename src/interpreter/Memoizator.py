import re

isOperation = lambda x: re.match(r"^[-/\*\^\+)(]{1}$", x)
isOperationEscaped = lambda x: re.match(r"^(-|/|\\\*|\\\^|\\\+|\+|\^|\*)$", x)
mapperStr = lambda arr: [x if isOperation(x) else "{}" for x in arr]
mapperRegex = lambda arr: [f"\{x}" if re.match(r"[)(\*\^\+]", x) else x for x in arr]
filtrator = lambda x: not isOperation(x)
filterValues = lambda arr: list(filter(filtrator, arr))

class Memoizator:
  __patternsMemoized = dict(
    toPolish = dict(),
    fromPolish = dict()
  )

  ## searches appropriate value in { __patternsMemoized }
  def memoized(self, inputStr, inputList, interpretation):
    inputListValues = filterValues(inputList)
    patterns = self.__patternsMemoized[interpretation]
    for reg in patterns:
      if re.match(reg, inputStr):
        pattern = patterns[reg]
        return pattern.format(*inputListValues) #+ "\t\tⓜ"
    return None


  ## inserts new patterns of input and result into { __patternsMemoized }
  def addExpression(self, _input, _result, interpretation):
    valuesQuantity = self.__countValues(_input)
    valuesRegex = [r"(\(?-\w+\)?|\w+)" for x in range(valuesQuantity)]
    (inputStr, inputRegex) = self.__generateKeyValue(_input, valuesRegex)
    (resultStr, resultRegex) = self.__generateKeyValue(_result, valuesRegex)
    patternsInput = self.__patternsMemoized[interpretation]
    interpretationInverted = self.__interpretationInverted(interpretation)
    patternsRes = self.__patternsMemoized[interpretationInverted]
    patternsInput[f"^{inputRegex}$"] = self.__join(resultStr)
    patternsRes[f"^{resultRegex}$"] = self.__join(inputStr)


  ## join array elements formating them
  def __join(self, arr):
    if not ("\\(" in arr or "(" in arr):
      return " ".join(arr)
    result = list()
    for x in arr:
      if isOperationEscaped(x):
        result += [" ", x, " "]
      else:
        result.append(x)
    return "".join(result)

  
  ## counts quantity of values in example
  def __countValues(self, arr):
    counter = 0
    for x in arr:
      if not isOperation(x):
        counter += 1
    return counter

  ## returns tuple of key and value of { val } for { __patternsMemoized }
  def __generateKeyValue(self, val, valuesRegex):
    valStr = mapperStr(val)
    valRegex = self.__join(mapperRegex(valStr)).format(*valuesRegex)
    return (valStr, valRegex)


  ## inverts mode of interpretation
  def __interpretationInverted(self, interpretation):
    if interpretation == "toPolish":
      return "fromPolish"
    elif interpretation == "fromPolish":
      return "toPolish"
    else:
      raise Exception("Bad interpretation set")
