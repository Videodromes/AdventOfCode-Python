with open('2015/01_not_quite_lisp/input.txt', 'r', encoding="utf-8") as input:
    content = input.read()

# Part 1
def final_floor():
    return content.count('(') - content.count(')')

# Part 2
def first_basement():
    floor = 0
    index = 0
    for char in content:
        if floor == -1:
            return index
        else:
            if char == '(':
                floor += 1
                index += 1
            elif char == ')':
                floor -= 1
                index += 1

print(f"Part 1: {final_floor()}")
print(f"Part 2: {first_basement()}")
