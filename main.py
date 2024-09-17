#!/usr/bin/env python3
import gurobipy as g
import sys
 
 
if __name__ == "__main__":
    input_file = str(sys.argv[1])
    output_file = str(sys.argv[2])
    with open(input_file, 'r') as file:
        lines = file.readlines()
        d = list(map(int, lines[0].split()))
        e = list(map(int, lines[1].split()))
        D = int(lines[2])
    m = g.Model()
 
    xs = m.addVars(24 * 7, lb=0, vtype=g.GRB.INTEGER, name=[f"x{i}" for i in range(24 * 7)])
    z = m.addVars(24 * 7, lb=0, vtype=g.GRB.INTEGER)
 
    # Demand constraints for weekdays
    for i in range(len(d) * 5):
        m.addConstr(d[i % 24] - g.quicksum(xs[j % (24 * 7)] for j in range(i - 7, i + 1)) <= D)
        m.addConstr(d[i % 24] - g.quicksum(xs[j % (24 * 7)] for j in range(i - 7, i + 1)) <= z[i])
        m.addConstr(g.quicksum(xs[j % (24 * 7)] for j in range(i - 7, i + 1)) - d[i % 24] <= z[i])
        m.addConstr(z[i] >= 0)
 
    # Demand constraints for weekends
    for i in range(5 * 24, 5 * 24 + len(e) * 2):
        m.addConstr(e[i % 24] - g.quicksum(xs[j % (24 * 7)] for j in range(i - 7, i + 1)) <= D)
        m.addConstr(e[i % 24] - g.quicksum(xs[j % (24 * 7)] for j in range(i - 7, i + 1)) <= z[i])
        m.addConstr(g.quicksum(xs[j % (24 * 7)] for j in range(i - 7, i + 1)) - e[i % 24] <= z[i])
        m.addConstr(z[i] >= 0)
 
    m.setObjective(z.sum(), sense=g.GRB.MINIMIZE)
 
    m.optimize()
    if m.status == g.GRB.OPTIMAL:
        with open(output_file, 'w') as file:
            file.write(f"{int(m.objVal)}\n")
            file.write(" ".join(str(int(xs[i].x)) for i in range(24 * 7)))
