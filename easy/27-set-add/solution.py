if __name__ == '__main__':
    n = int(input())
    countries = set()
    for _ in range(n):
        countries.add(input())
    print(len(countries))
