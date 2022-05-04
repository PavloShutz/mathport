def calc(s):

    stack, curr_num, operator = [], 0, "+"
    all_operators = {"+", "-", "*", "/"}
    nums = set((str(x) for x in range(10)))

    for index in range(len(s)):
        char = s[index]

        if char in nums:
            curr_num = curr_num * 10 + float(char)

        if char in all_operators or index == len(s) - 1:
            if operator == "+":
                stack.append(curr_num)

            elif operator == "-":
                stack.append(-curr_num)

            elif operator == "*":
                stack[-1] *= curr_num

            elif operator == "/":
                try:
                    stack[-1] = stack[-1] / curr_num
                except ZeroDivisionError:
                    return "Division by zero!"
            curr_num = 0
            operator = char

    return sum(stack)


if __name__ == '__main__':
    while True:
        print(calc(input(">>>")))
