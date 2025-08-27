# My
def is_isogram(string):
    symbols = []
    for item in string:
        if item.lower() in symbols:
            return False
        symbols.append(item.lower())
    return True

# Best
def is_isogram(string):
    return len(string) == len(set(string.lower()))


s = "Dermatoglyphics"
print(f"{s} --> {is_isogram(s)}")
s = "aba"
print(f"{s} --> {is_isogram(s)}")
s = "moOse"
print(f"{s} --> {is_isogram(s)}")