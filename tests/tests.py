import numpy as np
import unittest

from instruction import Coordinates, Instruction
from io_controller import IOController
from lightshow_part1 import LightShowPart1
from lightshow_part2 import LightShowPart2


class TestStringMethods(unittest.TestCase):

    def test_parse_instruction__success(self):
        line = "turn off 1,2 through 3,4"
        instruction = IOController.parse_instruction(line)

        self.assertEqual(instruction.instruction_name, Instruction.TURN_OFF)
        self.assertEqual(instruction.coordinates_start.x, 1)
        self.assertEqual(instruction.coordinates_start.y, 2)
        self.assertEqual(instruction.coordinates_end.x, 3)
        self.assertEqual(instruction.coordinates_end.y, 4)

    def test_parse_instruction__instruction_not_found(self):
        line = "turn 1,2 through 3,4"
        self.assertRaises(Exception, IOController.parse_instruction, line)

    def test_turn_on_part1(self):
        light_show = LightShowPart1()
        light_show.turn_on(range(0, 10), range(0, 15))
        light_show.turn_on(range(0, 20), range(0, 20))
        self.assertEqual(light_show.lights_on_count, 20*20)
        for i in range(0, 20):
            for j in range(0, 20):
                self.assertEqual(light_show.display[i][j], 1)

    def test_turn_on_part2(self):
        light_show = LightShowPart2()
        light_show.turn_on(range(0, 10), range(0, 15))
        light_show.turn_on(range(0, 20), range(0, 20))
        self.assertEqual(light_show.lights_on_count, 10*15 + 20*20)
        for i in range(0, 10):
            for j in range(0, 15):
                self.assertEqual(light_show.display[i][j], 2)

    def test_turn_off_part1(self):
        light_show = LightShowPart1()
        light_show.display = np.ones((light_show.N, light_show.N), dtype=int)
        light_show.lights_on_count = light_show.N * light_show.N
        light_show.turn_off(range(0, 10), range(0, 15))
        self.assertEqual(light_show.lights_on_count, 1000*1000 - 10*15)
        for i in range(0, 10):
            for j in range(0, 15):
                self.assertEqual(light_show.display[i][j], 0)

    def test_turn_off_part1__doesnt_go_below_0(self):
        light_show = LightShowPart1()
        self.assertEqual(light_show.lights_on_count, 0)
        light_show.turn_off(range(0, 2), range(0, 2))
        self.assertEqual(light_show.lights_on_count, 0)
        for i in range(0, 2):
            for j in range(0, 2):
                self.assertEqual(light_show.display[i][j], 0)

    def test_turn_off_part2(self):
        light_show = LightShowPart2()
        for i in range(0, 10):
            for j in range(0, 15):
                light_show.display[i][j] = 2
        light_show.lights_on_count = 10 * 15 * 2
        light_show.turn_off(range(0, 10), range(0, 15))
        self.assertEqual(light_show.lights_on_count, 10*15)
        for i in range(0, 10):
            for j in range(0, 15):
                self.assertEqual(light_show.display[i][j], 1)

    def test_turn_off_part2__doesnt_go_below_0(self):
        light_show = LightShowPart2()
        self.assertEqual(light_show.lights_on_count, 0)
        light_show.turn_off(range(0, 2), range(0, 2))
        self.assertEqual(light_show.lights_on_count, 0)
        for i in range(0, 2):
            for j in range(0, 2):
                self.assertEqual(light_show.display[i][j], 0)

    def test_toggle_part1(self):
        light_show = LightShowPart1()
        self.assertEqual(light_show.lights_on_count, 0)

        light_show.toggle(range(0, 10), range(0, 10))
        self.assertEqual(light_show.lights_on_count, 10*10)
        for i in range(0, 10):
            for j in range(0, 10):
                self.assertEqual(light_show.display[i][j], 1)

        light_show.toggle(range(0, 10), range(0, 10))
        self.assertEqual(light_show.lights_on_count, 0)
        for i in range(0, 10):
            for j in range(0, 10):
                self.assertEqual(light_show.display[i][j], 0)

    def test_toggle_part2(self):
        light_show = LightShowPart2()
        self.assertEqual(light_show.lights_on_count, 0)

        light_show.toggle(range(0, 10), range(0, 10))
        self.assertEqual(light_show.lights_on_count, 10 * 10 * 2)
        for i in range(0, 10):
            for j in range(0, 10):
                self.assertEqual(light_show.display[i][j], 2)

    def test_calculate_part1(self):
        instructions = [
            Instruction("turn on", Coordinates("0,0"), Coordinates("9,9")),
            Instruction("turn on", Coordinates("0,0"), Coordinates("19,19")),
            Instruction("turn off", Coordinates("0,0"), Coordinates("1,1")),
            Instruction("toggle", Coordinates("2,2"), Coordinates("3,3")),
        ]
        light_show = LightShowPart1()
        result = light_show.calculate_lights_on(instructions)
        self.assertEqual(result, 20*20 - 8)

    def test_calculate_part2(self):
        instructions = [
            Instruction("turn on", Coordinates("0,0"), Coordinates("9,9")),
            Instruction("turn on", Coordinates("0,0"), Coordinates("9,9")),
            Instruction("turn off", Coordinates("0,0"), Coordinates("1,1")),
            Instruction("toggle", Coordinates("2,2"), Coordinates("3,3")),
        ]
        light_show = LightShowPart2()
        result = light_show.calculate_lights_on(instructions)
        self.assertEqual(result, 10*10*2 - 4 + 8)
