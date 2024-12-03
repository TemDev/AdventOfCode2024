def func1(x, y):
    return 0 < x - y < 4


def func2(x, y):
    return 0 > x - y > -4


def main():
    f = open("Q2input.txt", "r")
    count = 0
    for line in f:
        report = list(map(int, line.strip().split(" ")))
        x = report[1] - report[0]
        if 0 < x < 4:
            f = func1
        elif 0 > x > -4:
            f = func2
        else:
            continue
        flag = False
        for i in range(2, len(report)):
            if not f(report[i], report[i - 1]):
                flag = True
                break
        if not flag:
            count += 1
    print(count)


def main2():
    f = open("Q2input.txt", "r")
    count = 0
    for line in f:
        report = list(map(int, line.strip().split(" ")))
        print(report)
        for j in range(len(report)):
            start = 2
            if j == 0:
                x = report[2] - report[1]
                start = 3
            elif j == 1:
                x = report[2] - report[0]
                start = 3
            else:
                x = report[1] - report[0]

            if 0 < x < 4:
                f = func1
            elif 0 > x > -4:
                f = func2
            else:
                continue
            flag = False
            for i in range(start, len(report)):
                end = i - 1
                if i == j:
                    continue
                elif end == j:
                    end = i - 2
                if not f(report[i], report[end]):
                    flag = True
                    break
            if not flag:
                count += 1
                print("PASS")
                break
    print(count)


if __name__ == "__main__":
    main2()