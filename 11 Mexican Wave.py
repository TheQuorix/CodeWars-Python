def wave(people):
    output = []

    for i, char in enumerate(people):
        if char == " ": continue

        output.append(people[:i] + char.upper() + people[i+1:])

    return output

print(wave("hello"))
print(wave(" s p a c e s "))
print(wave(""))
