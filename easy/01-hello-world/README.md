# 01. Say "Hello, World!" With Python

[HackerRank link](https://www.hackerrank.com/challenges/py-hello-world/problem)

## What it's asking
You're given one line of text as input. Print the fixed text `Hello, World!`,
then print back the line you were given.

## Steps
1. Read the one line of input the program is given.
2. Print the exact text `Hello, World!`.
3. Print the input you read in step 1.

## Code
```python
if __name__ == '__main__':
    input_string = input()
    print("Hello, World!")
    print(input_string)
```

## Walkthrough
- `input()` reads one line of text the program receives and hands it back to
  you as a string. We save it in `input_string` so we can use it later.
- `print("Hello, World!")` just displays that literal text.
- `print(input_string)` displays whatever was read in.

That `if __name__ == '__main__':` line at the top is boilerplate you'll see in
every HackerRank Python starter file — it just means "run this code when the
file is executed directly." You don't need to worry about it for now.
