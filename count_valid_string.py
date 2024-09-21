def check_validity(text: str) -> str:
    bracket_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    opening_brackets = set(bracket_pairs.values())
    stack = []

    for index, char in enumerate(text):
        if char in opening_brackets:
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[char]:
                return "invalid"
            stack.pop()
        elif not char.isalnum() and char not in " +-*/":
            return "invalid"

    if stack:
        return "invalid"

    return "valid"


def get_valid_invalid_text_count(text_list):
    valid_count = 0
    invalid_count = 0

    for item in text_list:
        if isinstance(item, str):
            if check_validity(item) == "valid":
                valid_count += 1
            else:
                invalid_count += 1

    return (valid_count, invalid_count)

text_list = ['[{(', [45, '()'], '({})', '(<)>', 'Hello']
result = get_valid_invalid_text_count(text_list)
print(result)  
