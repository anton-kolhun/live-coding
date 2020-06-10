"""
Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time.
He wonders how many ways there are to reach the top of the staircase.


Given the respective heights for each of the  staircases in his house, find and print the number of ways
he can climb staircase

For example, there is a staircase in the house that is 5 steps high. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2

Therefore, there are 13 ways in total to reach the top
"""


def stepOptions(n):
    # TODO: your implementation goes her
    return -1


if __name__ == '__main__':
    result1 = stepOptions(3)
    assert result1 == 4, 'length of [111, 12, 21, 3] equals 4'

    result2 = stepOptions(5)
    assert result2 == 13, ''
