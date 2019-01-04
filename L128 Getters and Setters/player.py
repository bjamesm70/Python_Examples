# player.py

# Lesson 128: Getters and Setters

# Player class file.

# - Jim
# (Contact Info)


class Player(object):
    
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
    
    # Getter, and Setter section for "_lives":
    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, new_lives):
        if new_lives >= 0:
            self._lives = new_lives
        else:
            print("Can not set 'lives' to < 0.  Setting to 0.")
            self._lives = 0
            
    lives = property(fget=_get_lives, fset=_set_lives)
    
    # Getter, and Setter section for "_level":
    def _get_level(self):
        return self._level
    
    def _set_level(self, new_level):
        if new_level >= 1:
            # For every level change +/- 1,000 points
            # to the _score.
            change = new_level - self._level
            
            self._score += change * 1000
            
            self._level = new_level
    
        else:
            print("Level can't be less than '1'.")
    
    level = property(fget=_get_level, fset=_set_level)
    
    # Getter, and Setter for "_score":
    
    @property
    def score(self):
        """Score of the player"""
        return self._score
    
    @score.setter
    def score(self, new_score):
        self._score = new_score
        
    # No score.deleter at this point.
    
    # Used with printing the object:
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)