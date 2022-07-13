from operators import *
from function import *


NUMBER = 1
OPERATOR = 2
FUNCTION = 3
PARENTHESES = 4
SPECIAL_SYMBOL = 5


# TODO: add float and negative numbers support
class TokenParser:
    def __init__(self):
        self.nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        self.operators = [pow_sign, fac_sign, mul_sign, div_sign, plus_sign, minus_sign]
        self.parentheses = ["(", ")", "|", "|"]
        self.functions = functions
        self.special_symbols = [","]
        self.last_operator = False

        self.token = None
        self.expression = ""
        self.expression_length = 0
        self.index = 0
        self.tokens = []
        self.symbol = ""

    def set_expression(self, expression):
        self.expression = expression
        self.expression_length = len(expression) - 1

    def parse_number(self):
        token = self.symbol
        self.index += 1

        if self.index > self.expression_length:
            self.tokens.append((NUMBER, token))
            return

        while self.nums.__contains__(self.expression[self.index]):
            token += self.expression[self.index]
            self.index += 1

            if self.index > self.expression_length:
                break

        self.tokens.append((NUMBER, token))

    def parse_operator(self):
        self.tokens.append((OPERATOR, symbol_to_operator(self.symbol)))
        self.index += 1
        self.last_operator = True

    def parse_parentheses(self):
        self.tokens.append((PARENTHESES, self.symbol))
        self.index += 1

    def parse_special_symbol(self):
        self.tokens.append((SPECIAL_SYMBOL, self.symbol))
        self.index += 1

    def parse_function(self):
        token = ""
        is_function = False

        for func in self.functions:
            if func[0] == self.symbol:
                is_function = True
                token = self.symbol
                token_index = 1
                local_index = self.index
                local_index += 1
                func_length = len(func) - 1

                while True:
                    symbol = self.expression[local_index]
                    if func[token_index] != symbol:
                        token = ""
                        break

                    token_index += 1
                    token += symbol
                    local_index += 1

                    if token_index > func_length:
                        break

            if token != "":
                function_name = find_function_by_name(self.functions, token)

                if function_name is None:
                    print(f"Unknown function called: '{function_name}'")

                self.index = local_index
                self.tokens.append((FUNCTION, function_name))
                break

        if token == "":
            if is_function:
                name = ""

                while self.expression[self.index] != "(":
                    name += self.expression[self.index]
                    self.index += 1

                print(f"Unknown function called: '{name}'!")
            else:
                self.index += 1

    def parse_tokens(self):
        while True:
            if self.index > self.expression_length:
                break

            self.symbol = self.expression[self.index]

            if self.nums.__contains__(self.symbol):
                self.parse_number()
                self.last_operator = False
                continue
            elif contains_operator(self.operators, self.symbol):
                if not self.last_operator and not isinstance(symbol_to_operator(self.symbol), Operator):
                    if self.index < self.expression_length:
                        next_symbol = self.expression[self.index + 1]

                        if self.nums.__contains__(next_symbol):
                            self.parse_number()
                            self.last_operator = False
                            continue

                self.parse_operator()
                self.last_operator = False
                continue
            elif self.parentheses.__contains__(self.symbol):
                self.parse_parentheses()
                self.last_operator = False
                continue
            elif self.special_symbols.__contains__(self.symbol):
                self.parse_special_symbol()
                self.last_operator = False
                continue
            else:
                self.parse_function()
                self.last_operator = False
                continue

            self.index += 1

        return self.tokens
