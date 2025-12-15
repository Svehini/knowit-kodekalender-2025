

def main():
    
    weightLost = 167772150 - 149848566
    chocolatesPerWindow = [2**(i-1) for i in range(1, 25)]
    
    realWeight = 167772150/sum(chocolatesPerWindow)
    mockWeith = 0.7 * realWeight
    
    weightLostPerWindow = [window * (realWeight - mockWeith) for window in chocolatesPerWindow]
    
    
    
    fakeWindows = []
    remainingLost = weightLost
    
    for i in range(24-1, -1, -1):
        if weightLostPerWindow[i] <= remainingLost:
            fakeWindows.append(i+1)
            remainingLost -= weightLostPerWindow[i]
            
    numOfMockulades = sum(chocolatesPerWindow[i-1] for i in fakeWindows)
    fakeWindows.sort()
    
    print(f"SjokoladeMg:{int(realWeight)},MockuladeMg:{int(mockWeith)},AntallMockulader:{numOfMockulades},Luker:{",".join(map(str, fakeWindows))}")

main()