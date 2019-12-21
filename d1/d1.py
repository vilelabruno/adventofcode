with open("input.txt", "r") as f:
    total = 0
    for l in f:
        print(l)
        mass= float(l)
        fuel = int(mass/3.0) - 2
        total = total + fuel
        print(fuel)

print (total)