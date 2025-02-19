# Recursion - stringifyNumbers

# Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!

# Examples

# obj = {
#   "num": 1,
#   "test": [],
#   "data": {
#     "val": 4,
#     "info": {
#       "isRight": True,
#       "random": 66
#     }
#   }
# }
 
# stringifyNumbers(obj)
 
# {'num': '1', 
#  'test': [], 
#  'data': {'val': '4', 
#           'info': {'isRight': True, 'random': '66'}
#           }
# }  

def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj