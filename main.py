import random

import arcade

from attack_animation import AttackType, AttackAnimations


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
        self.computer_choice_list = arcade.SpriteList()
        self.computer_list3 = arcade.SpriteList()
        self.computer_list2 = arcade.SpriteList()
        self.paper_open_list = arcade.SpriteList()
        self.rock_open_list = arcade.SpriteList()
        self.scissors_open_list = arcade.SpriteList()
        self.doom_guy3_list = arcade.SpriteList()
        self.doom_guy3 = arcade.Sprite("images/doom_guy_3.png", 0.15)
        self.doom_guy3.position = (280, 400)
        self.scissors_open = AttackAnimations(AttackType.SCISSORS)
        self.scissors_open.position = (370, 270)
        self.rock_open = AttackAnimations(AttackType.ROCK)
        self.rock_open.position = (190, 270)
        self.computer_3 = arcade.Sprite("images/computer_3.png" , 0.1)
        self.computer_3.position = (800, 400)
        self.computer_2 = arcade.Sprite("images/computer_2.png", 0.1)
        self.computer_2.position = (280, 400)
        self.paper_open = AttackAnimations(AttackType.PAPER)
        self.paper_open.position = (285, 270)
        self.computer_list3.append(self.computer_3)
        self.computer_list2.append(self.computer_2)
        self.paper_open_list.append(self.paper_open)
        self.rock_open_list.append(self.rock_open)
        self.scissors_open_list.append(self.scissors_open)
        self.doom_guy3_list.append(self.doom_guy3)

        self.computer_rock = AttackAnimations(AttackType.ROCK)
        self.computer_paper = AttackAnimations(AttackType.PAPER)
        self.computer_scissors = AttackAnimations(AttackType.SCISSORS)

        self.computer_rock.position = (802,270)
        self.computer_scissors.position = (802, 270)
        self.computer_paper.position = (802, 270)

        self.computer_choice_list.append(self.computer_rock)
        self.computer_choice_list.append(self.computer_paper)
        self.computer_choice_list.append(self.computer_scissors)

        self.computer_rock.visible = False
        self.computer_paper.visible = False
        self.computer_scissors.visible = False

        self.player_choice = ''
        self.computer_choice = ''
        self.result = ''
        self.score = 0
        self.score_computer = 0
        self.hide_timer = 0
        self.can_click = True
        self.show_computer_choice =True
        self.hidden_sprites = []

    def draw_square(self):
        arcade.draw_lrbt_rectangle_outline(180, 380, 350, 450,  arcade.color.RED, 3)
        arcade.draw_lrbt_rectangle_outline(700, 900, 350, 450, arcade.color.RED, 3)

        arcade.draw_lrbt_rectangle_outline(240, 320, 230, 310, arcade.color.RED, 2.5)
        arcade.draw_lrbt_rectangle_outline(150, 230, 230, 310, arcade.color.RED, 2.5)
        arcade.draw_lrbt_rectangle_outline(330, 415, 230, 310, arcade.color.RED, 2.5)
        arcade.draw_lrbt_rectangle_outline(760, 845, 230, 310, arcade.color.RED, 2.5)

    def Text(self):
        arcade.draw_text("Roche, Papier, Ciseau", 250, 800, arcade.color.WHITE, 50)
        arcade.draw_text("Un nouveau jeu original!", 250, 760, arcade.color.WHITE, 20)

    def draw_hands(self):
        self.paper_open_list.draw()
        self.rock_open_list.draw()
        self.scissors_open_list.draw()
        self.doom_guy3_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):

        if not self.can_click:

            return



        if self.rock_open.collides_with_point((x,y)):
            self.player_choice = 1
            self.hidden_sprites = [self.paper_open, self.scissors_open]
        elif self.paper_open.collides_with_point((x,y)):
            self.player_choice = 2
            self.hidden_sprites = [self.rock_open, self.scissors_open]
        elif self.scissors_open.collides_with_point((x,y)):
            self.player_choice = 3
            self.hidden_sprites = [self.paper_open, self.rock_open]
        else:
            return

        self.computer_choice = random.randint(1, 3)

        self.computer_rock.visible = False
        self.computer_paper.visible = False
        self.computer_scissors.visible = False

        if self.computer_choice == 1:
            self.computer_rock.visible = True
        elif self.computer_choice == 2:
            self.computer_paper.visible = True
        else:
            self.computer_scissors.visible = True

        for sprites in self.hidden_sprites:
            sprites.visible = False




        self.show_computer_choice = True
        self.hide_timer = 2
        self.can_click = False
        self.action()




    def action(self):
        p = self.player_choice
        c = self.computer_choice

        if (p == 1 and c == 2) or (p == 2 and c == 3) or (p == 3 and c == 1):
            self.result = 'lose'
            self.score_computer += 1
        elif (p == 2 and c == 1) or (p == 3 and c == 2) or (p == 1 and c == 3):
            self.result = 'win'
            self.score += 1
        else:
            self.result = 'tie'


    def on_update(self, delta_time):
        self.scissors_open.on_update()
        self.rock_open.on_update()
        self.paper_open.on_update()
        self.computer_rock.on_update()
        self.computer_scissors.on_update()
        self.computer_paper.on_update()
        self.timer += delta_time
        if self.hide_timer > 0:
            self.hide_timer -= delta_time

            if self.hide_timer <= 0:
                self.show_computer_choice = False
                self.computer_rock.visible = False
                self.computer_paper.visible = False
                self.computer_scissors.visible = False

                for sprites in self.hidden_sprites:
                    sprites.visible = True
                self.hidden_sprites = []
                self.can_click = True
                self.result = ''
        if self.timer >= 1:
            self.interval = not self.interval
            self.computer_damage -= 1
            self.timer = 0


    def on_draw(self):
        self.clear()
        self.draw_square()
        self.rock_open_list.draw()
        self.computer_list3.draw()
        self.Text()
        self.draw_hands()
        arcade.draw_text(f"the result is a: {self.result}", 250, 500, arcade.color.WHITE, 50)
        arcade.draw_text(f"the computer score is: {self.score_computer}", 700, 200, arcade.color.WHITE, 20)
        arcade.draw_text(f"your score is: {self.score}", 150, 200, arcade.color.WHITE, 20)
        self.computer_choice_list.draw()


def main():

    game = MyGame()

    arcade.run()


if __name__ == "__main__":
    main()
