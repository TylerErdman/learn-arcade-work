import arcade

WIDTH = 50
HEIGHT = 50
COLUMN_COUNT = 10
ROW_COUNT = 10
MARGIN = 20

SCREEN_WIDTH = WIDTH * COLUMN_COUNT + MARGIN * (COLUMN_COUNT + 1)
SCREEN_HEIGHT = HEIGHT * ROW_COUNT + MARGIN * (ROW_COUNT + 1)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in  range(COLUMN_COUNT):
                self.grid[row].append(0)

        self.grid[2][5] = 1

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 0:
                    color = arcade.color.ICTERINE
                else:
                    color = arcade.color.BLUE

                arcade.draw_rectangle_filled((WIDTH / 2) + (column * (WIDTH + MARGIN)) + MARGIN,
                                             (HEIGHT / 2) + (row * (HEIGHT + MARGIN)) + MARGIN,
                                             WIDTH, HEIGHT, color
                                             )

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        grid_x = x // (WIDTH + MARGIN)
        grid_y = y // (HEIGHT + MARGIN)

        if self.grid[grid_y][grid_x] == 0:
            self.grid[grid_y][grid_x] = 1
        else:
            self.grid[grid_y][grid_x] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()