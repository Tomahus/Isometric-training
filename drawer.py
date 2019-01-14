from constants import *
from features import *


class Drawer:

    def __init__(self, _screen):
        self._screen = _screen

    def clean_screen(self):
        self._screen.fill(COLORS["black"])

    def update_screen(self):
        pygame.display.update()

    def draw_on_screen(self, _surface, _pos):

        self._screen.blit(_surface, _pos)

    def draw_specs(self, _specs_list, _font):

        x = 10
        y = 10

        for each in _specs_list:

            line = _font.render(each, 1, COLORS["white"])
            self.draw_on_screen(line, (x, y))
            y += 15

    def draw_grid(self):

        cube_size = 20
        number_in_range = 10

        for row in range(number_in_range+1):

            s = convert_to_iso((400, row * cube_size))
            e = convert_to_iso((400+(number_in_range*cube_size), row * cube_size))
            pygame.draw.line(self._screen, COLORS["white"], s, e)

            for cols in range(number_in_range+1):
                s = convert_to_iso((400+(cols * cube_size), 0))
                e = convert_to_iso((400+(cols * cube_size), (number_in_range*cube_size)))
                pygame.draw.line(self._screen, COLORS["white"], s, e)

    def draw_data(self, _data):

        data_sorted = sorted(_data, key=self.get_item_pos)

        for each in data_sorted:
            self._screen.blit(each.get_surface(), convert_to_iso(each.get_pos()))

    def get_item_pos(self, _item):
        return _item.get_pos()







