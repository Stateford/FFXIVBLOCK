ffxiv_block = {
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
    
    for char in msg:
        print ffxiv_block[char.lower()]
        
if __name__ == "__main__":
    main()
