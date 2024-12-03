import re


def main():
    f = open("Q3input.txt", "r")
    pattern = "(mul\\(\\d+,\\d+\\))|(do\\(\\))|(don\\'t\\(\\))"
    total = 0
    off = False
    for line in f:
        matches = re.findall(pattern, line)
        for match in matches:
            if len(match[0]) > 0 and not off:
                match = match[0]
                num1, num2 = match.split("(")[1].split(",")
                num1 = int(num1)
                num2 = int(num2[:-1])
                if num1 < 1000 and num2 < 1000:
                    total += num1 * num2
            elif len(match[1]) > 0:
                off = False
            elif len(match[2]) > 0:
                off = True
            else:
                pass
    print(total)




if __name__ == "__main__":
    main()