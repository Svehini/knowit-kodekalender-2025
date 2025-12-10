

def main():
    
    reversed_morse = {
        'Ho-Hooo': 'A',
        'Hooo-Ho-Ho-Ho': 'B',
        'Hooo-Ho-Hooo-Ho': 'C',
        'Hooo-Ho-Ho': 'D',
        'Ho': 'E',
        'Ho-Ho-Hooo-Ho': 'F',
        'Hooo-Hooo-Ho': 'G',
        'Ho-Ho-Ho-Ho': 'H',
        'Ho-Ho': 'I',
        'Ho-Hooo-Hooo-Hooo': 'J',
        'Hooo-Ho-Hooo': 'K',
        'Ho-Hooo-Ho-Ho': 'L',
        'Hooo-Hooo': 'M',
        'Hooo-Ho': 'N',
        'Hooo-Hooo-Hooo': 'O',
        'Ho-Hooo-Hooo-Ho': 'P',
        'Hooo-Hooo-Ho-Hooo': 'Q',
        'Ho-Hooo-Ho': 'R',
        'Ho-Ho-Ho': 'S',
        'Hooo': 'T',
        'Ho-Ho-Hooo': 'U',
        'Ho-Ho-Ho-Hooo': 'V',
        'Ho-Hooo-Hooo': 'W',
        'Hooo-Ho-Ho-Hooo': 'X',
        'Hooo-Ho-Hooo-Hooo': 'Y',
        'Hooo-Hooo-Ho-Ho': 'Z'
    }


    
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        solution = ""
        
        for line in lines:
            letters = line.split(" ")
            for letter in letters:
                solution+=reversed_morse[letter.strip()]
        
        print(solution)
        
    
main()