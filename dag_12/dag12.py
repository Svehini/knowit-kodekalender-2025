

def main():
    
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    pending_togsett = False
    bamse = "01001010"
    togsett = "01000010"
    
    output = 0
    for line in lines:
        line = line.strip()
        if line == togsett:
            pending_togsett = True
        elif line == bamse and pending_togsett:
            print(f"bamse: {line}")
            output += 1
            pending_togsett = False
    return output
    
print(main())