# A more advance version of simplematch.py
# By Deon Fourie
# 25 April

def match(pattern, word):
    #for a '?' wildcard
    if len(pattern) == 0 and len(word) == 0:
        return True
    if (len(pattern) == 1 and word[0] == "?") or (len(word) == 1 and pattern[0] == "?"):
        return True
    if (len(pattern) > 1 and pattern[0] == "?") or (len(pattern) != 0 and len(word) != 0 and pattern[0] == word[0]):
        return match(pattern[1:], word[1:])
    #for a '*' wildcard
    if pattern == "*" and len(word) >= 1:
        return True
    if len(pattern) > 1 and pattern[0] == '*' and len(word) == 0:
        return False
    if len(pattern) != 0 and pattern[0] == "*":
        return match(pattern[1:], word) or match(pattern, word[1:])
    return False

