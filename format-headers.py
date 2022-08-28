import os

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

    for line in lines:
        if line[0] == ':':
            line = str(line).replace(line[0], '', 1)

        line = line[:-1] + line[-1] + "'"
        line = line[:-1] + line[-1] + ','
        line_info = str(line).split(': ')[1]

        line = str(line).replace(line_info, "'" + line_info)

        line_info = line.split(': ')[0]
        line = line.replace(line_info, "'" + line_info + "'")

        print(line)

while True:
    main()
    input('\nPress enter to continue...')
    os.system('cls')
