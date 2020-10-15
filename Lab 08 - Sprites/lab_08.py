
import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_GEM = 0.2
COIN_COUNT = 50
GEM_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class SilverCoin(arcade.Sprite):
    """Creating our coin"""
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.change_x = 0
        self.change_y = 0

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class RedGem(arcade.Sprite):
    """Creating the Evil Gem"""
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.change_x = 0
        self.change_y = 0

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Battle")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.gem_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMARANTH)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("player_stand.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = SilverCoin("coinSilver.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            coin.change_x = random.randrange(-5, 6)
            coin.change_y = random.randrange(-5, 6)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the Gems
        for i in range(GEM_COUNT):
            gem = RedGem("gemRed.png", SPRITE_SCALING_GEM)

            # Position the Gems
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)

            gem.change_x = random.randrange(-5, 6)
            gem.change_y = random.randrange(-5, 6)

            # Add the coin to the lists
            self.gem_list.append(gem)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.gem_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 24)

    def on_key_press(self, key, modifiers):
        """ Called when user presses key """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        if key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

    def update(self, delta_time):

        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.player_sprite.update()

        self.coin_list.update()

        self.gem_list.update()

        # Generate a list of all sprites that collided with the player.

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,

                                                              self.coin_list)

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite,

                                                            self.gem_list)

        # Loop through each colliding sprite, remove it, and add to the score.

        for coin in coins_hit_list:

            coin.remove_from_sprite_lists()

            self.score += 1

        for gem in gem_hit_list:

            gem.remove_from_sprite_lists()

            self.score -= 1

        if self.player_sprite.LEFT < 0:

            self.player_sprite.LEFT = 0

        if self.player_sprite.RIGHT > SCREEN_WIDTH:

            self.player_sprite.RIGHT = SCREEN_WIDTH

        if self.player_sprite.UP > SCREEN_HEIGHT:

            self.player_sprite.up = 0

        if self.player_sprite.DOWN < 0:

            self.player_sprite.down = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
