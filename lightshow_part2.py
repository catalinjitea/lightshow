from lightshow_part1 import LightShowPart1


class LightShowPart2(LightShowPart1):

    def turn_on(self, range_x: range, range_y: range) -> None:
        for i in range_x:
            for j in range_y:
                self.display[i][j] += 1
                self.lights_on_count += 1

    def turn_off(self, range_x: range, range_y: range) -> None:
        for i in range_x:
            for j in range_y:
                if self.display[i][j] > 0:
                    self.display[i][j] -= 1
                    if self.lights_on_count > 0:
                        self.lights_on_count -= 1

    def toggle(self, range_x: range, range_y: range) -> None:
        for i in range_x:
            for j in range_y:
                self.display[i][j] += 2
                self.lights_on_count += 2
