# Algorithms & Other

My material from:

* MITx 6.00.1  _Introduction to Computer Science_
  * NO Midterm or Final Exam questions are included here.
* MITx 6.00.2  _Introduction to Computational Thinking and Data Science_
  * NO Midterm or Final Exam questions are included here.
* Grokking Algorithms _by Aditya Y. Bhargava_
* Python Masterclass _by Jose Salvatierra on Udemy_

Notes:

* Operation precedence
  * `** > * > / > + or -`
* Floats in Python
  * If there is no integer p such that `x*(2**p)` is a whole number, then internal representation is always an approximation
  * Therefore to strictly test equality do not use `x == y` which tests the binary equality
  * Instead test for  `abs(x - y) < a sufficiently small number`
* Lists in Python
  * When looping over another list and also performing mutations, clone the list first
  * Python uses an internal counter to keep track of the index it is in the loop
  * mutating the list length does not automatically update the counter
    * Therefore it is essential to clone the base list to iterate over first
  * doing `list2 = list1` creates a pointer to the first list
    * ie `list2 is list1` evaluates to True
    * so `list2.append()` will affect list1 and vice-versa
    * `l1 + l2` can also be expressed as `l1.extend(l2)` (extend more expensive)
  * `sorted(list)` will return a new sorted list
    * `list.sort()` will mutate the original 
  * same applies to `reversed()` / `.reverse()`