# ten puzzle solver

Python 3.12.7

**possible(list[int], int)**
take in list of numbers and goal value, and will return boolean value based on if it is able to make goal number using list of numbers

**puzzle(list[int], int, bool)**
similar to possible, but will print ways to create the goal number
if *False* is given for the boolean, then function will suspend after one way is found

**createallset(int)**
return list of all numbers in given number of digits as string

**findall(list[str], goal)**
given the list of string of numbers, will return list that only include string of numbers that is possible to make the goal number

**testall(digit: int, goal: int)**
given the number of digits, will return set of strings that are possible to make the goal number, out of all possible numbers below that digit

note: this program is only intended for non-negative integers, and are not tested against negative integers or float

if the goal was 10, 4 digits took about 0.05 seconds, 5 digits took about 0.76 seconds, 6 digits took about 18.5 seconds to run tesetall() in my environment
