# Functional python examples

refactored kaa-the-wise's one line aoc solutions. Much of the solutions are pure functional showing how to use accumulate (i.e. scan)

Notable solutions are the impure ones:
- 5: impure map
- 7: impure reduce
- 11: impure any
- 12: impure accumulate (discarding input range i.e. iterative function application)
- 14: impure recursion

Notable pure solutions:
- 9: accumulate

original readme:

# AOC 2022 Python one-liners

Python one-liners for https://adventofcode.com/2022.

The hard rule is simple: the solution should only consist of a single expression and, possibly, some import statements.

There are also a couple of ways to work around the single expression limitation, such as assignment expressions, tuples-as-control-flow, and `eval`'ing arbitrary code. While those are not restricted, the aim should only be to use them for readability, and not to abuse them.

Obviously, the code should be written by a human, not generated in any way.
