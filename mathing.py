def calc(expr):
    operator_function = {
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    nums = list()
    opers = list()

    tokens = list('(' + expr + ')')

    while tokens:
        token = tokens.pop(0)

        if token.isdecimal():
            nums.append(float(token))
        else:
            if token == ')':
                oper = opers.pop()
                while opers and oper != '(':
                    b, a = nums.pop(), nums.pop()
                    f = operator_function[oper]
                    nums.append(f(a, b))

                    oper = opers.pop()

            else:
                opers.append(token)

    return nums[0]


if __name__ == '__main__':
    while True:
        a = input()
        print(calc(a))
