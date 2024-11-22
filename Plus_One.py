'''
arr = [1,2,3]
string_map = list((map(str,arr)))
print(string_map)

int1 = (''.join(string_map))
number = int(int1)
string_map = [int(digit) for digit in number]
print(string_map)
'''
arr = [1, 2, 3]

# Convert each element to a string and store in a list
string_map = list(map(str, arr))
print(string_map)  # Output: ['1', '2', '3']

# Join the string elements and convert them back to an integer
int1 = ''.join(string_map)
number = int(int1)

# Add 1 to the integer
number += 1  # Now the number is 124

# Convert the new integer back into a list of digits
string_map = [int(digit) for digit in str(number)]  # Iterate over str(number)
print(string_map)  # Output: [1, 2, 4]








