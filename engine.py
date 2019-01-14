from constants import *
from cube import Cube


class Engine:

    def __init__(self):

        self._running = True
        self._show_specs = True

        self._data = []
        self.generation()

        # Animation
        self._move_pair = 0
        self._move_impair = 0
        self._animate = False

    def get_inputs(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_F1:
                    if self._show_specs:
                        self._show_specs = False
                    else:
                        self._show_specs = True
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_SPACE:
                    if self._animate:
                        self._animate = False
                    else:
                        self._animate = True

    def get_running_state(self):
        return self._running

    def get_specs_state(self):
        return self._show_specs

    def get_objects_data(self):
        return self._data

    def generation(self):

        number_of_cubes = 10
        cube_list = []
        cube_size = 20
        color = 0

        for j in range(number_of_cubes):
            for i in range(number_of_cubes):

                pos = (390+(i*cube_size), j*cube_size)

                if color == 0:
                    cube_list.append(Cube("red_cube", pos))
                    color = 1
                else:
                    cube_list.append(Cube("green_cube", pos))
                    color = 0

        self._data = cube_list

    def move_lines(self, _data):

        if _data is not None and self._animate:

            counter = 0

            for i in range(len(_data)):
                if counter % 2 == 0:
                    if _data[i].get_pos()[1] >= _data[i].get_origin()[1]:
                        self._move_pair = -0.5
                    if _data[i].get_pos()[1] <= _data[i].get_origin()[1]-50:
                        self._move_pair = 0.5

                    _data[i].move_along_x(self._move_pair)
                    _data[i].move_along_y(self._move_pair)
                else:
                    if _data[i].get_pos()[1] <= _data[i].get_origin()[1]:
                        self._move_impair = 0.5
                    if _data[i].get_pos()[1] >= _data[i].get_origin()[1]+50:
                        self._move_impair = -0.5

                    _data[i].move_along_x(self._move_impair)
                    _data[i].move_along_y(self._move_impair)

                counter += 1























