"""
Module which contains classes Furniture and Chair.
"""
class Furniture:
    '''
    Makes a class for work with data about furniture.
    '''
    def __init__(self, style, assign):
        """
        Initializes an object of class Furniture and sets it's properties.

        >>> furniture1 = Furniture("empire", "bedroom")
        >>> furniture2 = Furniture("modern", "bathroom")
        >>> assert(not (furniture1 == furniture2))
        >>> assert(furniture1.style == "empire")
        >>> assert(furniture1.assign == "bedroom")
        """
        self.style = style
        self.assign = assign


    def __str__(self):
        """
        Represents this object in more-like-human language.

        >>> furniture1 = Furniture("empire", "bedroom")
        >>> assert(str(furniture1) == "<furniture style is empire>")
        """
        return f"<furniture style is {self.style}>"


class Chair(Furniture):
    '''
    Makes a class for work with data about chairs.
    '''
    def __init__(self, style, assign, tipe):
        """
        Initializes an object of class Chair and sets it's properties.

        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> assert(chair1.style == "empire")
        >>> assert(chair1.assign == "bedroom")
        >>> assert(chair1.tipe == "armchair")
        >>> assert(isinstance(chair1, Furniture))
        """
        super().__init__(style, assign)
        self.tipe = tipe


    def __str__(self):
        """
        Represents this object in more-like-human language.

        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> assert(str(chair1) == "<This armchair furniture style is empire>")
        """
        return f"<This {self.tipe} furniture style is {self.style}>"


    def get_assign(self):
        """
        Returns Chair's assign.

        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> assert(chair1.get_assign() == "bedroom")
        """
        return self.assign


if __name__ == "__main__":
    import doctest
    doctest.testmod()
