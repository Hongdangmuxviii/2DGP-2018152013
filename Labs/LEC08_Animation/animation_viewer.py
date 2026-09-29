from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BASE_DIR = Path(__file__).resolve().parent


def asset_path(relative_path):
    return str(BASE_DIR / relative_path)


RUN_SHEET = asset_path('assets/fox_swordswoman_run_12f.png')
GUARD_SHEET = asset_path('assets/fox_swordswoman_guard_12f.png')
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
run_frame = 0


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
grass = load_image(asset_path('grass.png'))
run_sheet = load_image(RUN_SHEET)
guard_sheet = load_image(GUARD_SHEET)

while True:
    left, bottom, width, height = RUN_FRAMES[run_frame]
    clear_canvas()
    grass.draw(CANVAS_WIDTH // 2, 30)
    run_sheet.clip_draw(left, bottom, width, height, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, 360, 360)
    update_canvas()
    delay(0.07)
    run_frame = (run_frame + 1) % len(RUN_FRAMES)

close_canvas()
