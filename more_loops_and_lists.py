# Write a function that creates a list of numbers up to 100 in increments of 3 
# starting from a number that is passed to the function as an input parameter. 
# The function should return a list of every third number between start and 100 (inclusive).
# Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))
print(every_three_nums(87))

# Create a function will remove all elements from a list with an index within a certain range. 
# The function will accept a list, a starting index, and an ending index. 
# All elements with an index between the starting and ending index should be removed from the list. 
#Write your function here
def remove_middle(my_list, start, end):
  del my_list[start: (end + 1)]
  return my_list

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# We have a conveyor belt of items where each item is represented by a different number. 
# We want to know, out of two items, which one shows up more on our belt. 
# To solve this, we can use a function with three parameters. 
# One parameter for the list of items, another for the first item we are comparing, and another for the second item. 
# If the two items appear the same number of times, return item1.
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item2) > my_list.count(item1):
    return item2
  return item1 

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Our next function will double a value at a given position. We will provide a list and an index to double. 
# This will create a new list by replacing the value at the index provided with double the original value. 
# If the index is invalid then we should return the original list. 
# Write your function here
def double_index(my_list, index):
  if index > (len(my_list) - 1):
    return my_list
  doubled_index = (my_list.pop(index)) * 2
  my_list.insert(index, doubled_index)
  return my_list

print(double_index([3, 8, -10, 12], 3))

# For the next code challenge, we are going to create a function that finds the middle item from a list of values. 
# This will be different depending on whether there are an odd or even number of values. 
# In the case of an odd number of elements, we want this function to return the exact middle value. 
# If there is an even number of elements, it returns the average of the middle two elements.
#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    half_list_length = int(len(my_list)/2)
    return (my_list[half_list_length] + my_list[half_list_length - 1]) / 2
  else:
    return my_list[int(len(my_list)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))