

def isPrime(num):
    if num < 2:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    
    return True
    
def isOdd(number):
    return True if number % 2 == 1 else False

def main():
    
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
        output = []
        for line in lines:
            line = line.rstrip("\n")
            line = line.split(" ")
            for number in line:
                if number == number[::-1] and isPrime(int(number)):
                    output.append(number)
             
        print(f"The numbers are:\n{output}")
        print(f"\nNumber of pal+prime is: {len(output)}")
        
main()