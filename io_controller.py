from typing import List

from instruction import Coordinates, Instruction


class IOController:

    @classmethod
    def read_instructions(cls, filename: str) -> List[Instruction]:
        instructions = []
        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip()
                instruction = cls.parse_instruction(line)
                instructions.append(instruction)

        return instructions

    @classmethod
    def parse_instruction(cls, line: str) -> Instruction:
        through_split = line.split(Instruction.THROUGH)
        if Instruction.TURN_ON in through_split[0]:
            instruction_name = Instruction.TURN_ON
        elif Instruction.TURN_OFF in through_split[0]:
            instruction_name = Instruction.TURN_OFF
        elif Instruction.TOGGLE in through_split[0]:
            instruction_name = Instruction.TOGGLE
        else:
            raise Exception("Instruction not found!")

        coordinates_start = Coordinates(
            coordinates=through_split[0].split(instruction_name)[1].strip()
        )
        coordinates_end = Coordinates(coordinates=through_split[1].strip())
        return Instruction(
            instruction_name=instruction_name,
            coordinates_start=coordinates_start,
            coordinates_end=coordinates_end,
        )

    @classmethod
    def write_result(cls, filename: str, result: int):
        with open(filename, "a") as file:
            file.write(str(result))
