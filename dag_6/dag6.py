

from collections import deque


def find_start(zone):
    # print(zone)
    for i in range(0, len(zone)):
        if "S" in zone[i]:
            for j in range(0, len(zone[i])):
                if zone[i][j] == "S":
                    return (i, j)
            
def find_shortest(zone, dir):
    start = find_start(zone)
    if start == None:
        return 0
    # print(f"START: {start}")
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = {start}
    
    height = len(zone)
    length = len(zone[0])
    
    
    while queue != []:
        x, y, d = queue.popleft()
        if zone[x][y] == "*":
            return d
        

        for (dx, dy) in dir:
            nx = x + dx
            ny = y + dy
            # print(f"nx, ny: {nx, ny}")
            if (nx >= 0 and nx <= length-1) and (ny >= 0 and ny <= height-1) and zone[nx][ny] != "#" and (nx, ny) not in visited:
                queue.append((nx, ny, d+1))
            # print(f"QUEUE: {queue}")
        visited.add((nx, ny))
    return 0

def main():
    
    with open("perfeksjonsruten.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    zones = []
    newZone = []
    for line in lines:
        if ";" not in line:
            newZone.append(line.rstrip("\n"))
        else:
            zones.append(newZone)
            newZone = []
    if ";" not in lines[-1]:
        zones.append(newZone)
        
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    shortest_paths = []
    for zone in zones:
        shortest_paths.append(find_shortest(zone, dir))
    
    
    print(f"Shortest Paths is: {shortest_paths},\n with sum: {sum(shortest_paths)}")

main()