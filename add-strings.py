# docs: https://docs.google.com/document/d/1RZXplVhLVJQw0lx0islOxvjOLIgNnMcMIVu9W8dKvQ4/edit
def insert_left_zeros( num, num_zeros):
    return (num_zeros*"0") + num

def remove_left_zeros(  num):
    num_without_left_zeros = ""
    start_of_number = 0

    for index in range(len(num)):
        if num[index] != '0':
            start_of_number = index
            break

    return num[start_of_number:]


def total_string_integers(  num1, num2):
    int_a = 0 # top digit
    int_b = 0 # bottom digit
    carry = 0 # carry
    total = ''

    num1  = remove_left_zeros(num1)
    num2  = remove_left_zeros(num2)

    if len(num1) > len(num2):
        num2 = insert_left_zeros(num2, len(num1) - len(num2))
    else:
        num1 = insert_left_zeros(num1, len(num2) - len(num1))

    int_part = 0
    tmp_total = 0
    for index in range(-1, -len(num1)-1, -1):
        tmp_total = int(num1[index]) + int(num2[index]) + int(carry)
        
        if tmp_total > 9:
            int_part = str(tmp_total)[1]
            carry = str(tmp_total)[0]
        else:
            int_part = str(tmp_total)
            carry = 0
        
        total = str(int_part + total)
    
    return (str(carry) + total) if int(carry) > 0 else total

assert total_string_integers("123", "45") == "168"