from Interpreter import PolishNotation
import time

tests1 = [
  ("a b + c /", "(a + b) / c"),
  ("a b ^ c +", "a ^ b + c"),
  ("3 6 * 4 3 0 7 - / ^ -", "3 * 6 - 4 ^ (3 / (0 - 7))"),
  ("3 6 4 3 0 7 - / ^ - *", "3 * (6 - 4 ^ (3 / (0 - 7)))")
]

p = PolishNotation()

print("TESTS: 1/2:\n")

for test in tests1:
  print(f"test 1.{tests1.index(test) + 1}:")
  (res2, res1) = test
  p1 = p.interpret(res2, "fromPolish")
  p2 = p.interpret(res1, "toPolish")
  print(f"p1: {p1}")
  print(f"p1 == res1: {p1} == {res1} [{p1 == res1}]")
  print(f"p2: {p2}")
  print(f"p2 == res2: {p2} == {res2} [{p2 == res2}]")
  print()


print("TESTS: 2/2: \n")
def timer(example, interpreter):
  timeStart = time.monotonic()
  p1 = p.interpret(example)
  timeEnd = time.monotonic() - timeStart
  return timeEnd

def timerCmp(example, interpreter = "toPolish"):
  print(f"example: {example}")
  calculated = timer(example, interpreter)
  print(f"calculated:  {calculated}")
  memoized = timer(example, interpreter)
  print(f"memoized:    {memoized}\n")

print("test 2.1:")
timerCmp("(a4 - b5 ^ (-5t)) * (36 / 80)")
print("interpreted from Poish (previous)")
timerCmp("a b -5t ^ - 3 80 / *")

print("test 2.2:")
timerCmp("a + b")
print("interpreted from Poish (previous)")
timerCmp("aa ccc +")

