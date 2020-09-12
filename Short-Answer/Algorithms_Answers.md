#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) The variable a is being multiplied  by 2 X 2, this cancels the 2 x 2 in the parameter. Leaving only `while a <  n` to be compared.


b) O(logn) The inner loop with variable `j` is being incremented by i^2(in essence), decreasing the amount of loops required to reach n.


c) O(n^2) As the function recurses (until it reaches the base case of 0), then the recurssion part of the equation will add 2 to the bunnyEars() function. i.e. it will double the time taken to execute the function.

## Exercise II

using `binary search`, the function `find_floor_f` will do th following:

- find the middle floor of the nth story building
    - drop eggs
    - if eggs do not break:
        - store the current floor in the variable `floor_f`
        - run the `find_floor_f` function again
    - if eggs `do break`:
        - stop the function and return the last stored value 
            of `floor_f` (i.e. as the answer)
 
The run time for this function would be O(log(n))  since an increase in the nth number of floor would result in at most 1 more computation and at least 0 more computations.
The function is also halving the number of n floors to reach the desired floor f. 

