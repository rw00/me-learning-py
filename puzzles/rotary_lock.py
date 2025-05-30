from typing import List

# You're trying to open a lock.
# The lock comes with a wheel which has
# the integers from 1 N arranged in a circle in order
# (integers 1 and N are adjacent to one another). 
# The wheel is initially pointing at 1.

# Determine the minimum number of rotations required to select all 
# M of the code's integers in order.
def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    result = 0
    current = 1
    for code in C:
        change = 0
        if code < current:
            change = min(current - code, N - current + code)
        elif code > current:
            change = min(code - current, N - code + current)
        result += change
        current = code
    return result
