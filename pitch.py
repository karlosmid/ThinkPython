# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Jun 5, 2011 3:27:45 PM$"

from gasp import *

def randomGasp():
    i = 0
    while i<10:
        print random_between(-5,5)
        i += 1

def blackBall():
    begin_graphics(800, 600, title="Catch", background=color.YELLOW)
    set_speed(120)

    ball_x = 10
    ball_y = 300
    ball = Circle((ball_x, ball_y), 10, filled=True)
    dx = 4
    dy = random_between(-4,4)

    while ball_x < 810:
        if ball_y >= 590 or ball_y <= 10:
            dy *= -1
        ball_x += dx
        ball_y += dy
        move_to(ball, (ball_x, ball_y))
        update_when('next_tick')

    end_graphics()

if __name__ == "__main__":
    blackBall()
#    randomGasp()
