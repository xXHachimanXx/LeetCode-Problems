# docs: https://docs.google.com/document/d/1Yy2vGYDVU2OIewCPxTnzZK4Cigx8SzcUj79opP93Bsc/edit
def plus_one(array):
    carry = 0
    for index in range(len(array) - 1, -1, -1): # num = 9 | carry = 1
        num = array[index] # 9
        if index == len(array) - 1: 
            num += 1

        num += carry # 9 + 1 = 10

        if num > 9: # num = 10
            unit_digit = num % 10 # 0
            carry = int((num - unit_digit)/10) # 1
            array[index] = int(unit_digit) # 0
        else:
            carry = 0
            array[index] = num
            break

    return [carry] + array if carry > 0 else array # [1, 0, 0, 0]

assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([9,9,9]) == [1,0,0,0]