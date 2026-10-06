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
        elif event.type == SDL_KEYDOWN and event.key in keys:
            keys[event.key] = True
        elif event.type == SDL_KEYUP and event.key in keys:
            keys[event.key] = False


def get_move_direction():
    dx = int(keys[SDLK_RIGHT]) - int(keys[SDLK_LEFT])
    dy = int(keys[SDLK_UP]) - int(keys[SDLK_DOWN])
    return dx, dy


def update_position():
    global x, y, direction

    dx, dy = get_move_direction()
    if dx:
        direction = dx
    x += dx * MOVE_SPEED
    y += dy * MOVE_SPEED
    x = max(FRAME_WIDTH // 2, min(CANVAS_WIDTH - FRAME_WIDTH // 2, x))
    y = max(FRAME_HEIGHT // 2, min(CANVAS_HEIGHT - FRAME_HEIGHT // 2, y))


def draw_character():
    dx, dy = get_move_direction()
    if dx or dy:
        row = 100 if direction == 1 else 0
    else:
        row = 300 if direction == 1 else 200
    character.clip_draw(frame * FRAME_WIDTH, row,
                        FRAME_WIDTH, FRAME_HEIGHT, x, y)


running = True
keys = {
    SDLK_LEFT: False,
    SDLK_RIGHT: False,
    SDLK_UP: False,
    SDLK_DOWN: False,
}
x = CANVAS_WIDTH // 2
y = CANVAS_HEIGHT // 2
direction = 1
frame = 0


while running:
    clear_canvas()
    background.clip_draw(240, 212, CANVAS_WIDTH, CANVAS_HEIGHT,
                         CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()
    handle_events()
    delay(0.05)


close_canvas()
