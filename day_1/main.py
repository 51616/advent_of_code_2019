import sys

def calc_fuel(weight):
    if weight<=0:
        return 0
    fuel = weight//3-2
    return max(0,fuel) + calc_fuel(fuel)

def part_one(inp):
    return sum([int(i)//3-2 for i in inp.split()])
    
def part_two(inp):
    return sum([calc_fuel(int(i)) for i in inp.split()])


if __name__=='__main__':
    inp = sys.stdin.read()
    out_1 = part_one(inp)
    out_2 = part_two(inp)
    print(f'Part one: {out_1}')
    print(f'Part two: {out_2}')
    
