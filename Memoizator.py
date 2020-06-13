import re

isOperation = lambda x: re.match(r"^[-/\*\^\+)(]{1}$", x)
mapperStr = lambda arr: [x if isOperation(x) else "{}" for x in arr]
mapperRegex = lambda arr: [f"\{x}" if re.match(r"[)(\*\^\+]", x) else x for x in arr]
filtrator = lambda x: not isOperation(x)
filterValues = lambda arr: list(filter(filtrator, arr))

class Memoizator:
  __patternsMemoized = dict()

  ## searches appropriate value in { __patternsMemoized }
  def memoized(self, inputStr, inputList):
    inputListValues = filterValues(inputList)
    for reg in self.__patternsMemoized:
      if re.match(reg, inputStr):
        pattern = self.__patternsMemoized[reg]
        return pattern.format(*inputListValues) #+ "\t\tⓜ"
    return None


  ## inserts new patterns of input and result into { __patternsMemoized }
  def addExpression(self, _input, _result):
    valuesQuantity = self.__countValues(_input)
    valuesRegex = ["\(?[-\w]+\)?" for x in range(valuesQuantity)]
    (inputStr, inputRegex) = self.__generateKeyValue(_input, valuesRegex)
    (resultStr, resultRegex) = self.__generateKeyValue(_result, valuesRegex)
    self.__patternsMemoized[f"^{inputRegex}$"] = self.__join(resultStr)
    self.__patternsMemoized[f"^{resultRegex}$"] = self.__join(inputStr)


  ## join array elements formating them
  def __join(self, arr):
    if not ("\\(" in arr or "(" in arr):
      return " ".join(arr)
    result = list()
    for x in arr:
      if re.match(r"^(-|/|\\\*|\\\^|\\\+|\+|\^|\*)$", x):
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
