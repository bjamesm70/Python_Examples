# ducks.py

# Lesson 138: Duck Test

# Teaching polymorphism, and the duck test.

# - Jim
# (contact info)


class Wing():
    
    def __init__(self, ratio):
        
        # Lift to weight ratio for wing.
        self._ratio = ratio
    
    def fly(self):
        
        if self._ratio > 1:
            
            print("Weee!  Flying is fun.")
        
        elif self._ratio == 1:
            
            print("This is hard work.  But. I'm flying.")
        
        else:
            
            print("I think I'll just walk.")


class Duck():
    
    def __init__(self):
        # Lift to weight ratio for wing.
        self._wing = Wing(1.8)
    
    def walk(self):
        print("Waddle, waddle, waddle")
    
    def swim(self):
        print("Come on it.  The water's lovely.")
    
    def quack(self):
        print("Quack quack")
    
    def fly(self):
        # Call your wing's fly class:
        self._wing.fly()


class Penguin():
    
    def walk(self):
        print("Waddle, waddle, I waddle, too!")
    
    def swim(self):
        print("Come on in.  But, it's a bit chilly this far south.")
    
    def quack(self):
        print("Are you having a laugh?!  I'm a penguin!")


#########################
# End Class Definitions #
#########################

def test_duck(duck):
    """
    :param duck: Duck
    :return:
    """
    duck.walk()
    duck.swim()
    duck.quack()


# Only run this code, if this python file
# is the main file.  Don't run it if this
# file is imported.
if __name__ == "__main__":
    donald = Duck()
    
    test_duck(donald)
    
    percy = Penguin()
    
    test_duck(percy)
    
    print("-" * 40)
    
    donald.fly()
