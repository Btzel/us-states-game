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
for found_state in manager.found_states:
    for states in manager.data_dict['state'].items():
        if states[1].lower() == found_state.lower():
            indexes.append(states[0])

for index in indexes:
    manager.data_dict['state'].pop(index)
    manager.data_dict['x'].pop(index)
    manager.data_dict['y'].pop(index)

missing_states_df = pd.DataFrame(manager.data_dict)
missing_states_df.to_csv("missing_states.csv")

