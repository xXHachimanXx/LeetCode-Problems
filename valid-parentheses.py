# docs: https://docs.google.com/document/d/1uJXV3lfrIlYvh8SRd8CyXaQXLY_47iCKAw1axasH7Ng/edit
def is_open( char):
    return char == '(' or char == '[' or char == '{'

def get_close_char_by_open_char( char):
    if char == '(':
        return ')'
    if char == '[':
        return ']'
    if char == '{':
        return '}'

def get_open_char_by_close_char( char):
    if char == ')':
        return '('
    if char == ']':
        return '['
    if char == '}':
        return '{'
        
def is_a_valid_string( string):
    stack_open = []
    stack_close = []

    if len(string) < 2:
        return False
    
    for char in string:
        if is_open(char):
            stack_open.append(char)
        else:
            if len(stack_open) == 0: return False

            temp = stack_open.pop()
            if temp != get_open_char_by_close_char(char): return False
        

    return len(stack_open) == 0

assert is_a_valid_string("([)]") == False
assert is_a_valid_string("()[]{}") == True