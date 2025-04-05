
import sys
from math import cos, exp
from typing import List
from dataclasses import dataclass, field

import taipy.gui.builder as tgb
from taipy.gui import Gui

DEFAULT_INIT_VALUE = 10

@dataclass
class TPvars:
    value: int = 0
    data: list[float] = field(default_factory=list)


def compute_data(decay: int) -> list:
    return [cos(i / 6) * exp(-i * decay / 600) for i in range(100)]


def run_application(init_value:int = DEFAULT_INIT_VALUE):

    app_globals = TPvars(
        value=init_value,
        data = compute_data(init_value)
    )


    # reactive components
    def slider_moved(state):
        state.app_globals.data = compute_data(state.app_globals.value)


    # app main page
    with tgb.Page() as page:
        tgb.text(value="# Taipy Getting Started", mode="md")
        tgb.slider(value="{app_globals.value}", on_change=slider_moved)
        tgb.chart(data="{app_globals.data}")

    # run taipy gui app
    Gui(page=page).run(
            run_browser=False,
            port=5555
        )

if __name__ == "__main__":
    try:
        init_value = int(sys.argv[1])
    except (IndexError, ValueError):
        init_value = DEFAULT_INIT_VALUE

    run_application(init_value)

