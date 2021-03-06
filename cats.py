"""
Module which contains classes Cat and Animal.
"""
class Animal:
    """
    Class for describing animal's properties.
    """
    def __init__(self, phylum, clas):
        """
        Initializes an object of class Animal and sets its properties.

        >>> animal1 = Animal("chordata", "mammalia")
        >>> assert(animal1.phylum == "chordata")
        >>> assert(animal1.clas == "mammalia")
        >>> animal2 = Animal("chordata", "birds")
        >>> assert(not (animal1 == animal2))
        """
        self.phylum = phylum
        self.clas = clas


    def __str__(self):
        """
        Represents this object in more-like-human language.

        >>> animal1 = Animal("chordata", "mammalia")
        >>> assert(str(animal1) == "<animal class is mammalia>")
        """
        return f"<animal class is {self.clas}>"


class Cat(Animal):
    """
    Class for describing cat's properties.
    """
    def __init__(self, phylum, clas, genus):
        """
        Initializes an object of class Cat and sets its properties.

        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> assert(cat1.genus == "felis")
        >>> assert(isinstance(cat1, Animal))
        """
        super().__init__(phylum, clas)
        self.genus = genus


    def sound(self):
        """
        Barsic(imagine it's your cat's name)! Say 'Meow'!

        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> assert(cat1.sound() == "Meow")
        """
        return "Meow"


    def __str__(self):
        """
        Represents this object in more-like-human language.

        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> assert(str(cat1) == "<This felis animal class is mammalia>")
        """
        return f"<This {self.genus} animal class is {self.clas}>"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
