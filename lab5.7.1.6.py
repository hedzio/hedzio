# Definicja segmentów dla każdej cyfry
SEGMENTS = {
    '0': [' _ ', '| |', '|_|'],
    '1': ['   ', '  |', '  |'],
    '2': [' _ ', ' _|', '|_ '],
    '3': [' _ ', ' _|', ' _|'],
    '4': ['   ', '|_|', '  |'],
    '5': [' _ ', '|_ ', ' _|'],
    '6': [' _ ', '|_ ', '|_|'],
    '7': [' _ ', '  |', '  |'],
    '8': [' _ ', '|_|', '|_|'],
    '9': [' _ ', '|_|', ' _|']
}

def segment(number):
    lines = ['', '', '']
    for i in str(number):
        seg = SEGMENTS.get(i, ['   ', '   ', '   '])
        for j in range(3):
            lines[j] += seg[j] + ' '
    for line in lines:
        print(line)
    return ''  # Add a return statement to avoid printing 'None'

try:
    liczby_do_podania = int(input("Podaj liczbe: "))
    print(segment(liczby_do_podania))
except ValueError:
    print("Podaj liczbe całkowitą!!!")
