# Docs: https://docs.google.com/document/d/1AVC-4QqkpMBKVUo306-ojkOKmmcJvRSu1AAQjlbxZ7I/edit
def find_max_consecutive_ones(nums) -> int:
    counter = 0
    max_count = 0
    for num in nums: # [1, 1, 0, 1, 1, 1]
        if num == 1:
            counter += 1 # 3
        else:
            max_count = counter if counter > max_count else max_count # 2
            counter = 0
    max_count = counter if counter > max_count else max_count

    return max_count

assert find_max_consecutive_ones([1,1,0,1,1,1]) == 3
assert find_max_consecutive_ones([1]) == 1