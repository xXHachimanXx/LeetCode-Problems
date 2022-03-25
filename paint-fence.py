# docs: https://docs.google.com/document/d/1atqUMZe43dCx28N4pvGVydRVU3RNklse2sEk69TYY_8/edit
def num_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k

    same = k
    diff = k * (k-1)

    for index in range(3, n+1):
        prev_diff = diff
        diff = (same + diff) * (k-1)
        same = prev_diff * 1

    return same + diff

assert num_ways(3, 2) == 6
assert num_ways(2, 2) == 4