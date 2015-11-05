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
    
    msg = raw_input('ENGLISH TO FFXIVBLOCK: ')
    final = ''
    
    for char in msg:
        final.append(ffxiv[char.lower()])
        print final
        
if __name__ == "__main__":
    main()
