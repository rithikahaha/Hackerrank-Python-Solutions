if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        op = command[0]
        args = command[1:]

        if op == "insert":
            lst.insert(int(args[0]), int(args[1]))
        elif op == "print":
            print(lst)
        elif op == "remove":
            lst.remove(int(args[0]))
        elif op == "append":
            lst.append(int(args[0]))
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()
