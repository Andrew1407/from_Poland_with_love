import re

mapperStr = lambda arr: [x if re.match(r"^[-/\*\^\+)(]{1}$", x) else "{}" for x in arr]
mapperRegex = lambda arr: [f"\{x}" if re.match(r"[)(\*\^\+]", x) else x for x in arr]


class Memoizator:
  __patternsMemoized = dict()

  ## searches appropriate value in { __patternsMemoized }
  def memoized(self, inputStr, inputList):
    inputListValues = self.__filterValues(inputList)
    for reg in self.__patternsMemoized:
      if re.match(reg, inputStr):
        pattern = self.__patternsMemoized[reg]
        return pattern.format(*inputListValues) #+ "\t\tⓜ"
    return None


  ## inserts new patterns of input and result into { __patternsMemoized }
  def addExpression(self, _input, _result, valuesQuantity):
    inputStr = mapperStr(self.__format(_input))
    resultStr = mapperStr(self.__format(_result))
    valuesRegex = ["\(?[-\w]+\)?" for x in range(valuesQuantity)]
    inputRegex = self.__join(mapperRegex(inputStr)).format(*valuesRegex)
    resultRegex = self.__join(mapperRegex(resultStr)).format(*valuesRegex)
    self.__patternsMemoized[f"^{inputRegex}$"] = self.__join(resultStr)
    self.__patternsMemoized[f"^{resultRegex}$"] = self.__join(inputStr)


  ## searches values in expresson list
  def __filterValues(self, example): 
    filtrator = lambda x: not re.match(r"^[-/\*\^\+)(]{1}$", x)
    filtered = filter(filtrator, example)
    return list(filtered)


  ## removes spaces between brackets
  def __format(self, arr):
    for x in arr:
      if "(" in x:
        return [x for x in "".join(arr)]
    return arr


  ## join array elements formating them
  def __join(self, arr):
    if not ("\\(" in arr or "(" in arr):
      return " ".join(arr)
    result = list()
    for x in arr:
      if re.match(r"^(-|/|\\\\\*|\\\\\^|\\\\\+|\+|\^|\*)$", x):
        result += [" ", x, " "]
      else:
        result.append(x)
    return "".join(result)
