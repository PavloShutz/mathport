def calc(expr):
    operator_function = {
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    expression = ''.join([i for i in expr.split(' ')])
    nums = list()
    opers = list()

    tokens = list('(' + expression + ')')

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
