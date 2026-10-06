from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAME_COUNT = 8
MOVE_SPEED = 5


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


running = True
keys = {
    SDLK_LEFT: False,
    SDLK_RIGHT: False,
    SDLK_UP: False,
    SDLK_DOWN: False,
}
frame = 0


close_canvas()
