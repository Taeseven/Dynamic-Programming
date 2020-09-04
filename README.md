# Dynamic Programming
> * Derived from Cornell Tech CS5112 2019 Fall, offered by Prof. Ramin.
> * Codes based on python2

## Diffing with Costs
-----------------------------
The goal is to align two string, $s$ and $t$, in a way to produce *minimum-cost* alignment. To produce such alignment, we insert the special character '-' some number of times into each string to produce **align_s** and **align_t** so that:  
> * **align_s** and **align_t** have the same length
> * There is no $i$ such that $align\_s[i]$ and $align\_t[i]$ are both '-'.

The cost of an alignment is given by a cost function, which we call **cost**. The cost of an alignment is the sum over all $i$ of $cost(align\_s[i], align_t[i])$. The cost of aligning a letter with itself is always 0.  

This problem arises, for example, in DNA sequencing; given two strands of DNA, there are many sequences of mutations (insertions, deletions, etc.) which would have transformed one to the other; we would like to find the most probable. We know that certain mutations are more likely than other， and these probabilities are reflected in the cost table(the pair with higher likelihood has a lower cost).


## Respacing
-----------------------------
The respacing problem is to put spaces back into a string that has lost them, given a dictionary. For example, given the string "itwasthebestoftimes" and an English dictionary, we would like to
reconstruct the original sentence: "it was the best of times".
