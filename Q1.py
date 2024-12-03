# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict

def main():
    f = open("Q1input.txt", "r")
    list1 = []
    list2 = []
    count = 0
    for line in f:
        count += 1
        x = line.strip().split(" ")
        list1.append(int(x[0]))
        list2.append(int(x[-1]))
    list1.sort()
    list2.sort()
    totalDif = 0
    for i in range(count):
        totalDif += abs(list1[i] - list2[i])
    print(totalDif)

def main2():
    f = open("Q1input.txt", "r")
    first = defaultdict(int)
    second = defaultdict(int)
    count = 0
    for line in f:
        count += 1
        x = line.strip().split(" ")
        first[int(x[0])] += 1
        second[int(x[-1])] += 1
    total = 0
    for (key, item) in first.items():
        total += key * second[key] * item
    print(total)

if __name__ == '__main__':
    main2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
