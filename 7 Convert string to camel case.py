# https://www.codewars.com/kata/517abf86da9663f1d2000003/python

# My
def to_camel_case(text):
    words = text.replace("-", "_").split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

# Best
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')



print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("the-Stealth_Warrior"))
print(to_camel_case("the_Stealth-Warrior"))