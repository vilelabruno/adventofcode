with open("input.txt", "r") as f:
    total = 0
    for l in f:
        print(l)
        mass= float(l)
        fuel = 0
        currentFuel = int(mass/3.0) - 2
        while currentFuel > 0:
            fuel = fuel + currentFuel
            currentFuel = int(currentFuel/3.0) - 2
        total = total + fuel
        print(fuel)
print (total)