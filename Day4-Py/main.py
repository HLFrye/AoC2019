def valid(code):
    double_found = False
    never_decreases = True
    for i in range(0, len(code) - 1):
        curr = code[i]
        next = code[i+1]
        if curr == next:
            double_found = True
        if curr > next:
            never_decreases = False
    return double_found and never_decreases

def main():
    range_start = 206938
    range_end = 679128
    count = 0
    for code in range(range_start, range_end):
        if valid(str(code)):
            count += 1
    print(count)

if __name__ == "__main__":
    main()