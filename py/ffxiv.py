ffxiv = {
    'a': '',
    'b': '',
    'c': '',
    'd': '',
    'e': "",
    'f': '',
    'g': '',
    'h': '',
    'i': "",
    'j': '',
    'k': '',
    'l': '',
    'm': '',
    'n': '',
    'o': '',
    'p': '',
    'q': '',
    'r': '',
    's': '',
    't': '',
    'u': '',
    'v': '',
    'w': '',
    'x': '',
    'y': '',
    'z': '',
}

def main():

     msg = input('ENGLISH TO FFXIVBLOCK: ')
     final = []

     for char in msg:
         final.append(ffxiv.get(char.lower(), char.lower()))
     print("".join(final))

main()
