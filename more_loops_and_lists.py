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

# Write a function that counts how many numbers are divisible by ten from a list of numbers. 
# This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. 
# Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. 
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# You are invited to a social gathering, but you are tired of greeting everyone there. 
# Luckily we can create a function to accomplish this task for us. 
# In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name.
#Write your function here
def add_greetings(names):
  greeting_list = []
  for name in names:
    greeting_list.append("Hello, " + name)
  return greeting_list

print(add_greetings(["Owen", "Max", "Sophie", "Sam"]))

# Let’s try a tricky challenge involving removing elements from a list. 
# This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. 
# It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. 
#Write your function here
def delete_starting_evens(my_list):
  while (my_list[0] % 2 == 0):
    my_list.pop(0)
    if len(my_list) < 1:
      break
  return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# This next function will give us the values from a list at every odd index. 
# We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. 
# Return the list of elements which we got from the odd indices
#Write your function here
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
      new_list.append(my_list[index])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. 
# If the sum of the elements of each list are equal, return lst1.

#Write your function here
def larger_sum(lst1, lst2):
  total_list1 = 0
  total_list2 = 0
  for number in lst1:
    total_list1 += number
  for number in lst2:
    total_list2 += number
  if total_list1 >= total_list2:
    return lst1
  return lst2 

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [6, 3, 7]))

# Create a function called username_generator take two inputs, first_name and last_name and returns a user_name. 
# The username should be a slice of the first three letters of their first name and the first four letters of their last name.
# Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the 
# right, so the last letter of the username ends up as the first letter and so forth. 
# For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.
def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

def password_generator(user_name):
  password = ""
  password = password + user_name[-1]
  password = password + user_name[:-1]
  return password

print(password_generator("AbeSimp"))

# rewrite password_generator utilising a loop to iterate through user_name characters
def password_generator(user_name):
  password = ""
  index = 0
  password = password + user_name[-1]
  for characters in range(0, len(user_name)):
    password += user_name[index]
    index += 1
    if user_name[index] == user_name[-1]:
      return password

print(password_generator("AbeSimp"))