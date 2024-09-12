class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception('Title must be in a string format')
        
        if hasattr(self, '_title') and self._title is not None:
            raise Exception('Cannot change title once made')
        
        if not len(value) > 0:
            raise Exception('Title must be written')
        self._title = value
    
    def add_result(self, value):
        if not isinstance(value, Result):
            raise Exception('result mus be an instance of Result')
        self._results.append(value)
    
    def results(self):
        return self._results

    def players(self):
        players_done = set()
        
        for result in self._results:
            if isinstance(result.player, Player):
                players_done.add(result.player)
                
        return list(players_done)

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username
        self._results = []
        
    @property
    #  I'm using property to check if certain criteria are met
    def username(self):
        return self._username
    
    @username.setter
    # filling in criteria to be met
    def username(self, value):
        if not isinstance(value, str):
            raise Exception('Name must be in string format')
        
        if not (2 <= len(value) <= 16):
            raise Exception('Name must be between 2 and 16 characters')
        
        self._username = value
        
    def add_results(self, result):
        if not isinstance(result, Result):
            raise Exception('results must be an instance of Result')
        self._results.append(result)
        
    def results(self):
        return self._results

    def games_played(self):
        
        games_done = set()
        
        for result in self._results:
            if isinstance(result.game, Game):
                games_done.add(result.game)
        return list(games_done)

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        
        Result.all.append(self)
        player.add_results(self)
        game.add_result(self)
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, amount):
        if not isinstance(amount, int):
            raise Exception('The amount must be an integer')
        
        if not (1 <= amount <= 5000):
            raise Exception('The amount can only be between 1 and 5000')
        
        if hasattr(self, '_score') and self._score is not None:
            raise Exception('The score cannot be changed')
        self._score = amount
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, value):
        if not isinstance(value, Player):
            raise Exception('player must be a Player')
        self._player = value
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, value):
        if not isinstance(value, Game):
            raise Exception('game must be part of Game')
        self._game = value