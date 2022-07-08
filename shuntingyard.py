from tokenparser import *
from operators import *


# My bullshit implementation of this algorithm in P y T h O n
class ShuntingYard:
    def __init__(self):
        self.tokens = []
        self.output_queue = []
        self.operator_stack = []

    def specify_tokens_list(self, tokens):
        self.tokens = tokens

    def evaluate_rpn(self):
        for token in self.tokens:
            type = token[0]
            value = token[1]

            if type == NUMBER:
                self.output_queue.append(value)
            elif type == FUNCTION:
                self.operator_stack.insert(0, value)
            elif type == OPERATOR:
                if len(self.operator_stack) > 0:
                    if isinstance(self.operator_stack[0], Operator):
                        while len(self.operator_stack) > 0 and (self.operator_stack[0] > value or self.operator_stack[0] == value):
                            self.output_queue.append(self.operator_stack[0])
                            self.operator_stack.pop(0)

                            if len(self.operator_stack) > 0:
                                if not isinstance(self.operator_stack[0], Operator):
                                    break
                            else:
                                break
                    elif self.operator_stack[0] == "(":
                        pass
                    self.operator_stack.insert(0, value)
                else:
                    self.operator_stack.append(value)
            elif type == PARENTHESES:
                if value == "(":
                    self.operator_stack.insert(0, value)
                elif value == ")":
                    while True:
                        if not isinstance(self.operator_stack[0], Operator):
                            if self.operator_stack[0] == "(":
                                self.operator_stack.pop(0)
                                break

                        self.output_queue.append(self.operator_stack[0])
                        self.operator_stack.pop(0)

                    if isinstance(self.operator_stack[0], Function):
                        self.output_queue.append(self.operator_stack[0])
                        self.operator_stack.pop(0)

        while len(self.operator_stack) > 0:
            self.output_queue.append(self.operator_stack[0])
            self.operator_stack.pop(0)

    def print_output_queue(self):
        for item in self.output_queue:
            print(item, end=" ")

    def get_output_queue(self):
        return self.output_queue


if __name__ == "__main__":
    test_expression1 = "333 + 43 * 2 / (1 - 5) ^ 2 ^ 3"

    parser = TokenParser()
    parser.set_expression(test_expression1)
    tokens = parser.parse_tokens()

    algorithm = ShuntingYard()
    algorithm.specify_tokens_list(tokens)
    algorithm.evaluate_rpn()

    print(f"RPN for expression {test_expression1}")
    algorithm.print_output_queue()

