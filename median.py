# -*- coding: utf-8 -*-
#
"""
Data structure for median
Write a data structure that supports two operations.
1. Adding a number to the structure.
2. Calculating the median.
The solution can be in any language, but there are things we value:
1. Written in C++ (CMake for build system).
2.  Well-structured code. Easy to read and understand.
3. There are automatic tests.
4. Hosted on  github.com (or  bitbucket.com, or  gitlab.com).
5. The operations to add a number and calculate the median have a minimum time complexity.


Adding a number to the structure and calculating the median are clear requirements and at the same time
are open to a myriad of implementation interpretations.

Hence, the programming of language of choice is Python and the internal data storage types as well as
standard library functions have been chosen to perform the task.

The reason behind this is that they have been optimized for speed and simplicity of use as well, of course, as maximal
readability of the code itself.

"""

# ======================================================================
# Library Declarations as needed
import statistics
import sys
import os
# ======================================================================
# Variable Declarations/Initializations as needed
med = []

def input_and_calculate(*args):
    '''
    This function calculates the median. The user is prompted to enter numbers separated by space.
    If the user wants to call it outside of this script, after importing, the user needs to pass a TUPLE of NUMBERS!

    :return: Median in float format
    '''
    if len(args) < 2:
        raise ValueError('User did not give sufficient number of arguments!')

    current_file = __file__
    # Parsing arguments
    if current_file in args[0]:
        argument_list = args[1:]
    else:
        argument_list = args


    # Attempting to gather the input from the user and do a sanity check against it..
    try:
        for number in argument_list:
            med.append(float(number))
    except ValueError:
        print('User did not enter valid input. Please enter VALID NUMBERS next time!!!\n')
        raise
        return False



    # Additional sanity checks
    for item in med:
        if item != 0.0:
            abs_val = abs(item)
            test_val = str(abs_val).replace(".", "", 1)
            if not test_val.isdigit():
                print('{} is not a valid digit, I cannot calculate the median properly when one or more items is invalid, leaving'.format(item))
                return False


    # Outputing the median
    return statistics.median(med)

if __name__ == '__main__':
    medi = input_and_calculate(*sys.argv)
    if medi is False:
        print('There was an error in the program, leaving')
    else:
        print('The median of the numbers given is', medi)


