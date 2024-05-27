def reverse_string(s):

# Base case: if the string is empty or has only one character, return it as is

    if len(s) <= 1:

        return s

# Recursive case: call the function with the substring excluding the first character,

# then concatenate the first character at the end

    return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))     

print(reverse_string("python")) 

print(reverse_string("Samten Thinlay"))