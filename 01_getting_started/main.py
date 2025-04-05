from taipy.gui import Gui
import taipy.gui.builder as tgb
from math import cos, exp



# global/state vars
value = 30

def compute_data(decay: int) -> list:
    return [cos(i / 6) * exp(-i * decay / 600) for i in range(100)]

data = compute_data(value)

# reactive components
def slider_moved(state):
    state.data = compute_data(state.value)


# app page
with tgb.Page() as page:
    tgb.text(value="# Taipy Getting Started", mode="md")
    tgb.slider(value="{value}", on_change=slider_moved)
    tgb.chart(data="{data}")


Gui(page=page).run(
        run_browser=False,
        port=5555
    )
