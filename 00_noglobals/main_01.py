from taipy import Gui

# Initial data
data = {"message": "Hello, Taipy!", "counter": 0}

# Define the page content
page = """
# My First Taipy App

<|{message}|text|>

Counter: <|{counter}|text|>

<|Increment|button|on_action=increment_counter|>
"""

# Define the callback function
def increment_counter(state):
    state.counter += 1

# Create and run the Gui
if __name__ == "__main__":
    gui = Gui(page)
    gui.run(data=data)
