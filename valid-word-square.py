def is_valid_word_square(matrix):
    for index, word in enumerate(matrix):
        temp_str = ""
        for char_index in range(len(word)):
            if char_index <= len(matrix[char_index])+1:
                temp_str = temp_str + matrix[char_index][index]
            else:
                return False

        if temp_str != word : return False
    return True

assert is_valid_word_square([
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]) == True

assert is_valid_word_square([
  "abcd",
  "bnrt",
  "crm",
  "dt"
]) == True

assert is_valid_word_square([
  "ball",
  "area",
  "read",
  "lady"
]) == False