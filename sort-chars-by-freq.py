# docs: https://docs.google.com/document/d/1vHSy-bW-bL8LOynptVH_tay1Z314VZwhXvSll10GEzg/edit
def sort_chars_by_freq(string):
    string_list = [*string]  # list of chars
    output = ""
    letter_dict = {}

    for letter in string_list:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1

    letter_list = [(-v, k) for k, v in letter_dict.items()]

    letter_list.sort()

    for count, letter in letter_list:
        output += letter * (-count)
    return output

assert sort_chars_by_freq("tree") == "eert"
assert sort_chars_by_freq("cccaaa") == "aaaccc"
assert sort_chars_by_freq("Aabb") == "bbAa"