from taipy.gui import Gui
import taipy.gui.builder as tgb
from math import cos, exp



# global/state vars

def compute_data(decay: int) -> list:
    return [cos(i / 6) * exp(-i * decay / 600) for i in range(100)]


# reactive components
def slider_moved(state):
    state.data = compute_data(state.decay)


# app page
INIT_DECAY = 30
INIT_DATA = compute_data(INIT_DECAY)


with tgb.Page() as page:
    tgb.text(value="# Taipy Getting Started", mode="md")
    tgb.slider(value="{decay:INIT_DECAY}", on_change=slider_moved)
    tgb.chart(data="{data:INIT_DATA}", x="i", y="y", mode="line")


Gui(page=page).run(
        run_browser=False,
        port=5555
    )
