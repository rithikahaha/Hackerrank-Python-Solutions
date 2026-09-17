# 61. Map and Lambda Function

[HackerRank link](https://www.hackerrank.com/challenges/map-and-lambda-expression/problem)

## What it's asking
Given `n`, generate the first `n` Fibonacci numbers (`0, 1, 1, 2, 3, 5, ...`
— each one is the sum of the two before it), then print the **cube** of each
one.

## Steps
1. Write a tiny function that cubes a number.
2. Build the list of the first `n` Fibonacci numbers.
3. Apply the cube function to every number in that list.
4. Print the result.

## Code
```python
cube = lambda x: x ** 3


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
```

## Walkthrough
- `lambda x: x ** 3` defines a small, unnamed function inline — it's the
  same thing as writing:
  ```python
  def cube(x):
      return x ** 3
  ```
  just shorter, and handy for quick, throwaway functions like this one that
  you don't need to reuse elsewhere.
- `fibonacci(n)` builds the sequence by starting with `[0, 1]` and
  repeatedly appending the sum of the previous two numbers, `fib[-1] +
  fib[-2]`. `fib[:n]` then trims it down to exactly `n` numbers — this also
  correctly handles small `n` (like `0` or `1`), since a slice never raises
  an error even if you ask for more than the list has.
- `map(cube, fibonacci(n))` applies `cube` to every single number in the
  Fibonacci list, one at a time, without you writing a loop yourself.
  `list(...)` collects the results into an actual list so it can be
  printed.
