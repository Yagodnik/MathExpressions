import math


def empty_function(x):
    print("EMPTY FUNCTION")


class Function:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def __str__(self):
        return self.name

    def __call__(self, x):
        return self.function(x)

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        return self.name[index]


def log10(x):
    if x < 0:
        print(f"Invalid argument for log10!\n{x} < 0 !")
        exit(0)

    return math.log10(x)


def natural_log(x):
    if x < 0:
        print(f"Invalid argument for natural log!\n{x} < 0 !")
        exit(0)

    return math.log(x, math.e)


def arcsin(x):
    if not -math.pi / 2 <= x <= math.pi / 2:
        print(f"Invalid argument for arcsin!\nValue is not in range -pi/2 <= {x} <= pi/2 !")
        exit(0)

    return math.asin(x)


def arccos(x):
    if not -math.pi / 2 <= x <= math.pi / 2:
        print(f"Invalid argument for arccos!\nValue is not in range -pi/2 <= {x} <= pi/2 !")
        exit(0)

    return math.acos(x)


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


functions = [
    Function("arcsin", arcsin),
    Function("arccos", arccos),
    Function("arctan", math.atan),
    Function("sign", sign),
    Function("sinh", math.sinh),
    Function("cosh", math.cosh),
    Function("tanh", math.tanh),
    Function("exp", math.exp),
    Function("sin", math.sin),
    Function("cos", math.cos),
    Function("tan", math.tan),
    Function("log", log10),
    Function("ln", natural_log)
]


def find_function_by_name(functions_list, name):
    for func in functions_list:
        if func.name == name:
            return func

    return None

# if __name__ == "__main__":
    # symbol = "s"
    #
    # for func in functions:
    #     if func[0] == symbol:
    #         token = symbol
    #         print(token)
    #
    #         print(func(2))
