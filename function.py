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


def natural_log(x):
    return math.log(x, math.e)


functions = [
    Function("arcsin", math.asin),
    Function("arccos", math.acos),
    Function("arctan", math.atan),
    Function("sinh", math.sinh),
    Function("cosh", math.cosh),
    Function("tanh", math.tanh),
    Function("exp", math.exp),
    Function("sin", math.sin),
    Function("cos", math.cos),
    Function("tan", math.tan),
    Function("log", math.log10),
    Function("ln", natural_log)
]


def find_function_by_name(functions_list, name):
    for func in functions_list:
        if func.name == name:
            return func

# if __name__ == "__main__":
    # symbol = "s"
    #
    # for func in functions:
    #     if func[0] == symbol:
    #         token = symbol
    #         print(token)
    #
    #         print(func(2))
