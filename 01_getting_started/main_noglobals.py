from taipy.gui import Gui
import taipy.gui.builder as tgb
from math import cos, exp


def compute_data(decay_param: int) -> list:
    return [cos(i / 6) * exp(-i * decay_param / 600) for i in range(100)]


def slider_moved(state):
    state.data = compute_data(state.value)


# Create a function to build the page
def create_app():
    initial_decay = 10
    initial_data = compute_data(initial_decay)

    with tgb.Page() as page:
        tgb.text(value="# Taipy Getting Started", mode="md")
        tgb.slider(value="{value}", on_change=slider_moved)
        tgb.chart(data="{data}")

    # Initialize state with values rather than using globals
    return Gui(page=page, initialize_state={'value': initial_decay, 'data': initial_data})


if __name__ == "__main__":
    app = create_app()
    app.run(run_browser=False, port=5555)
