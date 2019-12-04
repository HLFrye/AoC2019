def process_path(line):
  pts = []
  curr = (0, 0)
  for instr in line.split(","):
    angle = instr[0]
    dist = int(instr[1:]) + 1
    if angle == 'R':
      for step in range(1, dist):
        curr = (curr[0] + 1, curr[1])
        pts.append(curr)
    elif angle == 'L':
      for step in range(1, dist):
        curr = (curr[0] - 1, curr[1])
        pts.append(curr)
    elif angle == 'U':
      for step in range(1, dist):
        curr = (curr[0], curr[1] + 1)
        pts.append(curr)      
    elif angle == 'D':
      for step in range(1, dist):
        curr = (curr[0], curr[1] - 1)
        pts.append(curr)     
  return pts 

def manhattan(coord):
  return abs(coord[0]) + abs(coord[1])

def compare_paths(path1, path2):
  pts = set(path1).intersection(set(path2))
  dists = list(map(manhattan, pts))
  dists.sort()
  return dists[0]

def main():
  with open("./input.txt") as f:
    path1 = process_path(f.readline())
    path2 = process_path(f.readline())
  print(compare_paths(path1, path2))

if __name__ == "__main__":
  main()