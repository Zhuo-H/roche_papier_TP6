import arcade
import time


SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Rock Paper Cissors +"


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background_color = arcade.color.BLACK
        self.interval = True
        self.computer_damage = 3
        self.timer = 0
        self.is_visible = True
        self.computer_list3 = arcade.SpriteList()
        self.computer_list2 = arcade.SpriteList()
        self.paper_open_list = arcade.SpriteList()
        self.rock_open_list = arcade.SpriteList()
        self.scissors_open_list = arcade.SpriteList()
        self.doom_guy3_list = arcade.SpriteList()
        self.doom_guy3 = arcade.Sprite("images/doom_guy_3.png", 0.15)
        self.doom_guy3.position = (280, 400)
        self.scissors_open = arcade.Sprite("assets/scissors.png", 0.6)
        self.scissors_open.position = (370, 270)
        self.rock_open = arcade.Sprite('assets/srock.png', 0.6)
        self.rock_open.position = (200, 270)
        self.computer_3 = arcade.Sprite("images/computer_3.png" , 0.1)
        self.computer_3.position = (800, 400)
        self.computer_2 = arcade.Sprite("images/computer_2.png", 0.1)
        self.computer_2.position = (280, 400)
        self.paper_open = arcade.Sprite('assets/spaper.png', 0.6)
        self.paper_open.position = (285, 270)
        self.computer_list3.append(self.computer_3)
        self.computer_list2.append(self.computer_2)
        self.paper_open_list.append(self.paper_open)
        self.rock_open_list.append(self.rock_open)
        self.scissors_open_list.append(self.scissors_open)
        self.doom_guy3_list.append(self.doom_guy3)
    def draw_square(self):
        arcade.draw_lrbt_rectangle_outline(180, 380, 350, 450,  arcade.color.RED, 3)
        arcade.draw_lrbt_rectangle_outline(700, 900, 350, 450, arcade.color.RED, 3)

        arcade.draw_lrbt_rectangle_outline(240, 320, 230, 310, arcade.color.RED, 2.5)
        arcade.draw_lrbt_rectangle_outline(150, 230, 230, 310, arcade.color.RED, 2.5)
        arcade.draw_lrbt_rectangle_outline(330, 415, 230, 310, arcade.color.RED, 2.5)
    def Text(self):
        arcade.draw_text("Roche, Papier, Ciseau", 250, 800, arcade.color.WHITE, 50)
        arcade.draw_text("Un nouveau jeu original!", 250, 760, arcade.color.WHITE, 20)

    def draw_hands(self):
        self.paper_open_list.draw()
        self.rock_open_list.draw()
        self.scissors_open_list.draw()
        self.doom_guy3_list.draw()
    def on_mouse_press(self, x, y, button, modifiers):
        clicked_sprites = arcade.get_sprites_at_point((x,y), self.computer_list3)
        if len(clicked_sprites) > 0:
            sprite = clicked_sprites[0]
            sprite.remove_from_sprite_lists()
            self.computer_3 = sprite
            arcade.schedule(self.action, 2)
    def action(self, delta_time):
        self.computer_list3.append(self.computer_3)
        arcade.unschedule(self.action)



    def on_update(self, delta_time):
        self.timer += delta_time
        if self.timer >= 1:
            self.interval = not self.interval
            self.computer_damage -= 1
            self.timer = 0

    def on_draw(self):

        self.clear()
        self.draw_square()
        self.computer_list3.draw()
        self.Text()
        self.draw_hands()

def main():

    game = MyGame()

    arcade.run()


if __name__ == "__main__":
    main()
