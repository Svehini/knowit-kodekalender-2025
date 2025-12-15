import gurobipy as gp
from gurobipy import GRB


def read_data():
    
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    T = int(lines[0].split("=")[1])
    
    prep_time = {}
    cake_value = {}
    cake_preps = {}
    
    i = 1
    
    while lines[i] != "---": 
        name, time = lines[i].split(":")
        prep_time[name] = time
        i += 1
    
    i += 1
    
    for line in lines[i:]:
        parts = line.split()
        cake = parts[0]
        joy = int(parts[1])
        preps = parts[2:]
        cake_value[cake] = joy
        cake_preps[cake] = preps
    
    return T, prep_time, cake_value, cake_preps


def solverIHardlyKnowHer(T, prep_time, cake_value, cake_preps):
    m = gp.Model("Julebakst")
    m.setParam("OutputFlag", 0)
    
    x = m.addVars(cake_value.keys(), vtype=GRB.BINARY, name="cake")
    y = m.addVars(prep_time.keys(), vtype=GRB.BINARY, name="prep")
    
    m.setObjective(
        gp.quicksum(cake_value[c] * x[c] for c in cake_value),
        GRB.MAXIMIZE
    )
    
    m.addConstr(
        gp.quicksum(prep_time[p] * y[p] for p in prep_time) <= T,
        name="time_limit"
    )
    
    for c in cake_preps:
        for p in cake_preps[c]:
            m.addConstr(x[c] <= y[p], name=f"req_{c}_{p}")
    
    for p in prep_time:
        m.addConstr(
            y[p] <= gp.quicksum(x[c] for c in cake_preps if p in cake_preps[c]),
            name=f"useful_{p}"
        )
        
    m.optimize()
    
    if m.status != GRB.OPTIMAL:
        return None
    
    selected_cakes = [c for c in cake_value if x[c].X > 0.5]
    selected_cakes.sort()
    total_joy = int(m.ObjVal)
    
    return total_joy, selected_cakes
    


def main():
    T, prep_time, cake_value, cake_preps = read_data()
    result = solverIHardlyKnowHer(T, prep_time, cake_value, cake_preps)
    
    if result is None:
        print("No Solution Found :(")
        return
    total_joy, cakes = result
    print(",".join([str(total_joy)] + cakes))
    
main()