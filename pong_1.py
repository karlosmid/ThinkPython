# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 5, 2011 3:58:52 PM$"

from gasp import *

COMPUTER_WINS = 1
PLAYER_WINS = 0
QUIT = -1


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def play_round():
    left_x = 10
    left_y = 140
    left = Box((left_x, left_y), 10,100, filled=True)
    dy = 5

    right_x = 780
    right_y = 140
    right = Box((right_x, right_y), 10,100,filled=True)

    while True:       

        if key_pressed('q') and left_y <= 580:
            left_y += 5
        elif key_pressed('a') and left_y >= 20:
            left_y -= 5
        elif key_pressed('o') and right_y <= 580:
            right_y += 5
        elif key_pressed('l') and right_y >= 20:
            right_y -= 5

        if key_pressed('1'):
            return QUIT

        move_to(left, (left_x, left_y))
        move_to(right, (right_x, right_y))

        if distance(left_x, left_y, right_x, right_y) <= 30:
            remove_from_screen(left)
            remove_from_screen(right)
            return PLAYER_WINS

        update_when('next_tick')


def play_game():
    player_score = 0
    comp_score = 0

    while True:
        pmsg = Text("Player: %d Points" % player_score, (10, 570), size=24)
        cmsg = Text("Computer: %d Points" % comp_score, (640, 570), size=24)
        sleep(3)
        remove_from_screen(pmsg)
        remove_from_screen(cmsg)

        result = play_round()

        if result == PLAYER_WINS:
            player_score += 1
            pmsg = Text("Player Wins!", (340, 290), size=32)
            sleep(2)
            remove_from_screen(pmsg)
        elif result == COMPUTER_WINS:
            comp_score += 1
        else:
            return QUIT

        if player_score == 5:
            return PLAYER_WINS
        elif comp_score == 5:
            return COMPUTER_WINS


def pong():

    begin_graphics(800, 600, title="Pong", background=color.YELLOW)
    set_speed(120)

    result = play_game()

    if result == PLAYER_WINS:
        Text("Player Wins!", (340, 290), size=32)
    elif result == COMPUTER_WINS:
        Text("Computer Wins!", (340, 290), size=32)

    sleep(4)

    end_graphics()

if __name__ == "__main__":
    pong()
