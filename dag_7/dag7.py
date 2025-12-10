
def isThereTroll(word, troll, distance):
    for i in range(0, len(word)):
        if word[i] == troll[0] and distance <= 5 and distance > 0:
            if len(troll) == 1:
                return 1
            new_troll = troll[1:]
            if isThereTroll(word[i+1:], new_troll, 0):
                return 1
        distance+=1
    return 0
    

def isThereNisse(word, nisse, distance):
    for i in range(0, len(word)):
        if word[i] == nisse[0] and distance <= 2:
            if len(nisse) == 1:
                return 1
            new_nisse = nisse[1:]
            if isThereNisse(word[i+1:], new_nisse, 0):
                return 1
        distance+=1
    return 0

def isThereWord(word):
    for i in range(0, len(word)):
        if word[i] == "t" and isThereTroll(word[i+1:], ['r', 'o', 'l', 'l'], 0):
            return 1
        if word[i] == "n" and word[0] != "n" and word[-1] != "e" and isThereNisse(word[i+1:], ['i', 's', 's', 'e'], 0):
            return 1
    return 0

def main():
    
    with open("ordliste.txt", "r", encoding="utf-8") as f:
        words = f.readlines()
    
    # words = ["tlrkoklkl"]
    numberOfTrollsAndNisser = 0
    for word in words:
        word = word.rstrip("\n")
        score = isThereWord(word)
        if score == 1:
            print(f"New word added: {word}")
        numberOfTrollsAndNisser+=score
    print(f"Number of nisser and troll: {numberOfTrollsAndNisser}")

main()