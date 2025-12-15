import re

def parse_number(text):
    return int(re.search(r"\d+", text).group())

def main():

    total_produced = {}

    with open("julebrusmaskiner.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = [p.strip() for p in line.split(",")]

            machine_name = parts[0].replace("Maskin", "").strip()
            temperatur = parse_number(parts[1])
            vann = parse_number(parts[2])
            kullsyre = parse_number(parts[3])
            
            if 95 <= temperatur <= 105 and 400 <= vann <= 1500 and 300 <= kullsyre <= 500:

                produced = (vann - 100) + (kullsyre * 0.1)

                if temperatur >= 100:
                    evaoprated = int(produced/40)
                    produced -= evaoprated

                total_produced[machine_name] = total_produced.get(machine_name, 0) + int(produced)

    print(f"Total amount is: {int(sum(total_produced.values()))}")

    machine, amount = max(total_produced.items(), key=lambda x: x[1])
    print(f"The machine who made the most is: {machine} with {amount}L")


main()
