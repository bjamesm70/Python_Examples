# enemy.py

# Parent class for all the enemies in the game,
# and the specific enemy classes that inherit from it.

# - Jim
# (Contact Info)

import random  # Used for chance of dodging an attack.

class Enemy:
    
    """Base class of enemies."""
    
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
        
    def take_damage(self, damage):
        
        remaining_points = self._hit_points - damage
        
        if remaining_points >= 0:
            
            self._hit_points = remaining_points
            print("I took {} points, and have {} left.".format(damage, self._hit_points))
        
        else:
            self._lives -= 1
            
            if self._lives > 0:
                print("{0._name} lost a life.".format(self))
                
                # Future code: reset hit point to original level.
            
            else:
                print("{0._name} is dead.".format(self))
                self._alive = False
                self._hit_points = 0
    
    def __str__(self):
        
        return "Name: {0._name}, Lives: {0._lives}, Hit Points: {0._hit_points}". format(self)
    
    
class Troll(Enemy):
    
    # "Troll" is a subclass of "Enemy".
    
    def __init__(self, name):
        
        # Call the parent class:
        # Python 2 (and later) format:
        ##Enemy.__init__(self, _name=_name, _lives=1, _hit_points=23)

        # Python 3 (only) format:
        #super(Troll, self).__init__(_name=_name, _lives=1, _hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)
        
    def grunt(self):
        
        print("Me {0._name}.  {0._name} stomp you!".format(self))


class Vampyre(Enemy):

    # Vampyre is a subclass of "Enemy".

    def __init__(self, name):
        
        super().__init__(name=name, lives=3, hit_points=12)
    
    def dodges(self):
        
        # The Vampyre has a random chance of dodging an attack.
        
        if random.randint(1, 3) == 3:
            
            # Sucessful dodge:
            print("***** {0._name} dodges *****".format(self))
            return True
        
        else:
            
            return False
     
    # Subclass overriding example:
    def take_damage(self, damage):
        
        # See if the vampyre dodged the attack:
        if not self.dodges():
            
            # Didn't dodge.
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):
    
    # Subclass of Vampyre.
    # 140 hit points.
    # Only takes 1/4th the damage.

    def __init__(self, name):
        
        super().__init__(name=name)
        
        # We can't set "lives", nor "hit_points" in the Vampyre class init method.
        self._lives = 3
        self._hit_points = 140
        
    def take_damage(self, damage):
        
        # Only takes 1/4 the damage.
        super().take_damage(damage=(damage // 4))