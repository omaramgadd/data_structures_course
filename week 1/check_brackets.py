def isbalanced(text):
    stack = []
    lst = []
    for index, char in enumerate(text, start=1):
        if char not in "[{()}]":
            continue
        if char in "[{(":
            stack.append(char)
            lst.append(index)
        else:
            if len(stack) == 0:
                return index
            top = stack.pop()
            lst.pop()
            if (top == '[' and char != ']') or (top == '{' and char != '}') or (top == '(' and char != ')'):
                return index
    if len(stack) != 0:
        return lst[0]
    else:
        return "Success"


if __name__ == "__main__":
    text = input()
    print(isbalanced(text))