from shuntingyard import *
from rpn import *


if __name__ == '__main__':
    expression = "ln(tan(54) / 3 * 2^2)"

    parser = TokenParser()
    parser.set_expression(expression)
    tokens = parser.parse_tokens()

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

