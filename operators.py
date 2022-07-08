class Operator:
    def __init__(self, symbol, precedence):
        self.symbol = symbol
        self.precedence = precedence

    def __str__(self):
        return self.symbol

    def __gt__(self, other):
        return self.precedence > other.precedence

    def __lt__(self, other):
        return self.precedence < other.precedence

    def __eq__(self, other):
        if other.symbol != "^" and self.symbol != "^":
            return self.precedence == other.precedence
        else:
            return False


plus_sign = Operator("+", 1)
minus_sign = Operator("-", 1)
mul_sign = Operator("*", 2)
div_sign = Operator("/", 2)
pow_sign = Operator("^", 3)
fac_sign = Operator("!", 4)


def contains_operator(list, operator_symbol):
    for item in list:
        if item.symbol == operator_symbol:
            return True

    return False


def symbol_to_operator(symbol):
    if symbol == "+":
        return plus_sign
    elif symbol == "-":
        return minus_sign
    elif symbol == "*":
        return mul_sign
    elif symbol == "/":
        return div_sign
    elif symbol == "^":
        return pow_sign


if __name__ == "__main__":
    print(f"+ = - ? {plus_sign == minus_sign}")
    print(f"^ = * ? {pow_sign == mul_sign}")
    print(f"^ > * ? {pow_sign > mul_sign}")
    print(f"^ > - ? {pow_sign < minus_sign}")

    print(fac_sign)
