"""
Username  : lcastillov
Problem   : Day 11: Plutonian Pebbles (1)
Date      : 12/22/2024
Time      : ???
Execution : python3 part-one-version-1.py < input.txt
"""

import sys


def splits(n, d):
    if d == 0:
        return 1
    if n == 0:
        return splits(1, d - 1)
    s = str(n)
    if len(s) % 2 == 0:
        l = splits(int(s[: len(s) // 2]), d - 1)
        r = splits(int(s[len(s) // 2 :]), d - 1)
        return l + r
    return splits(2024 * n, d - 1)


if __name__ == "__main__":
    stones = list(map(int, sys.stdin.readline().split()))
    answer = sum(splits(n, 25) for n in stones)
    print(answer)
