

def main():
    rangsjering = {}
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for line in lines[1:]:
        line = line.split(",")
        score = int(line[1])*50 - int(line[2])*25 + int(line[3])*15
        rangsjering[line[0]] = score
    
    sorted_scores = sorted(rangsjering.items(), key=lambda x: x[1])
    
    lowest_scores = sorted_scores[:3]
    highest_scores = sorted_scores[-3:]
    
    output = ""
    for score in lowest_scores:
        output = f"{score[0]} {score[1]}," + output
    for score in highest_scores:
        output = f"{score[0]} {score[1]}," + output
    

    print(output)
main()