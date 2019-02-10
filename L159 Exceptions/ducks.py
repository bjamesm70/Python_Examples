# ducks.py

# Lesson 138: Duck Test
# Revisited in Lesson 162: Raising Exceptions

# Teaching polymorphism, and the duck test.

# - Jim
# (contact info)


class Wing:
    
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


class Duck:
    
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


class Penguin:
    
    def __init__(self):
        self.fly = self.aviate
    
    def walk(self):
        print("Waddle, waddle, I waddle, too!")
    
    def swim(self):
        print("Come on in.  But, it's a bit chilly this far south.")
    
    def quack(self):
        print("Are you having a laugh?!  I'm a penguin!")
        
    def aviate(self):
        print("I won the lottery, and bought a learjet.")


class Mallard(Duck):

    pass


class Flock(object):
    
    def __init__(self):
        self.flock = []
    
    def add_duck(self, input_duck: Duck) -> None:
        
        # Adds the given 'input_duck' to the flock
        # if he/she can fly.
        
        # Check to see if it has a 'fly' method.
        # If not, return "None".  (If we don't
        # provide "None", then the 'getattr'
        # function retuns an exception: 'AttributeError'
        # by default which will crash your program if
        # not handled!)  If the attribute is found,
        # it returns the attribute.
        fly_method = getattr(input_duck, "fly", None)
        
        # "callable" checks if the returned object is
        # "callable" aka it's a method not a variable.
        # See: https://docs.python.org/3/library/functions.html#callable
        # for more info.
        if callable(fly_method):
            self.flock.append(input_duck)
        else:
            # TypeError: (from python's documentation):
            # Raised when an operation or function is applied to an object of inappropriate type.
            # The associated value is a string giving details about the type mismatch.
            # "__name__" to get a clean description of the object.
            raise TypeError("Can not add duck.  Are you sure it's not a '{}'?".format(str(type(input_duck).__name__)))
        
    def migrate(self):
        
        # If there are any issues during take-off,
        # save the error for later.
        # Note: this is not completely helpful as it
        # can only save 1 exception.
        caught_exception = None
        
        # Time to fly.
        for one_duck in self.flock:
            try:
                one_duck.fly()
                # TODO: Remove the 'raise' before releasing the code.
                # TODO: Only for testing.
                # TODO: Leaving in 'TODO' as an example.
                # raise AttributeError("testing exception: 'AttributeError'.")
            
            except AttributeError as caught_exception:
                
                # Saving the error for later, after
                # the rest of the flock is up, in
                # the air.
                print("One duck down!")

        if caught_exception:
            raise caught_exception

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
