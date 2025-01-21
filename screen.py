import turtle

class Screen:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.screen.setup(width=750,height=500)
        self.load_image()

    def load_image(self):
        image = "blank_states_img.gif"
        self.screen.addshape(image)
        turtle.shape(image)
    def get_answer(self,score,total_state_count):
        answer_state = self.screen.textinput(title=f"{score}/{total_state_count} States Correct",
                                             prompt="What's another state's name?").lower()
        return answer_state