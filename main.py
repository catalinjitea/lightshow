from lightshow_part1 import LightShowPart1
from lightshow_part2 import LightShowPart2

from io_controller import IOController


if __name__ == '__main__':
    light_show_part1 = LightShowPart1()
    instructions = IOController.read_instructions(filename="tests/file1.txt")
    result_part1 = light_show_part1.calculate_lights_on(instructions)
    IOController.write_result(filename="tests/file1.txt", result=result_part1)

    light_show_part2 = LightShowPart2()
    instructions = IOController.read_instructions(filename="tests/file2.txt")
    result_part2 = light_show_part2.calculate_lights_on(instructions)
    IOController.write_result(filename="tests/file2.txt", result=result_part2)
