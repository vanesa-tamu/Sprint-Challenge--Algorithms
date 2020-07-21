'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    # TBC
    if len(word) < 2:
        return count
    elif word[:2] == 'th':
        count += 1
    # recursion
    return count_th(word[1:], count)


word = "abcthefthghith"
print(count_th(word))
