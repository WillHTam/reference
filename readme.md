# Programming, Algorithms, and Other

My notes from:

* MITx 6.00.1  _Introduction to Computer Science_
  * NO Midterm or Final Exam questions are included here.
* MITx 6.00.2  _Introduction to Computational Thinking and Data Science_
* Grokking Algorithms _by Aditya Y. Bhargava_
* Python Masterclass _by Jose Salvatierra on Udemy_

Notes:

* Defensive Programming
  * Write out docstrings!
  * Modularize
    * The breaking up of a big function into smaller ones which are easier to parse and test
  * Check conditions with assertions
    * Testing / Validation
      * Compare input / output
      * 'How can I break my program?'
    * Debugging
      * Study events that led up to the error
* Operation precedence (leftmost will eval first)
  * `** > * > / > + or -`
* Floats in Python
  * If there is no integer p such that `x*(2**p)` is a whole number, then internal representation is always an approximation
  * Therefore to strictly test equality do not use `x == y` which tests the binary equality
  * Instead test for  `abs(x - y) < a_sufficiently_small_number`use
* Lists in Python
  * When looping over another list and also performing mutations, clone the list first
    * `clone = list[:]`
  * Python uses an internal counter to keep track of the index it is in the loop
  * mutating the list length does not automatically update the counter
    * Therefore it is essential to clone the base list to iterate over first
  * doing `list2 = list1` creates a pointer to the first list
    * ie `list2 is list1` evaluates to True
    * so `list2.append()` will affect list1 and vice-versa
    * `l1 + l2` can also be expressed as `l1.extend(l2)` (extend more expensive)
  * `sorted(list)` will return a new sorted list
    * `list.sort()` will mutate the original
  * same applies to `reversed(list)` / `list.reverse()`
* Dictionaries in Python
  * use `from collections import DefaultDict' to simply adding to dictionary
    * `dict[key] += 1` can be used even if the dict does not exist
  * use dict.get(key, default) to try to get the key's value, and return default if it does not exist
