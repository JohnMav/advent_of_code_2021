from dataclasses import dataclass
import csv

@dataclass
class Submarine:
    X: int = 0
    Y: int = 0
    aim: int = 0

    def move_forward(self, distance: int):
        self.X += distance
        self.Y += self.aim * distance

    def adjust_aim(self, distance: int):
        self.aim += distance

    def relay_position(self) -> None:
        print(f"I am currently at position ({self.X}, {self.Y})")

    def receive_direction(self, direction: str, distance: int) -> None:
        if direction == 'forward':
            self.move_forward(distance)
        elif direction == 'up':
            self.adjust_aim(-distance)
        elif direction == 'down':
            self.adjust_aim(distance)
        else:
            print('Unclear Direction Received')

        self.relay_position()

    def receive_orders(self, file_path: str) -> None:
        with open(file_path) as f:
            reader = csv.reader(f, delimiter=' ')
            orders = list(reader)

        for order in orders:
            direction = str(order[0])
            distance = int(order[1])
            self.receive_direction(direction, distance)
        
        print('Final Position: ')
        self.relay_position()
    

if __name__ == '__main__':
    my_sub = Submarine()
    my_sub.receive_orders('data/puzzle_2.csv')

