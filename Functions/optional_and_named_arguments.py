'''
Example of function with optional and named arguments
'''

def fancy(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy(4, char2='#'))