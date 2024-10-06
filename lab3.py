# SHAHEER NASIR (021842158) #
# DSA456V1B #
# OCT 2, 2024 # 

## PART A ##

# factorial
def factorial(n):
    if n == 0: 
        return 1 
    
    return n * factorial(n-1)  

# linear search
def linear_search(list, key, i=0): # added i=0 for index as a default parameter
    if(list[i] == key): 
        return i 
    
    return linear_search(list, key, i+1) 

# binary search
# not sure how to get index 
def binary_search(lst, key):
  # out of array
  if len(lst) == 0:
    return -1

  # middle of array
  mid = len(lst) / 2
  mid = int(mid)

  # if found, return index
  if key == lst[mid]:
    return len(lst)

  # if key is less than middle, go left
  if key < lst[mid]:
    return binary_search(lst[:mid], key)

  # if key is more than middle, go right
  if key > lst[mid]:
    return binary_search(lst[mid:], key)

# hanoi
def hanoi(n, src, des, aux):
    if n>0:
        hanoi(n-1, src, aux, des)
        print("Moved Disk [" + str(n) + "] from " + src + " to " + des)
        hanoi(n-1, aux, des, src)


## PART B ##

# function 1 analysis
def function1(value, number): 
     if (number == 0): # 1
            return 1
     elif (number == 1): # 1
            return value
     else:
            return value * function1(value, number-1) # O(n)

#  The time complexity for this function is O(n)
#  T(n) = O(n-1) + 3
#  Simplified to O(n), we drop the constants
#  The reason why it's O(n) and not a constant function is because of number - 1

# function 2 analysis
def recursive_function2(mystring,a, b):
     if(a >= b ): # base case 
            return True
     else:
            if(mystring[a] != mystring[b]): # 1
                  return False
            else:
                  return recursive_function2(mystring,a+1,b-1) # O(n)

def function2(mystring):
     return recursive_function2(mystring, 0,len(mystring)-1) # 1

# recursive_function2 checks to see if index characters match
# else it moves the index closer to eachother +1 => <= -1
# function2 returns total string length - 1, this is a constant.
# the time complexity of this function is O(n)
# recursive_function2 is linear time as it increases the number of operators based off length

# function 3 
# T(n) = T(n/2) + 3
# T(n/2) = T(n/2) + 3
# T(n/4) + 6
# T(n/8) + 9
# T(n/2) + 3 is simplified to O(log n)