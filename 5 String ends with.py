# My # Best
def solution(text, ending):
    return text.endswith(ending)

print(solution("abc", "bc"))
print(solution("abc", "d"))