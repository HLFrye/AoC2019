import math

def calculate_fuel(module_weight):
  fuel = 0
  weight = module_weight
  while True:
    new_fuel = math.floor(int(weight) / 3) - 2
    # For part 1, just return new_fuel here
    if new_fuel <= 0:
      return fuel
    fuel += new_fuel
    weight = new_fuel

def main():
  with open("./input.txt") as f:
    total = sum(map(calculate_fuel, f.readlines()))
  print(total)

if __name__ == '__main__':
  main()