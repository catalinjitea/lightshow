import numpy as np
from typing import List

from instruction import Instruction


class LightShowPart1:
    N = 1000

    def __init__(self):
        self.display = np.zeros((self.N, self.N), dtype=int)
        self.lights_on_count = 0

    def calculate_lights_on(self, instructions: List[Instruction]) -> int:
        for instruction in instructions:
            range_x = range(
                instruction.coordinates_start.x, instruction.coordinates_end.x + 1
            )
            range_y = range(
                instruction.coordinates_start.y, instruction.coordinates_end.y + 1
            )

            if instruction.instruction_name == Instruction.TURN_ON:
                self.turn_on(range_x=range_x, range_y=range_y)
            elif instruction.instruction_name == Instruction.TURN_OFF:
                self.turn_off(range_x=range_x, range_y=range_y)
            if instruction.instruction_name == Instruction.TOGGLE:
                self.toggle(range_x=range_x, range_y=range_y)

        return self.lights_on_count

    def turn_on(self, range_x: range, range_y: range) -> None:
        for i in range_x:
            for j in range_y:
                if self.display[i][j] == 0:
                    self.display[i][j] = 1
                    self.lights_on_count += 1

    def turn_off(self, range_x: range, range_y: range) -> None:
        for i in range_x:
            for j in range_y:
                if self.display[i][j] == 1:
                    self.display[i][j] = 0
                    if self.lights_on_count > 0:
                        self.lights_on_count -= 1

    def toggle(self, range_x: range, range_y: range) -> None:
        for i in range_x:
            for j in range_y:
                if self.display[i][j] == 1:
                    self.display[i][j] = 0
                    if self.lights_on_count > 0:
                        self.lights_on_count -= 1
                elif self.display[i][j] == 0:
                    self.display[i][j] = 1
                    self.lights_on_count += 1
