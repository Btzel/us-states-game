from screen import Screen
from game_manager import GameManager
import pandas as pd
screen = Screen()
manager = GameManager()

game_is_on = True
while True:
    answer = screen.get_answer(manager.score,manager.total_state_count)
    if answer == "exit":
        break
    is_found,state_name,state_position,manager.score = manager.compare_answer(answer,manager.score)
    if is_found:
        manager.create_state(state_name,state_position)

indexes = []

[indexes.append(states[0]) for states in manager.data_dict['state'].items() for found_state in manager.found_states if states[1].lower() == found_state.lower()]
[manager.data_dict[key].pop(index) for index in indexes for key in ['state','x','y']]

missing_states_df = pd.DataFrame(manager.data_dict)
missing_states_df.to_csv("missing_states.csv")

