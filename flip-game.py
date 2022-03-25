
# docs: https://docs.google.com/document/u/1/d/1M8zHQEA06npXP3nIFrBPZPSZae84064COyc5KL8pQXc/edit?usp=drive_web&ouid=107472081058632220123
def flip_char(char):
	    return '-' if char == '+' else '+'

def flip_string(input_str): # ---+++-+++-+
    ptr_left = 0
    ptr_right = 1
    flipped_strings = []

    # ---+++-+++-+
    for counter in range(len(input_str)-1): # --
        temp_str = list(input_str)
        if input_str[ptr_left] == input_str[ptr_right] == '+': #
            temp_str[ptr_left] = self.flip_char(input_str[ptr_left]) 
            temp_str[ptr_right]  = self.flip_char(input_str[ptr_right]) 
            flipped_strings.append("".join(temp_str)) # --

        ptr_left += 1
        ptr_right += 1
        
    return flipped_strings # 

assert flip_string("++++") == [
  "--++",
  "+--+",
  "++--"
]

assert flip_string("---+++-+++-+") == [
	"---+++-+---+",
	"---+++---+-+",
	"---+---+++-+",
	"-----+-+++-+"
]