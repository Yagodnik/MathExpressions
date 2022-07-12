from operators import *
from function import *


# https://stackoverflow.com/questions/40328938/how-to-evaluate-reverse-polish-notation-using-stacks
class RPNExpression:
    def __init__(self):
        self.expression = []
        self.stack = []
        self.index = 0
        self.length = 0

    def specify_expression(self, expression):
        self.expression = expression
        self.length = len(self.expression)

    def evaluate(self):
        while True:
            if self.index > self.length - 1:
                break

            item = self.expression[self.index]

            if isinstance(item, Operator):
                if item.symbol == "+":
                    x = float(self.stack.pop(-1))
                    y = float(self.stack.pop(-1))
                    self.stack.append(x + y)

                if item.symbol == "-":
                    x = float(self.stack.pop(-1))
                    y = float(self.stack.pop(-1))
                    self.stack.append(y - x)

                if item.symbol == "*":
                    x = float(self.stack.pop(-1))
                    y = float(self.stack.pop(-1))
                    self.stack.append(x * y)

                if item.symbol == "/":
                    x = float(self.stack.pop(-1))
                    y = float(self.stack.pop(-1))
                    self.stack.append(y / x)

                if item.symbol == "^":
                    x = float(self.stack.pop(-1))
                    y = float(self.stack.pop(-1))
                    self.stack.append(y ** x)

                if item.symbol == "!":
                    x = float(self.stack.pop(-1))
                    self.stack.append(math.factorial(x))

            elif isinstance(item, Function):
                x = float(self.stack.pop(-1))
                self.stack.append(item(x))
            else:
                self.stack.append(item)

            self.index += 1

        return self.stack[0]
