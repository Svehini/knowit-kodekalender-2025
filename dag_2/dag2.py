

def caesar_cypher(input_text, shift):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyzæøå"
    alphabet_upper = alphabet_lower.upper()

    output = ""

    for char in input_text:
        if char in alphabet_lower:
            idx = alphabet_lower.index(char)
            new_idx = (idx - shift) % len(alphabet_lower)
            output += alphabet_lower[new_idx]

        elif char in alphabet_upper:
            idx = alphabet_upper.index(char)
            new_idx = (idx - shift) % len(alphabet_upper)
            output += alphabet_upper[new_idx]

        else:
            output += char

    return output


def main():
    password = ""
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    first_line = lines[0]
    user_input = "n"
    shift = 0
    while user_input != "y":
        this_first_line = caesar_cypher(first_line, shift)
        user_input = input(f"{this_first_line}Does this look correct?\nYes(y)/No(n)")
        if user_input == "y":
            break
        shift += 1
    
    output = []
    for line in lines:
        line = caesar_cypher(line, shift)
        output.append(line)
        shift += 1
    output = ", ".join(w.strip() for w in output)
    print(f"Decrypted:\n{output}")
    
main()