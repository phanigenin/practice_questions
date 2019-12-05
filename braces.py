# Check if input string is a valid one, with parantheses
REF = {'{':'}','(':')','[':']'}


def isValid(s: str) -> bool:
    stack = []
    for char in s:
        if char in REF.keys():
            stack.append(char)
        else:
            ix = list(REF.values()).index(char)
            match = list(REF.keys())[ix]
            stack.remove(match)

    return not len(stack)