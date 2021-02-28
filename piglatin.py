vowels = ("a", "e", "i", "o", "u")


def split_word(word):
    words_in_word = word.split()
    return words_in_word

def add_way(word):
    word = word + "way"
    return word

def add_a(word):
    word = word + "a"
    return word

def add_consonants(word):
    for i in word:
        if i not in vowels:
            word = word[1::] + word[0]
        elif i in vowels:
            break
    return word

def add_ay(word):
    word = word + "ay"
    return word

def remove_way(word):
    word = word[:-3]
    return word

def remove_ay(word):
    word = word[:-2]
    return word

def remove_a(word):
    word = word[:-1]
    return word

def remove_consonants(word):
    for i in word:
        if word[-1] not in vowels:
            word = word[-1] + word[:-1]
    return word

def to_pig_latin(sentence):
    new_sentence = ""
    sentence = split_word(sentence)
    for m in sentence:
        if m[0] in vowels:
            m = add_way(m)
            new_sentence = new_sentence + m + " "
        else:
            m = add_a(m)
            m = add_consonants(m)
            m = add_ay(m)
            new_sentence = new_sentence + m + " "
    return new_sentence

def to_english(sentence):
    new_sentence = ""
    sentence = split_word(sentence)
    for m in sentence:
        if m[-3::] == "way":
            m = remove_way(m)
            new_sentence = new_sentence + m + " "
        else:
            m = remove_ay(m)
            m = remove_consonants(m)
            m = remove_a(m)
            new_sentence = new_sentence + m + " "
    return new_sentence











