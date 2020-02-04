# FizzBuzz
##### Difficulty: Easy

## Problem statement
#### Description
# A classic Data Structures an algorithms problem, you are given an input array of integers from 1 to 100 (inclusive). 
# You have to write a fizzbuzz function that takes in an input array and iterates over it. When your function receives a number 
# that is a factor of 3 you should store 'Fizz' in the output array, if the number is a factor of 5 then you should store 'Buzz' in
# the output array. Additionally, if the number is a factor of both 3 and 5, you must store 'FizzBuzz' in the output array. For all other
# cases, you must store the numbers as they are. Return the output array from your function.

# Good Luck!

import numpy as np

def fizzbuzz(input_array):
    # Input list is an array of integers
    output_list = list(np.zeros(input_array.shape))
    
    # Iterating over input_list
    for i in range(len(input_array)):
        
        # If common factor of 3 and 5
        if (input_array[i] % 5 == 0) & (input_array[i] %3 ==0):
            output_list[i] = "FizzBuzz"
            
        # If common factor of 5
        elif (input_array[i] % 5 == 0):
            output_list[i] = "Buzz"
            
        # If common factor of 3
        elif (input_array[i] % 3 == 0):
            output_list[i] = "Fizz"
            
        # Otherwise store as original integer
        else:
            output_list[i] = input_array[i]

    return output_list

# Test data array of integers from 1 to 100
input_array = np.array(range(1, 101))
fizzbuzz(input_array)