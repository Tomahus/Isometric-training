from constants import *


class Cube:

    def __init__(self, _id, _pos):

        self._surface = pygame.image.load("res/" + _id + ".png").convert_alpha()
        self.cube_pos = _pos
        self._id = _id
        self._origin = _pos

    def move_along_x(self, _x):
        self.cube_pos = (self.cube_pos[0]+_x, self.cube_pos[1])

    def move_along_y(self, _y):
        self.cube_pos = (self.cube_pos[0], self.cube_pos[1] + _y)

    def get_pos(self):
        return self.cube_pos

    def get_surface(self):
        return pygame.transform.scale2x(self._surface)

    def get_id(self):
        return self._id

    def get_origin(self):
        return self._origin



