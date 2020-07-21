#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n) since 2 `n`s can be taken out of the function as they are repetitive. We would have one `n` variable in the while loop, so the output will increase so long as `n` (the input) increases as well.


b)  O(logn) since the inner loop with the variable `j` is being incremented by `i^2`(in essence), hence decreasing the amount of loops required to reach `n` . 

c)  O(n^2) because if the argument for `bunnies` is not 0 (which is a low probablility), then as the function recurses (until it reaches the base case of 0), then the recurssion part of the equation will add `2` to the `bunnyEars()` function. i.e. it will double the time taken to execute the function 

## Exercise II

using `binary search`, the function `find_floor_f` will do th following:

- find the middle floor of the nth story building
    - drop eggs
    - if eggs do `not break`:
        - store the current floor in the variable `floor_f`
        - run the `find_floor_f` function again
    - if eggs `do break`:
        - stop the function and return the last stored value 
            of `floor_f` (i.e. as the answer)
 
The run time for this function would be O(log(n))  since an increase in the nth number of floor would result in at most 1 more computation and at least 0 more computations.
The function is also halving the number of n floors to reach the desired floor f. 