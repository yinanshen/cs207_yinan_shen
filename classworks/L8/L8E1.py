class Dog:
    def __init__(self, breed, colors, special=None):
        self.breed = breed
        self.colors = colors
        self.special = special

    @classmethod
    def beagle(cls):
        return cls('beagle', ['black', 'white', 'brown'], 'hunting')

if __name__ == "__main__":  
    my_dog = Dog.beagle()
    print((my_dog))
    print(vars(my_dog))
