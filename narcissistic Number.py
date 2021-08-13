# Narcissistic Number
 
# Defining a function
def narcissistic_number():
    total = 0 # set a variable  and make it 0
    number = int(input()) # Ask user to enter and convert it into INT
    for digit in str(number): # use For loop to pick a digit and use str() Here digit will be str
        total = total + int(digit) ** len(str(number)) # Convert digit into int and find the len of the number
    # then do exponentiation. The loop automatically saves it to total var
    return total == number # return total and check if the number equals total
    
print(narcissistic_number()) # call the function and print the output which returned from the 					function


# 2nd method(shortcut and minimum lines) using list comprehension
def narcissistic_number():
    number = int(input())
    return number == sum([int(digit) ** len(str(number)) for digit in str(number)])

print(narcissistic_number())

