from shuntingyard import *
from rpn import *


# TODO: fix bug with mismatched brackets checking


def parse(exp):
    parser = TokenParser()
    parser.set_expression(exp)
    tokens = parser.parse_tokens()

    print(f"Parsing {exp}")
    for token in tokens:
        print(token[1])

    print()


if __name__ == '__main__':
    expression = "(2 ^ 3)!"

    parser = TokenParser()
    parser.set_expression(expression)
    tokens = parser.parse_tokens()

    print(expression)
    for token in tokens:
        print(token)


    # parse("(5 + 1)!")
    # parse("(5 +1)!")
    #
    # exit(0)

    algorithm = ShuntingYard()
    algorithm.specify_tokens_list(tokens)
    algorithm.evaluate_rpn()

    print(f"RPN for expression {expression}")
    algorithm.print_output_queue()

    rpn_expression = algorithm.get_output_queue()
    print("\n")

    rpn = RPNExpression()
    rpn.specify_expression(rpn_expression)
    print(f"{expression} = {rpn.evaluate()}")
