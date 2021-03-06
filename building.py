"""
Module which contains classes related to building.
"""
class Building:
    def __init__(self, address: str):
        """
        Creates an object of class Building.

        >>> building_one = Building("Kozelnytska st. 2a")
        >>> building_one.address
        'Kozelnytska st. 2a'
        """
        self.address = address


class Classroom:
    '''
    Makes a class for work with data about classrooms.
    '''
    def __init__(self, number, capacity, equipment):
        """
        Creates a new classroom.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment


    def __str__(self):
        """
        Represents this object in human language.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        """
        return """Classroom {0} has a capacity of {1} persons and has the following \
equipment: {2}.""".format(self.number, self.capacity, ", ".join(self.equipment))


    def is_larger(self, oth_room):
        """
        Gives an answer about which room can accommodate more people.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        return self.capacity > oth_room.capacity


    def equipment_differences(self, oth_room):
        """
        Compares equipment amoung rooms.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'projector', 'mic']
        """
        unique_equipment = []
        for thing in self.equipment:
            if thing not in oth_room.equipment:
                unique_equipment.append(thing)
        return unique_equipment


    def __repr__(self):
        """
        Represents this object in more-like-computer language.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> [classroom_016]
        [Classroom('016', 80, ['PC', 'projector', 'mic'])]
        """
        class_name = type(self).__name__
        return f"{class_name}('{self.number}', {self.capacity}, {self.equipment})"


class AcademicBuilding(Building):
    """
    Make a class to work with data about educational building.
    """
    def __init__(self, address, rooms):
        """
        Creates a new building.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        """
        super().__init__(address)
        self.classrooms = rooms


    def total_equipment(self):
        """
        Gives information about all equipment in the building.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
        """
        first_lst = []
        sec_lst = []

        for room in self.classrooms:
            for thing in room.equipment:
                first_lst.append(thing)

        for equipment in first_lst:
            element = tuple([equipment, first_lst.count(equipment)])
            sec_lst.append(element)

        sec_lst = list(set(sec_lst))
        sec_lst.sort()
        return sec_lst


    def __str__(self):
        """
        Represents this object in human language.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        result = self.address

        for room in self.classrooms:
            result += '\n' + room.__str__()

        return result


class House(Building):
    def __init__(self, address, rooms: list):
        """
        Creates an object of class Building.

        >>> rooms_info = ['room_1', 'room_2']
        >>> house_one = House("Kozelnytska st. 2a", rooms_info)
        >>> house_one.address
        'Kozelnytska st. 2a'
        >>> house_one.rooms
        ['room_1', 'room_2']
        """
        super().__init__(address)
        self.rooms = rooms


if __name__ == "__main__":
    import doctest
    doctest.testmod()
