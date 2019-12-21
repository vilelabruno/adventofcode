passwds = []
for i in range(265275,781584):
    finalSameDigit = False
    sameDigit = False
    flag = False
    decrease = False
    oldLt = -1
    for lt in str(i):
        lt = int(lt)
        if oldLt != lt:
            if sameDigit:
                finalSameDigit = True
            flag = False
        if oldLt == lt:
            if flag:
                sameDigit = False
            else:
                sameDigit = True
                flag = True
            
        if oldLt > lt:
            decrease = True
        oldLt = lt
    if not finalSameDigit:
        finalSameDigit = sameDigit
    if (not finalSameDigit) or decrease:
        continue
    else:
        passwds.append(str(i))    

        #print(lt)
print((passwds))
print(len(passwds))