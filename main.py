from drawer import *
from engine import *


class Application:

    def __init__(self):

        pygame.init()
        pygame.key.set_repeat(100, 10)

        self._screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

        self._running = True
        self.game_clock = pygame.time.Clock()

        self._show_specs = False
        self._specs_font = pygame.font.SysFont(SPECS_FONT, SPECS_SIZE)
        self._specs = ["Fps"]

        # Objects
        self._drawer = Drawer(self._screen)
        self._engine = Engine()

        self.objects_data = None

    def run(self):

        while self._running:
            self.update()
            self.draw()
            self.game_clock.tick(FPS_LIMIT)

        # Quit application
        pygame.quit()
        print("\n# Program exited properly #")

    def update(self):

        # Get states
        self._running = self._engine.get_running_state()
        self._show_specs = self._engine.get_specs_state()

        # Process inputs
        self._engine.get_inputs()
        self._engine.move_lines(self.objects_data)

        # Get stuff
        self.objects_data = self._engine.get_objects_data()

        # Specs
        self.update_specs()

    def draw(self):

        # Clean
        self._drawer.clean_screen()

        # Draw specs
        if self._show_specs:
            self._drawer.draw_specs(self._specs, self._specs_font)

        # Draw grid
        self._drawer.draw_grid()

        # Draw stuff

        self._drawer.draw_data(self.objects_data)

        # Update
        self._drawer.update_screen()

    def update_specs(self):

        self._specs[0] = "FPS : {0:.1f}".format(self.game_clock.get_fps())


app = Application()
app.run()