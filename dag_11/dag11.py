def main():
    
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    weight_limit = int(lines[0])
    all_toys = {}

    for line in lines[1:]:
        toy, weight, glede = line.strip().split(",")
        weight = int(weight)
        glede = int(glede)
        all_toys[toy] = (weight, glede)
        
    toys_list = list(all_toys.items())

    n = len(toys_list)

    dp = [0] * (weight_limit + 1)

    choice = [[False] * (weight_limit + 1) for _ in range(n)]

    for i, (toy_name, (weight, glede)) in enumerate(toys_list):
        for w in range(weight_limit, weight - 1, -1):
            if dp[w - weight] + glede > dp[w]:
                dp[w] = dp[w - weight] + glede
                choice[i][w] = True

    glede_output = max(dp)
    presents_sent = []
    w = dp.index(glede_output)

    for i in range(n - 1, -1, -1):
        if choice[i][w]:
            toy_name, (weight, glede) = toys_list[i]
            presents_sent.append(toy_name)
            w -= weight

    num_presents = len(presents_sent)

    print(f"Total glede: {glede_output}")
    print(f"Number of presents sent: {num_presents}")
    print("Presents:")
    for p in presents_sent:
        print(f" - {p}")

    return glede_output, num_presents


print(main())
