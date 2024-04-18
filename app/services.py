"""
Jumbles the input string by shifting each letter by 'n' positions in the alphabet.
digits and spaces are preserved,
while all other characters are removed from the output.

Params:
s (str): The input string to be jumbled.
n (int): The number of positions to shift each letter in the input string.

Returns:
str: The jumbled string with letters shifted, and digits and spaces preserved.

"""
def jumble(s, n):
    if(n>1000):
        return "Shift error"
    
    result = []  
    for char in s:
        if char.isalpha():
            # get the base position         
            start = 'a' if char.islower() else 'A'  
            # Calculate the new character position with wrapping using mod 26.
            offset = (ord(char) - ord(start) + n) % 26
            # Append the shifted character to the result list with the shifting offset.
            result.append(chr(ord(start) + offset))

        elif char.isdigit() or char == ' ': 
            result.append(char)  
       

    return ''.join(result)  