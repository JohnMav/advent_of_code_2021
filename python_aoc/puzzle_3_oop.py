from dataclasses import dataclass
import csv

@dataclass
class Submarine:
    X: int = 0
    Y: int = 0
    aim: int = 0
    gamma_rate: str = ''
    epsilon_rate: str = ''
    power: int = 0
    life_support_rating: int = 0
    o2_generator_rating: int = 0
    co2_scrubber_rating: int = 0


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


    def __convert_binary_to_int(self, binary: str) -> int:
        return int(binary, 2)


    def __flip_bits(self, bits: str) -> str:
        return ''.join(['1' if b == '0' else '0' for b in bits])


    def compute_gamma_rate(self, readings: list) -> str:
        num_bits = len(str(readings[0]))
        num_readings = len(readings)
        gamma_reading = ''
        for bit_position in range(0, num_bits):
            bit_total = sum([int(r[bit_position]) for r in readings])
            if bit_total > (float(num_readings) / 2.0):
                gamma_reading += '1'
            else:
                gamma_reading += '0'
        
        return gamma_reading


    def compute_epsilon_rate(self, readings: list) -> str:
        gamma_reading = self.compute_gamma_rate(readings)
        epsilon_reading = self.__flip_bits(gamma_reading)
        return epsilon_reading


    def compute_power(self, readings: list) -> int:
        self.gamma_rate = self.compute_gamma_rate(readings)
        self.epsilon_rate = self.compute_epsilon_rate(readings)
        return self.__convert_binary_to_int(self.gamma_rate) * self.__convert_binary_to_int(self.epsilon_rate)


    def compute_o2_rating(self, readings: list) -> str:
        num_bits = len(str(readings[0]))
        for bit_position in range(0, num_bits):
            num_readings = len(readings)
            bit_total = sum([int(r[bit_position]) for r in readings])
            if bit_total >= (float(num_readings) / 2.0):
                readings = list(filter(lambda x: x[bit_position] == '1', readings))
            else:
                readings = list(filter(lambda x: x[bit_position] == '0', readings))
        
            if len(readings) == 1:
                return readings[0]


    def compute_co2_rating(self, readings: list) -> str:
        num_bits = len(str(readings[0]))
        for bit_position in range(0, num_bits):
            num_readings = len(readings)
            bit_total = sum([int(r[bit_position]) for r in readings])
            if bit_total >= (float(num_readings) / 2.0):
                readings = list(filter(lambda x: x[bit_position] == '0', readings))
            else:
                readings = list(filter(lambda x: x[bit_position] == '1', readings))
        
            if len(readings) == 1:
                return readings[0]


    def compute_life_support_rating(self, readings: list) -> int:
        self.o2_generator_rating = self.compute_o2_rating(readings)
        self.co2_scrubber_rating = self.compute_co2_rating(readings)
        return self.__convert_binary_to_int(self.o2_generator_rating) * self.__convert_binary_to_int(self.co2_scrubber_rating)


    def read_diagnostic_report(self, file_path: str) -> tuple:
        with open(file_path) as f:
            reader = csv.reader(f, delimiter=' ')
            readings = [reading[0] for reading in list(reader)]
            
        self.power = self.compute_power(readings)
        self.life_support_rating = self.compute_life_support_rating(readings)
        print(f"Current Power is: {self.power}")
        print(f"Curent life support rating: {self.life_support_rating}")


    def receive_orders(self, file_path: str) -> tuple:
        with open(file_path) as f:
            reader = csv.reader(f, delimiter=' ')
            orders = list(reader)

        for order in orders:
            direction = str(order[0])
            distance = int(order[1])
            self.receive_direction(direction, distance)
        
        return (self.X, self.Y)
    

if __name__ == '__main__':
    my_sub = Submarine()
    my_sub.read_diagnostic_report('data/puzzle_3.csv')
