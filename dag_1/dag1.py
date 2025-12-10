


def main():
    password = ""
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    waiting = []
    for line in lines:
        if "ADD" in line:
            waiting.append(line)
        elif "PROCESS" in line:
            if waiting == []:
                password+=("X")
            package_to_process = waiting[0]
            waiting.pop(0)
            password+=(package_to_process.split()[1][0])
        elif "COUNT" in line:
            count = len(waiting)
            if count >= 10:
                count = count % 10
            password+=(str(count))
    print(f"Password is: {password}")
    
main()
    