# Program used to determine if a given pattern matches a given word
# By Deon Fourie
# 21 April

def match(pattern, word):
    if len(pattern) == 0 and len(word) == 0:
        return True
    if (len(pattern) == 1 and word[0] == "?") or (len(word) == 1 and pattern[0] == "?"):
        return True
    if (len(pattern) > 1 and pattern[0] == "?") or (len(pattern) != 0 and len(word) != 0 and pattern[0] == word[0]):
        return match(pattern[1:], word[1:])
    return False

