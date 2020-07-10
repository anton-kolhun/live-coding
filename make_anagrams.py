"""
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form
the second string. In other words, both strings must contain the same exact letters in the same exact frequency

Given two strings, a and b that may or may not be of the same length, determine the minimum number of character
deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

For example, if a = 'cde' and b = 'dcf' we can delete 'e' from string A and 'f' from string B
so that both remaining strings are 'cd' and 'dc'  which are anagrams.
"""


def makeAnagram(a, b):
    # TODO: your implementation goes her
    return 0


if __name__ == '__main__':
    result = makeAnagram('etst', 'test2')
    assert result == 1, '"etst" is converted to "test" with 0 deletions. "test2" is converted to "test" with 1 deletion'
