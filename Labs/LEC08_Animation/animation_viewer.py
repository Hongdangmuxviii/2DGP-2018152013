from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BASE_DIR = Path(__file__).resolve().parent


def asset_path(relative_path):
    return str(BASE_DIR / relative_path)


RUN_SHEET = asset_path('assets/fox_swordswoman_run_12f.png')
GUARD_SHEET = asset_path('assets/fox_swordswoman_guard_12f.png')
JUMP_SHEET = asset_path('assets/fox_swordswoman_jump_10f.png')
ATTACK_SHEET = asset_path('assets/fox_swordswoman_attack_12f.png')
RUN_FRAMES = (
    (0, 724, 362, 362),
    (362, 724, 362, 362),
    (724, 724, 362, 362),
    (1086, 724, 362, 362),
    (0, 362, 362, 362),
    (362, 362, 362, 362),
    (724, 362, 362, 362),
    (1086, 362, 362, 362),
    (0, 0, 362, 362),
    (362, 0, 362, 362),
    (724, 0, 362, 362),
    (1086, 0, 362, 362),
)
GUARD_FRAMES = (
    (0, 724, 362, 362),
    (362, 724, 362, 362),
    (724, 724, 362, 362),
    (1086, 724, 362, 362),
    (0, 362, 362, 362),
    (362, 362, 362, 362),
    (724, 362, 362, 362),
    (1086, 362, 362, 362),
    (0, 0, 362, 362),
    (362, 0, 362, 362),
    (724, 0, 362, 362),
    (1086, 0, 362, 362),
)
JUMP_FRAMES = (
    (0, 397, 396, 396),
    (396, 397, 397, 396),
    (793, 397, 397, 396),
    (1190, 397, 396, 396),
    (1586, 397, 397, 396),
    (0, 0, 396, 397),
    (396, 0, 397, 397),
    (793, 0, 397, 397),
    (1190, 0, 396, 397),
    (1586, 0, 397, 397),
)
ATTACK_FRAMES = (
    (0, 724, 362, 362),
    (362, 724, 362, 362),
    (724, 724, 362, 362),
    (1086, 724, 362, 362),
    (0, 362, 362, 362),
    (362, 362, 362, 362),
    (724, 362, 362, 362),
    (1086, 362, 362, 362),
    (0, 0, 362, 362),
    (362, 0, 362, 362),
    (724, 0, 362, 362),
    (1086, 0, 362, 362),
)
action_index = 0
frame_index = 0


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
grass = load_image(asset_path('grass.png'))
run_sheet = load_image(RUN_SHEET)
guard_sheet = load_image(GUARD_SHEET)
jump_sheet = load_image(JUMP_SHEET)
attack_sheet = load_image(ATTACK_SHEET)

actions = (
    (run_sheet, RUN_FRAMES),
    (guard_sheet, GUARD_FRAMES),
    (jump_sheet, JUMP_FRAMES),
    (attack_sheet, ATTACK_FRAMES),
)

while True:
    sheet, frames = actions[action_index]
    left, bottom, width, height = frames[frame_index]
    clear_canvas()
    grass.draw(CANVAS_WIDTH // 2, 30)
    sheet.clip_draw(left, bottom, width, height, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, 360, 360)
    update_canvas()
    delay(0.07)
    frame_index += 1
    if frame_index == len(frames):
        frame_index = 0
        action_index = (action_index + 1) % len(actions)

close_canvas()
