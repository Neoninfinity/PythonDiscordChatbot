
"""Takes in a string and checks to see if its a valid integer"""
def is_number(s):
    if s.isdigit() == True: # isdigit is a function from the standard library
        return True
    else:
        return False
    
    
print(is_number("lol"))