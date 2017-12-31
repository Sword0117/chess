from configurations import *
import model
import piece

class Controller():
    def __init__(self):
        self.init_model()

    def init_model(self): 
		# instantiated a new Model class within controller class
		# A way of controller to interact with model
        self.model = model.Model()

	# wrapper around function in piece class 
    def get_numeric_notation(self, position):
        return piece.get_numeric_notation(position)

	# wrapper around functions in model class
    def get_all_pieces_on_chess_board(self):
        return self.model.items()

    def reset_game_data(self):
        self.model.reset_game_data()

    def reset_to_initial_locations(self):
        self.model.reset_to_initial_locations()

