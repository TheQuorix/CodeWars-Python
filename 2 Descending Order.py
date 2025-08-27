# My # Best
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

s = 1201
print(descending_order(s))