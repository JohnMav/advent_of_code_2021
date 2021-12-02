import csv

def csv_to_list(path: str) -> list:
    with open(path) as f:
        reader = csv.reader(f)
        data = list(reader)
    
    return data

def gt(a: int, b: int ) -> bool:
    return a > b

def puzzle_1(data: list) -> int:
    return len(list(filter(lambda i: gt(data[i], data[i-1]), range(len(data)))))

def puzzle_2(data: list) -> int:
    groups = list(map(lambda i: int(data[i+1][0]) + int(data[i+2][0]) + int(data[i+3][0]), range(len(data)-3)))
    return puzzle_1(groups)

def print_solution(puzzle_name: str, value: int) -> None:
    print(f"The solution to {puzzle_name} is {value}")

if __name__ == '__main__':
    data = csv_to_list('data/puzzle_1.csv')
    print_solution('part a', puzzle_1(data))
    print_solution('part b', puzzle_2(data))
