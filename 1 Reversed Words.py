# My
def reverse_words(string):
    words = string.split(" ")

    string = ""
    for item in reversed(words):
        string+= item + " "
    return string[:-1]

# Best
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])

s = "The greatest victory is that which requires no battle"
print (reverse_words(s))


