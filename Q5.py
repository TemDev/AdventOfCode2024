from collections import defaultdict


def main():
    f = open("Q5input.txt", "r")
    newline = False
    ordering = defaultdict(list)
    updates = []
    for line in f:
        if line == '\n':
            newline = True
        elif newline:
            updates.append(list(map(int, line.strip().split(","))))
        else:
            splitted = list(map(int, line.strip().split("|")))
            ordering[splitted[1]].append(splitted[0])
    total = 0
    total2 = 0
    for update in updates:
        length = len(update)
        breaking = False
        for (index, num) in enumerate(update):
            for num2 in range(index):
                if num in ordering[update[num2]]:
                    breaking = True
            if breaking:
                break
        if not breaking:
            total += update[length // 2]
        else:
            i = 0
            while i != length:
                num = update[i]
                for j in range(i):
                    num2 = update[j]
                    if num in ordering[num2]:
                        update[i], update[j] = update[j], update[i]
                        i = j
                        break
                i += 1
            total2 += update[length // 2]
    print(total)
    print(total2)



if __name__ == '__main__':
    main()