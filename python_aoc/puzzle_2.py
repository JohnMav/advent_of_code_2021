import csv

X = 0
Y = 1

def csv_to_list(path: str) -> list:
    with open(path) as f:
        reader = csv.reader(f, delimiter=' ')
        data = list(reader)
    return data


def move_horizontal(distance: int, point: list) -> list:
    point[X] = int(point[X]) + distance
    return point


def move_vertical(distance: int, point: list) -> list:
    point[Y] = int(point[Y]) + distance
    return point


def change_aim(current_aim: int, distance: int) -> int:
    return current_aim + distance


def print_sub_position(step: int, point: list) -> None:
    print(f"{step}: Sub is now at position {point}")


def prod(l: list):
    val = 1
    for i in l:
        val *= i
    return val


def puzzle_1(data: list) -> int:
    sub_point = [0,0]
    print_sub_position(0, sub_point)
    for i, step in enumerate(data):
        direction = step[0]
        distance = int(step[1])
        if direction == 'forward':
            sub_point = move_horizontal(distance, sub_point)
        elif direction == 'down':
            sub_point = move_vertical(distance, sub_point)
        else:
            sub_point = move_vertical(-distance, sub_point)
        
        print_sub_position(i+1, sub_point)

    return prod(sub_point)


def puzzle_2(data: list) -> int:
    sub_point = [0,0]
    current_aim = 0
    print_sub_position(0, sub_point)
    for i, step in enumerate(data):
        direction = step[0]
        distance = int(step[1])
        if direction == 'forward':
            sub_point = move_horizontal(distance, sub_point)
            sub_point = move_vertical((distance * current_aim), sub_point)
        elif direction == 'down':
            current_aim = change_aim(current_aim, distance)
        elif direction == 'up':
            current_aim = change_aim(current_aim, -distance)
        
        print_sub_position(i+1, sub_point)

    return prod(sub_point)


def print_solution(puzzle_name: str, value: int) -> None:
    print(f"The solution to {puzzle_name} is {value}")

if __name__ == '__main__':
    data = csv_to_list('data/puzzle_2.csv')
    print_solution('part a', puzzle_1(data))
    print_solution('part b', puzzle_2(data))
