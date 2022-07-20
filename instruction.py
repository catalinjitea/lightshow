
class Coordinates:
    def __init__(self, coordinates: str):
        coordinates_pair = coordinates.split(',')
        self.x = int(coordinates_pair[0])
        self.y = int(coordinates_pair[1])

    def __str__(self):
        return f"{self.x},{self.y}"


class Instruction:
    THROUGH = "through"
    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"
    INSTRUCTION_NAMES = [TURN_ON, TURN_OFF, TOGGLE]

    def __init__(
        self,
        instruction_name: str,
        coordinates_start: Coordinates,
        coordinates_end: Coordinates,
    ):
        self.instruction_name = instruction_name
        self.coordinates_start = coordinates_start
        self.coordinates_end = coordinates_end

    def __str__(self):
        return (
            f"{self.instruction_name} "
            f"{self.coordinates_start} "
            f"{self.THROUGH} "
            f"{self.coordinates_end}"
        )
