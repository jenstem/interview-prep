# Recursion - reverse

# Write a recursive function called reverse which accepts a string and returns a new string in reverse.

# Examples

# reverse('python') # 'nohtyp'
# reverse('appmillers') # 'srellimppa'

def reverse(strng):
    if len(strng) == 0:
        return strng
    else:
        return strng[-1] + reverse(strng[:-1])


print(reverse('python'))
print(reverse('appmillers'))
