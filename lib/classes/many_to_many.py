class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception('Title must be in a string format')
        
        if hasattr(self, '_title') and self._title is not None:
            raise Exception('Cannot change title once made')
        
        if not (2 <= len(value) <= 16):
            raise Exception('Title must be between 2 and 16 characters')
        self._title = value
        
    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score