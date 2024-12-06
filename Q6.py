from collections import defaultdict


def main():
    f = open("Q6input.txt", "r")
    plan = []
    for line in f:
        plan.append(list(line))
    rows = len(plan)
    columns = len(plan[0])
    loc_y = -1
    loc_x = -1
    for i in range(rows):
        for j in range(columns):
            if plan[i][j] == "^":
                loc_y = i
                loc_x = j
    copy_loc_y = loc_y
    copy_loc_x = loc_x
    count = 0

    visited = set()
    direction = 0

    def det_direction(direction, loc_y, loc_x):
        match direction:
            case 0:
                if plan[loc_y - 1][loc_x] == '#':
                    direction += 1
                    direction %= 4
                else:
                    loc_y -= 1
            case 1:
                if plan[loc_y][loc_x + 1] == '#':
                    direction += 1
                    direction %= 4
                else:
                    loc_x += 1
            case 2:
                if plan[loc_y + 1][loc_x] == '#':
                    direction += 1
                    direction %= 4
                else:
                    loc_y += 1
            case 3:
                if plan[loc_y][loc_x - 1] == '#':
                    direction += 1
                    direction %= 4
                else:
                    loc_x -= 1
        return direction, loc_y, loc_x

    while loc_x != 0 and loc_y != 0 and loc_y != rows - 1 and loc_x != columns - 1:
        visited.add((loc_y, loc_x))
        (direction, loc_y, loc_x) = det_direction(direction, loc_y, loc_x)

    visited.add((loc_y, loc_x))

    print(len(visited))

    for (i, j) in visited:
        if i == copy_loc_y and j == copy_loc_x or plan[i][j] == '#':
            continue
        direction = 0
        loc_y = copy_loc_y
        loc_x = copy_loc_x
        visited = defaultdict(int)
        plan[i][j] = '#'
        while loc_x != 0 and loc_y != 0 and loc_y != rows - 1 and loc_x != columns - 1:
            visited[(loc_y, loc_x)] += 1
            if visited[(loc_y, loc_x)] > 4:
                count += 1
                break
            (direction, loc_y, loc_x) = det_direction(direction, loc_y, loc_x)
        plan[i][j] = '.'
    print(count)


if __name__ == '__main__':
    main()
