"""
Artwork from http://kenney.nl
"""

import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40

MOVEMENT_SPEED = 5
NUMBER_OF_COINS = 20


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        self.coin_list = None
        self.wall_list = None
        self.score = 0
        self.game_over = False

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Loading up sound
        self.coin_sound = arcade.load_sound("coin2.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.4)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        for x in range(0, 1000, 64):
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = SCREEN_HEIGHT
            self.wall_list.append(wall)

        for x in range(0, 1000, 64):
            wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for y in range(0, 1000, 64):
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 1000, 64):
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
            wall.center_x = 1000
            wall.center_y = y
            self.wall_list.append(wall)

        wall = arcade.Sprite("bush.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("bush.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("bush.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = 100
        self.wall_list.append(wall)

        coordinate_list = [[400, 40], [600, 340], [300, 340]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for item in range(50, 200, 2):
            random_number = random.randrange(6)
            if random_number > 4:
                wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
                wall.center_x = item * 4
                wall.center_y = SCREEN_HEIGHT / 2
                self.wall_list.append(wall)

        for item in range(50, 200, 2):
            random_number = random.randrange(6)
            if random_number > 4:
                wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
                wall.center_x = item * 4
                wall.center_y = SCREEN_HEIGHT / 3.5
                self.wall_list.append(wall)

        for item in range(50, 200, 2):
            random_number = random.randrange(6)
            if random_number > 4:
                wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING)
                wall.center_x = item * 4
                wall.center_y = SCREEN_HEIGHT / 1.2
                self.wall_list.append(wall)

        for i in range(NUMBER_OF_COINS):

            coin_placed_successfully = False

            coin = arcade.Sprite("coinGold.png",SPRITE_SCALING)

            while not coin_placed_successfully:
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, self.view_left + 20, self.view_bottom + 20, arcade.color.BLACK, 24)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()

            arcade.play_sound(self.coin_sound)

            self.score += 1

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()