import os

def format_headers(input_lines):
    """
    Formats headers from a list of input lines.

    Args:
        input_lines: A list of lines each representing a header key-value pair.

    Returns:
        A dictionary representing the headers.
    """
    headers = {}
    key = None
    for line in input_lines:
        stripped = line.strip()
        if stripped:
            if ':' in stripped and ' ' in stripped: # Line format is "key: value"
                split_line = stripped.split(':', 1) # Only split on the first ':'
                key = split_line[0].strip().replace(':', '') # Remove all colons from the key
                value = split_line[1].strip()
                headers[key] = value
                key = None # Reset key
            elif ':' in stripped: # Line format is "key:"
                key = stripped.replace(':', '')  # Remove all colons from the key
            elif key: # Line format is "value"
                headers[key] = stripped # Set value to the key from the previous line
                key = None # Reset key
    return headers

def main():
    print('Paste your headers here:')
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    os.system('cls')

    headers = format_headers(lines)

    print("headers = {")
    for key, value in headers.items():
        print(f"    '{key}': '{value}',")
    print("}")

if __name__ == "__main__":
    while True:
        main()
        input('\nPress enter to continue...')
        os.system('cls')
        