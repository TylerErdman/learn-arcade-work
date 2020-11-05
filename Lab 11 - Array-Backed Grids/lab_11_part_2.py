import arcade

WIDTH = 40
HEIGHT = 40
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
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

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
        grid_x = int(x // (WIDTH + MARGIN))
        grid_y = int(y // (HEIGHT + MARGIN))

        # Alternating the number when pressed
        if self.grid[grid_y][grid_x] == 0:

            self.grid[grid_y][grid_x] = 1

        else:
            self.grid[grid_y][grid_x] = 0

        selected_cells = 0

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    selected_cells += 1

        print("There are", selected_cells, "selected cells.")

        row_counting = 0

        for row in range(ROW_COUNT):
            # Count how many blocks are selected in a row
            continuous_count = 0
            # To keep the function from repeating itself
            times_said = 0
            # counting which row we are on
            row_counting += 1

            selected_cells = 0

            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 1:

                    selected_cells += 1

                    continuous_count += 1

                if continuous_count > 2 and self.grid[row][column] == 0 and times_said == 0:

                    print("There are", continuous_count, "cells selected in row", row + 1)
                    times_said = 1
            print("Row", row_counting, "has", selected_cells, "selected.")

        for column in range(COLUMN_COUNT):

            selected_cells = 0

            for row in range(ROW_COUNT):

                if self.grid[row][column] == 1:

                    selected_cells += 1

            print("Column", column + 1, "has", selected_cells, "selected cells.")


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
