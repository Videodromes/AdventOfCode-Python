with open('2015/03_perfectly_spherical_houses_in_a_vacuum/input.txt', 'r', encoding='utf-8') as input:
    data = input.read()

x_pos, y_pos = 0, 0

def part1(x, y):
    grid = {(x, y)}
    
    for direction in data:
        if direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1
        elif direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        
        grid.add((x, y))
    
    return len(grid)

def part2(x, y):
    robo_x, robo_y = x, y
    grid_santa = {(x, y)}
    grid_robo = {(x,y)}
    
    for i, direction in enumerate(data):
        if i % 2 == 0:
            if direction == '^':
                y += 1
            elif direction == 'v':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == '<':
                x -= 1
            grid_santa.add((x, y))
        else:
            if direction == '^':
                robo_y += 1
            elif direction == 'v':
                robo_y -= 1
            elif direction == '>':
                robo_x += 1
            elif direction == '<':
                robo_x -= 1
            grid_robo.add((robo_x,robo_y))
    
    return len(grid_santa.union(grid_robo))

print(f"Part 1: {part1(x_pos, y_pos)}\nPart 2: {part2(x_pos, y_pos)}")
