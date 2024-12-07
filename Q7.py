def main():
    f = open("Q7input.txt", "r")
    total = 0
    for line in f:
        tv, operands = line.split(": ")
        tv = int(tv)
        operands = list(map(int, operands.split(" ")))
        l = [operands[0]]

        for i in range(1, len(operands)):
            new_l = []
            for j in [lambda x, y: x * y, lambda x, y: x + y, lambda x, y: int(str(x) + str(y))]:
                for k in l:
                    v = j(k, operands[i])
                    if v <= tv:
                        new_l.append(v)
            l = new_l
        for i in l:
            if i == tv:
                total += tv
                break
    print(total)


if __name__ == "__main__":
    main()
