def main():
    f = open("Q4input.txt", "r")
    map = []
    for line in f:
        map.append(line.strip())
    rows = len(map)
    columns = len(map[0])
    count = 0
    print(rows, columns, sep=" ")
    for i in range(rows):
        line = map[i]
        for j in range(0, columns):
            sli = line[j:min(j + 4, columns)]
            if sli == "XMAS":
                count += 1
            elif sli == "SAMX":
                count += 1
            if i < rows - 3:
                sli = map[i][j] + map[i + 1][j] + map[i + 2][j] + map[i + 3][j]
                if sli == "XMAS":
                    count += 1
                if sli == "SAMX":
                    count += 1
                if j < columns - 3:
                    sli = map[i][j] + map[i + 1][j + 1] + map[i + 2][j + 2] + map[i + 3][j + 3]
                    if sli == "XMAS":
                        count += 1
                    if sli == "SAMX":
                        count += 1
                    sli = map[i + 3][j] + map[i + 2][j + 1] + map[i + 1][j + 2] + map[i][j + 3]
                    if sli == "XMAS":
                        count += 1
                    if sli == "SAMX":
                        count += 1
    print(count)

def main2():
    f = open("Q4input.txt", "r")
    map = []
    for line in f:
        map.append(line.strip())
    rows = len(map)
    columns = len(map[0])
    count = 0
    print(rows, columns, sep=" ")
    for i in range(rows - 2):
        for j in range(columns - 2):
            sli = map[i][j] + map[i + 1][j + 1] + map[i + 2][j + 2]
            sli2 = map[i + 2][j] + map[i + 1][j + 1] + map[i][j + 2]
            if sli == "MAS" or sli == "SAM":
                if sli2 == "MAS" or sli2 == "SAM":
                    count += 1
    print(count)


if __name__ == "__main__":
    main2()