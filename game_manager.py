import pandas as pd
from turtle import Turtle

class GameManager:
    def __init__(self):
        self.data_dict = pd.read_csv("50_states.csv").to_dict()
        self.state_name = ""
        self.state_position = (0,0)
        self.found_states = []
        self.score = 0
        self.total_state_count = len(self.data_dict['state'].values())

    def compare_answer(self,answer,score):
        is_found = False
        counter = 0

        if any(answer.lower() == found_state.lower() for found_state in self.found_states):
                return False,"","",score

        for state_name in self.data_dict['state'].values():
            if answer.lower() == state_name.lower():
                is_found = True
                self.state_name = state_name.title()
                self.state_position = (self.data_dict['x'][counter],
                                       self.data_dict['y'][counter])
                self.found_states.append(self.state_name)
                score += 1
                break
            counter += 1

        return is_found,self.state_name,self.state_position,score
    @staticmethod
    def create_state(text,state_pos):
        text_instance = Turtle()
        text_instance.shape("circle")
        text_instance.shapesize(stretch_len=0.5,stretch_wid=0.5)
        text_instance.penup()
        text_instance.goto(state_pos)
        text_instance.write(arg=text, align="center", font=("Courier", 10, "normal"))


