# A program that checks if a string is a palindrome
# By Deon Fourie
# 21 April


def palindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return palindrome(word[1:-1])

def get_input():
    return input().lower()

def welcome():
    print("Enter a string:")

def main():
    welcome()
    word = get_input()
    if palindrome(word) is True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")

if __name__=='__main__':
    main()

