from taipy.gui import Gui
import taipy.gui.builder as tgb
import pandas as pd

from dataclasses import dataclass, field

"""
*********************************************************************
this is rubbish, globals okay, just organize better
*********************************************************************
"""



# global cache for raw data
_DATA = None

@dataclass
class TPglobals:
    data: pd.DataFrame = field(default_factory=pd.DataFrame)
    chart_data: pd.DataFrame = field(default_factory=pd.DataFrame)
    categories: list = field(default_factory=list)
    selected_category: str = ""
    layout: dict = field(default_factory=dict)


def read_data():
    global _DATA
    if _DATA is None:
        _DATA = pd.read_csv("../data.csv")
    return _DATA

def init_chart_data(data):
    chart_data = (
        data.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    return chart_data

def get_categories(data):
    categories = list(data["Category"].unique())
    return categories


def run_application():

    app_globals = TPglobals(
        data = read_data(),
        chart_data = init_chart_data(read_data()),
        categories = get_categories(read_data()),
        selected_category = get_categories(read_data())[0],
        layout = {"yaxis": {"title": "Revenue (USD)"}, "title": "Sales by State"}
    )

    def change_category(state):
        state.app_globals.data = app_globals.data[app_globals.data["Category"] == state.app_globals.selected_category]
        state.app_globals.chart_data = (
            state.app_globals.data.groupby("State")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        state.app_globals.layout = {
            "yaxis": {"title": "Revenue (USD)"},
            "title": f"Sales by State for {state.app_globals.selected_category}",
        }


    with tgb.Page() as page:
        tgb.selector(value="{app_globals.selected_category}",
                        lov=app_globals.categories,
                        on_change=change_category
                    )
        tgb.chart(
            data="{app_globals.chart_data}",
            x="State",
            y="Sales",
            type="bar",
            layout="{app_globals.layout}",
        )
        tgb.html("br")
        tgb.table(data="{app_globals.data}")

    Gui(page=page).run(
            run_browser=False,
            port=5555,
            title="Sales",
            dark_mode=False)

run_application()
