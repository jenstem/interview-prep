from array import array

# Create an array and traverse

my_array = array('i', [1,2,3,4,5,6,7,8,9])

my_list = [10,11,12]

# def traverse_array():
#     for i in my_array:
#         print(i)

# traverse_array()


# Access individual elements through indexes
# print(my_array[3])

# Append any value to the array using append() method

# my_array.append(10)
# print(my_array)

# Insert value in an array using insert() method

# my_array.insert(9, 10)
# print(my_array)

# Extend python array using extend() method

# my_array.extend([10,11,12])
# print(my_array)

# Add items from list into array using fromlist() method

my_array.fromlist(my_list)
print(my_array)