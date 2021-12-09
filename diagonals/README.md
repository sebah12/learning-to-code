<div align="right" style="text-align:right"><i>Sebastian Hernando
<br>2020-2021</i></div>

# 16 Diagonal Problem

This is a solution to the problem of filling a 5x5 board with diagonal lines in a way such that no line touch another one.
One way to solve this kind of problems is by finding all the possible combinations of lines on the board and checking wich ones are valid... good luck with that.


# About the solution

By no means this is the most efficient solution, it was written as an introductory problem to learn the backtraking approach to solving a problem.

First I define a class called "Board" to represent the empty board and various methods to interact with it.
Then there is a function named "fill_board" that starts to put lines on the board complying to the rules and trying to put 16 diagonals on it using backtracking.

# Backtracking

You can try to do it by hand, starting with an empty board and filling lines one by one. This would take you some time but you would do it this way. Maybe...
But we can automate this problem using code and implementing <a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a> is similar to the way you would do it by hand. 

