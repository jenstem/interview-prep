# Recursion - nestedEvenSum

# Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an object which may contain nested objects.

# Examples

# obj1 = {
#   "outer": 2,
#   "obj": {
#     "inner": 2,
#     "otherObj": {
#       "superInner": 2,
#       "notANumber": True,
#       "alsoNotANumber": "yup"
#     }
#   }
# }
 
# obj2 = {
#   "a": 2,
#   "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
#   "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
#   "d": 1,
#   "e": {"e": {"e": 2}, "ee": 'car'}
# }
 
# nestedEvenSum(obj1) # 6
# nestedEvenSum(obj2) # 10

# takes 2 params, object and initialize sum to 0
def nestedEvenSum(obj, sum=0):
    # iterate through the keys in the dict of objects
    for key in obj:
        # if the value of the current key is another dict
        # that means it is a nested object
        # call the function recursively and pass the nested object
        # and the sum to the function
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
            # checks if value is even by dividing by 2
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            # add the value to the sum
            sum += obj[key]
    return sum