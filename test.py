import re

def solution(s):
    pattern = r"\w{2}"
    match = re.findall(pattern, s)
    if len(s) % 2 != 0:
        match.append(f"{s[-1]+'_'}")
    return match

print(solution("asdfadss"))
print(solution(""))