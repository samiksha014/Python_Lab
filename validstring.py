def check_validity(text: str) -> str:

    # Define the set of valid bracket symbols
    bracket_symbols = {'(', ')', '[', ']', '{', '}', '<', '>'}
    bracket_pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    store = []

    # Iterate through each character in the text
    for char in text:
        if char in bracket_symbols:
            # If it's an opening bracket, push it onto the store
            if char in bracket_pairs.values():
                store.append(char)
            # If it's a closing bracket, check for a matching opening bracket
            elif char in bracket_pairs:
                if not store or store[-1] != bracket_pairs[char]:
                    return f"invalid: unmatched closing bracket '{char}' at position {text.index(char)}"
                else:
                    store.pop()
        elif not char.isalnum() and char not in " +-*/":  # Optional: allow some basic non-bracket symbols
            return f"invalid: invalid character '{char}' at position {text.index(char)}"

    # If store is not empty, it means there's an unmatched opening bracket
    if store:
        return f"invalid: unmatched opening bracket '{stack[-1]}'"

    return "valid"

# Example usage:
test_cases = [
    "(<>)",   # valid
    "(<)>",   # invalid: unmatched closing bracket
    "+()",    # valid (if considering simple algebraic characters as valid)
    "{1}",    # valid (alphanumeric and balanced brackets)
    ")(<)",   # invalid: unmatched closing bracket
]

for case in test_cases:
    result = check_validity(case)
    print(f"{case}: {result}")
