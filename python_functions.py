#Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
  print(n * (n + 1) // 2)

#Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

#largest([1, 2, 3, 4, 0])  # returns 4
#largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(nums):
  nums.sort()
  return nums[-1]

#Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string. 

#occurrences('fleep floop', 'e')   # returns 2
#occurrences('fleep floop', 'p')   # returns 2
#occurrences('fleep floop', 'ee')  # returns 1
#occurrences('fleep floop', 'fe')  # returns 0