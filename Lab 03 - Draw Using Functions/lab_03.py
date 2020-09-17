import arcade

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 600


def draw_ocean():
    """A function that draws the ocean as the background"""
    arcade.draw_rectangle_filled(WINDOW_WIDTH/2, WINDOW_HEIGHT/3, 600, 300, arcade.color.OCEAN_BOAT_BLUE)


def draw_island(x, y):
    """Function to draw an island with a nice tree on it in a specific location"""
    arcade.draw_arc_filled(x, y, 100, 100, arcade.color.SAND, 0, 180)
    arcade.draw_arc_outline(x - 20, y + 40, 20, 70, arcade.color.BROWN, 0, 100, 20)
    arcade.draw_triangle_filled(x - 30, y + 55, x - 40, y + 65, x - 15, y + 85, arcade.color.GREEN)
    arcade.draw_triangle_filled(x - 35, y + 100, x - 40, y + 85, x - 15, y + 80, arcade.color.GREEN)
    arcade.draw_triangle_filled(x + 15, y + 100, x - 20, y + 80, x, y + 80, arcade.color.GREEN)


def draw_wave(x, y):
    """Function to draw a wave in a specific location"""
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 180, 270, 5)
    arcade.draw_arc_outline(x - 20, y, 20, 20, arcade.color.BLACK, 180, 360, 5)
    arcade.draw_arc_outline(x - 40, y, 20, 20, arcade.color.BLACK, 180, 360, 5)
    arcade.draw_arc_outline(x - 60, y, 20, 20, arcade.color.BLACK, 270, 360, 5)


def draw_fish(x, y):
    """Function to draw a moderately large white fish with a pink belly at a specific point"""
    arcade.draw_polygon_filled([[x, y], [x + 55, y + 30], [x + 80, y], [x + 55, y - 30]], arcade.color.WHITE_SMOKE)
    arcade.draw_ellipse_filled(x + 65, y + 10, 10, 5, arcade.color.BLACK)
    arcade.draw_triangle_filled(x, y, x + 80, y, x + 55, y - 30, arcade.color.PINK)
    arcade.draw_triangle_filled(x, y, x - 20, y + 30, x - 20, y - 30, arcade.color.WHITE_SMOKE)
    arcade.draw_ellipse_filled(x + 40, y, 30, 10, arcade.color.BLUEBERRY)


def draw_seaweed(x, y, length):
    """A function that draws some seaweed in a specific location with variable length"""
    arcade.draw_arc_outline(x, y, 10, length, arcade.color.GUPPIE_GREEN, 90, 270, 10)
    arcade.draw_arc_outline(x, y + length, 10, length, arcade.color.GUPPIE_GREEN, 270, 450, 10)
    arcade.draw_arc_outline(x, y + length * 2, 10, length, arcade.color.GUPPIE_GREEN, 90, 270, 10)
    arcade.draw_arc_outline(x, y + length * 3, 10, length, arcade.color.GUPPIE_GREEN, 270, 450, 10)


def main():
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, "My Tropical Island")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_ocean()
    draw_fish(200, 200)
    draw_fish(150, 0)
    draw_fish(500, 120)
    draw_seaweed(100, 100, 10)
    draw_seaweed(300, 150, 15)
    draw_seaweed(450, 200, 20)
    draw_wave(500, 200)
    draw_wave(100, 100)
    draw_wave(200, 250)
    draw_wave(70, 290)
    draw_island(200, 250)
    draw_island(400, 120)
    draw_island(100, 0)

    arcade.finish_render()
    arcade.run()


main()
