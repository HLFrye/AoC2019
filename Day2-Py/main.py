
def run_intcode(data):
  ptr = 0
  def read_value():
    nonlocal ptr
    res = data[ptr]
    ptr += 1
    return res

  def run_addition():
    arg1_loc = read_value()
    arg2_loc = read_value()
    dst_loc = read_value()
    arg1 = data[arg1_loc]
    arg2 = data[arg2_loc]
    data[dst_loc] = arg1 + arg2

  def run_multiplication():
    arg1_loc = read_value()
    arg2_loc = read_value()
    dst_loc = read_value()
    arg1 = data[arg1_loc]
    arg2 = data[arg2_loc]
    data[dst_loc] = arg1 * arg2

  while True:
    opcode = read_value()
    if opcode == 99:
      return data[0]
    elif opcode == 1:
      run_addition()
    elif opcode == 2:
      run_multiplication()
    else:
      raise Exception("What is this bullshit? " + opcode)
     
def main():
  with open("./input.txt") as f:
    data = list(map(int, f.readline().split(",")))

  # Modify data before run
  for noun in range(0, 99):
    for verb in range(0, 99):

      data[1] = noun
      data[2] = verb

      res = run_intcode(data.copy())
      if res == 19690720:
        print(noun * 100 + verb)
        return
  print("Couldn't find it")

if __name__ == "__main__":
  main()