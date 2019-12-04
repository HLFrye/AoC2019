def process_path(line):
  pts = {}
  steps = 0
  curr = (0, 0)
  for instr in line.split(","):
    angle = instr[0]
    dist = int(instr[1:]) + 1
    if angle == 'R':
      for step in range(1, dist):
        steps += 1
        curr = (curr[0] + 1, curr[1])
        if curr not in pts:
          pts[curr] = steps
    elif angle == 'L':
      for step in range(1, dist):
        steps += 1
        curr = (curr[0] - 1, curr[1])
        if curr not in pts:
          pts[curr] = steps
    elif angle == 'U':
      for step in range(1, dist):
        steps += 1
        curr = (curr[0], curr[1] + 1)
        if curr not in pts:
          pts[curr] = steps
    elif angle == 'D':
      for step in range(1, dist):
        steps += 1
        curr = (curr[0], curr[1] - 1)
        if curr not in pts:
          pts[curr] = steps
  # print(pts)
  return pts 

def manhattan(coord):
  return abs(coord[0]) + abs(coord[1])

def step_dist_func(path1, path2):
  def step_dist(coord):
    return path1[coord] + path2[coord]
  return step_dist

def compare_paths(path1, path2):
  step_dist = step_dist_func(path1, path2)
  pts = set(path1.keys()).intersection(set(path2.keys()))
  dists = list(map(step_dist, pts))
  dists.sort()
  return dists[0]

def run_input(filename):
  with open(filename) as f:
    path1 = process_path(f.readline())
    path2 = process_path(f.readline())
  print(compare_paths(path1, path2))


def main():
  run_input("./input.txt")

if __name__ == "__main__":
  main()