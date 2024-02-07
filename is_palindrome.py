def is_palindrome(word):
    return word == word[::-1]

# def is_palindrome(word):
#     reverseword = ''
#     for char in word:
#         reverseword=char+reverseword
#     print(reverseword)
#     if word ==  reverseword:
#         return True

print(is_palindrome('oko'))