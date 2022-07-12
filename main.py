from shuntingyard import *
from rpn import *


if __name__ == '__main__':
    expression = "sinh(arcsin(-0.5))"

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
