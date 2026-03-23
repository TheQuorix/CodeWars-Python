def generate_hashtag(s):
    output = '#' + s.title().replace(' ', '')

    if len(output) > 140 or output == '#':
        return False
    return output

print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag("LoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooongCat"))
