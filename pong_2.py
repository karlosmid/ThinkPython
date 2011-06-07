# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 5, 2011 3:58:52 PM$"

from gasp import *

RIGHT_WINS = 1
LEFT_WINS = 0
QUIT = -1
SET = 21


def hit(bx, by, r, px, py,h):
    """
      >>> hit(760, 100, 10, 780, 100, 100)
      False
      >>> hit(770, 100, 10, 780, 100, 100)
      True
      >>> hit(770, 200, 10, 780, 100, 100)
      True
      >>> hit(770, 210, 10, 780, 100, 100)
      False
    """
    if bx >= px:
        distance = bx - px
    else:
        distance = px - bx
    if py<=by and by<=py+h and distance <= r:
        return True
    else:
        return False


def play_round():
    left_x = 10
    left_y = 140
    h = 100
    r = 5
    left = Box((left_x, left_y), r,h, filled=True)

    right_x = 780
    right_y = 140
    right = Box((right_x, right_y), r,h,filled=True)

    ball_x = 400
    ball_y = 300
    ball = Circle((ball_x, ball_y), r, filled=True)
    dx = random_between(-5, 5)
    dy = random_between(-5, 5)

    while True:       

        if ball_y >= 590 or ball_y <= 10:
            dy *= -1        
        ball_x += dx
        ball_y += dy
        if ball_x >= 810:
            remove_from_screen(ball)
            remove_from_screen(left)
            remove_from_screen(right)
            return LEFT_WINS
        elif ball_x <= 0:
            remove_from_screen(ball)
            remove_from_screen(left)
            remove_from_screen(right)
            return RIGHT_WINS
        if hit(ball_x,ball_y,r,left_x,left_y,h):
           dy *= -1
           dx *= -1
        elif hit(ball_x,ball_y,r,right_x,right_y,h):
           dy *= -1
           dx *= -1
        if key_pressed('q') and left_y <= 600-h:
            left_y += 5
        elif key_pressed('a') and left_y >= 0:
            left_y -= 5
        elif key_pressed('o') and right_y <= 600-h:
            right_y += 5
        elif key_pressed('l') and right_y >= 0:
            right_y -= 5

        if key_pressed('1'):
            return QUIT

        move_to(ball, (ball_x, ball_y))
        move_to(left, (left_x, left_y))
        move_to(right, (right_x, right_y))
        

        update_when('next_tick')


def play_game():
    left_score = 0
    right_score = 0

    while True:
        lmsg = Text("Left: %d Points" % left_score, (10, 570), size=24)
        rmsg = Text("Right: %d Points" % right_score, (620, 570), size=24)
        sleep(3)
        remove_from_screen(lmsg)
        remove_from_screen(rmsg)

        result = play_round()

        if result == LEFT_WINS:
            left_score += 1
            score = Text("Left Scores!", (340, 290), size=32)
            sleep(2)
            remove_from_screen(score)
        elif result == RIGHT_WINS:
            right_score += 1
            score = Text("Right Scores!", (340, 290), size=32)
            sleep(2)
            remove_from_screen(score)
        else:
            return QUIT

        if left_score == SET:
            return LEFT_WINS
        elif right_score == SET:
            return RIGHT_WINS


def pong():

    begin_graphics(800, 600, title="Pong", background=color.YELLOW)
    set_speed(120)

    result = play_game()

    if result == LEFT_WINS:
        Text("Left Wins!", (340, 290), size=32)
    elif result == RIGHT_WINS:
        Text("Right Wins!", (340, 290), size=32)

    sleep(4)

    end_graphics()

if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
    pong()
