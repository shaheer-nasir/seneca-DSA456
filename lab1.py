# SHAHEER NASIR (SGNASIR / 021842158) #
# DSA456V1B #
# PROF: Veria Havary-Nassab #
# SEPT 21, 2024 #

# Function 1
def wins_rock_scissors_paper(p1, p2):
    
    # convert input to lower to remove case sensitivity
    p1 = p1.lower()
    p2 = p2.lower()
   
    # results based on input
    if p1 == "rock" and p2 == "scissors":
        return True
    elif p1 == "paper" and p2 == "rock":
        return True
    elif p1 == "scissors" and p2 == "paper":
        return True
    else:
        return False

# Function 2
def factorial(n):
    
    # if !0, return 1
    if(n == 0):
        n = 1

    # store value for loops
    # - 1 so n does not multiply the value to itself
    i = n - 1
    
    # loop for factorial function
    for _ in range(i):
        n = n * i
        
        # equivalent to (n - 1) 
        i = i - 1
        
    return n

# Function 3
def Fibonacci(n):
    n1 = 1 # next pos
    n2 = 0 # prev pos
    sum = 0 # prev 2 pos

    # validation
    if(n == 2):
        return 1

    # loop to calculate fib 
    for _ in range(n):
        sum = n1 + n2
        n2 = n1
        n1 = sum
    
    return sum

# Function 4
def unique_values(n):
    
    # user input is stored in list
    value = []
    dupe = False
    i = 0

    while i < n:

        num_input = int(input("Enter a value: "))

        # check to see dupe in list
        for x in value:
            if(num_input == x):
                dupe = True
            else:
                dupe = False
        
        # if dupe exists, display error & add remove 1 from loop
        if(dupe):
            print("ERROR: Number already exists")
            i -= 1

        # if no dupe, append to list
        else:
            value.append(num_input)

        i += 1

    # sort list
    value.sort()

    return value
