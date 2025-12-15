

def main():
    
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    
    whole_string = "".join(lines)
    
    constonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    output = ""
    
    chars = list(whole_string)
    for i in range(0, len(chars)-1):
        if chars[i] in nums:
            continue
        if chars[i] in constonants:
            if (i >= 2 and i+2 <= len(chars)) and chars[i-2] in nums and chars[i+2] in nums:
                output+=chars[i]
        else:
            output+=chars[i]
        
                    
                
    
    print(output)
    
main()