from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BASE_DIR = Path(__file__).resolve().parent


def asset_path(relative_path):
    return str(BASE_DIR / relative_path)


RUN_SHEET = asset_path('assets/fox_swordswoman_run_12f.png')
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


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
grass = load_image(asset_path('grass.png'))
run_sheet = load_image(RUN_SHEET)
grass.draw(CANVAS_WIDTH // 2, 30)
run_sheet.clip_draw(0, 724, 362, 362, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, 360, 360)
update_canvas()
delay(1)
close_canvas()
