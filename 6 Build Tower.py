# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/python

# My
def tower_builder(n_floors):
    tower = []
    width = 2 * n_floors - 1
    for i in range(n_floors):
        stars = 2 * i + 1
        space = (width - stars) // 2
        floor = ' ' * space + '*' * stars + ' ' * space
        tower.append(floor)
    return tower

# Best
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

print(tower_builder(3))
print(tower_builder(6))