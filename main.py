from shuntingyard import *
from rpn import *


# TODO: fix bug (5 + 1)! and (5 +1)! different result!
# TODO: fix bug (2 ^ 3)! and (2^3)!
# TODO: fix bug with mismatched brackets checking

if __name__ == '__main__':
    expression = "sinh(ln(2 ^ 3))"

    parser = TokenParser()
    parser.set_expression(expression)
    tokens = parser.parse_tokens()

    # for token in tokens:
    #     print(token)

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
