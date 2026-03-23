def first_non_repeating_letter(s):
    s_lower = s.lower()
    for i, char in enumerate(s):
        if char.lower() not in s_lower[:i] + s_lower[i+1:]:
            return char
    return ''
