from dino_runner.components.obstacles.obstacle_manager import ObstacleManger


class ResetGame:

    def __init__(self):

        self.obstacle_manager = ObstacleManger()

    def run(self, game):

        game.game_speed = 20
        game.score = 0
        game.playing = True

        

