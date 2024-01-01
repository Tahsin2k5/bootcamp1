class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_ops = MathOperations()
result1 = math_ops.add(1, 2)        # Calls the first add method
result2 = math_ops.add(1, 2, 3)     # Calls the second add method

print(result1)
print(result2)
