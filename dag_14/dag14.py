

def findShortestLoop(all_nodes, adjecency_list):
    shortesLoopWeight = 100000000000
    shortestLoopPath = []
    all_nodes = sorted(all_nodes, key=lambda x: int(x[1]))

    def DFS(start, current, path, total_weight):
        nonlocal shortesLoopWeight, shortestLoopPath
        for (neighbor, weight) in adjecency_list[current]:
            if neighbor == start:
                cycle_weight = total_weight + weight
                if cycle_weight < shortesLoopWeight:
                    shortesLoopWeight = cycle_weight
                    shortestLoopPath = path + [start]
            elif neighbor not in path:
                DFS(start, neighbor, path + [neighbor], total_weight + weight)   

    for node in all_nodes:
        DFS(start=node, current=node, path=[node], total_weight=0)
    
    return shortesLoopWeight, shortestLoopPath



def main():
    
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        
    all_nodes = []
    adjecency_list = {}
    
    for line in lines:
        parts = line.split(" ")
        start = parts[0]
        end = parts[2]
        time = int(parts[3].strip("()"))
        if start not in all_nodes:
            all_nodes.append(start)
        adjecency_list.setdefault(start, []).append((end, time))

    shortestLoopWeight, shortestLoopPath = findShortestLoop(all_nodes, adjecency_list)
    
    print(f" -> ".join(shortestLoopPath) + f" ({shortestLoopWeight})")

main()