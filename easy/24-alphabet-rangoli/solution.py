def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3

    rows = []
    for i in range(size):
        letters = [alpha[size - 1 - k] for k in range(i + 1)]
        row = letters + letters[-2::-1]
        rows.append("-".join(row).center(width, "-"))

    print("\n".join(rows + rows[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
