from pico2d import *
import math

open_canvas(800, 600)
charactor = load_image('character.png')
degree =0

def move_circle (): 
    print('CIRCLE')
    clear_canvas()
    charactor.draw(400,300)
    theta = math.radians(degree)
    x = 400 + 200 * math.cos(theta)
    y = 300 + 200 * math.sin(theta)
    def move_circle():
     for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        charactor.draw(x, y)
        update_canvas()
        delay(0.01)
    update_canvas()
    pass

def move_rectangle():
    print('RECTANGLE')
    pass

def move_triangle():
    print('TRIANGLE')
    pass
while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


close_canvas()