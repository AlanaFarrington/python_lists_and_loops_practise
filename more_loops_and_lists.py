# Write a function that creates a list of numbers up to 100 in increments of 3 
# starting from a number that is passed to the function as an input parameter. 
# The function should return a list of every third number between start and 100 (inclusive).
# Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))
print(every_three_nums(87))