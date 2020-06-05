from Interpreter import PolishNotation

tests = [
  ("a b + c /", "(a + b) / c"),
  ("a b ^ c +", "a ^ b + c"),
  ("3 6 * 4 3 0 7 - / ^ -", "3 * 6 - 4 ^ (3 / (0 - 7))"),
  ("3 6 4 3 0 7 - / ^ - *", "3 * (6 - 4 ^ (3 / (0 - 7)))")
]

p = PolishNotation()

for test in tests:
  print(f"Test {tests.index(test) + 1}:")
  res1 = test[1]
  res2 = test[0]
  p1 = p.interpret(test[0], "fromPolish")
  p2 = p.interpret(test[1], "toPolish")
  print(p1)
  print(p1 == res1)
  print(p2)
  print(p2 == res2)
  print()

print("Намальна...")
