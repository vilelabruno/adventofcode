def compile_intprogram(intprogram):
  pc = 0
  end_of_program = False
  while(not end_of_program):
    print(intprogram[pc])
    if intprogram[pc] == 1:
      intprogram[intprogram[pc+3]] = intprogram[intprogram[pc+1]] + intprogram[intprogram[pc+2]]
    elif intprogram[pc] == 2:
      intprogram[intprogram[pc+3]] = intprogram[intprogram[pc+1]] * intprogram[intprogram[pc+2]]
    elif intprogram[pc] == 99:
      end_of_program = True
    else:
      print("ERROR: Undefined '" + str(intprogram[pc]) +"' opcode on position " + str(pc) + ". Something went wrong!")
    pc += 4
  return intprogram

f = open("input.txt", 'r')
intprogram = [int(x) for x in f.readline().split(",")]

intprogram = compile_intprogram(intprogram)
print("Output: " + str(intprogram[0]))