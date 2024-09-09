"""CandyLandShake class

This is a class that creates the Candy Land Shake
drink menu item.

Author: Mason Pride mtpride@ksu.edu
Version: 0.1
"""

from typing import List, Set
from src.gamegrub.data.enums.Size import Size


class CandyLandShake:
    """Represents the Candy Land Shake drink

    This class builds the CandyLandShake drink 
    menu item.
    """

    def __init__(self) -> None:
        """Initializes the class

        Creates the CandyLandShake object with
        preset price, calories, size, and topping attributes.
        """
        self.__size: Size = Size.JUNIOR
        self.__price: float = 5.75
        self.__calories: int = 770
        self.__chocolate: bool = True
        self.__vanilla: bool = False
        self.__strawberry: bool = False
    
    @property
    def size(self) -> Size:
        """Size attibute getter method

        Gets the size attribute of the class.

        Returns:
            size attribute of the class; of type Size
        """
        return self.__size

    @size.setter
    def size(self, value: Size) -> None:
        """Size attibute setter method

        Sets the size, price, and calories 
        attribute of the class to the desired Size.

        Args: 
            value: The desired Size from Size enum class
        """
        self.__size = value
        if value == Size.CLASSIC:
            self.__price = 7.45
            self.__calories = 1215
        elif value == Size.WINNER:
            self.__price = 9.55
            self.__calories = 1465
        else:
            self.__price = 5.75
            self.__calories = 770

    @property
    def price(self) -> float:
        """Price attibute getter method

        Gets the price attribute of the class.

        Returns:
            price attribute of the object; of type float
        """
        return self.__price

    @property
    def calories(self) -> int:
        """Calories attribute getter method

        Gets the calories attribute of the class.

        Returns:
            calories attribute of the object; of type int
        """
        return self.__calories

    @property
    def chocolate(self) -> bool:
        """Chocolate attribute getter method

        Gets the chocolate attribute of the class.

        Returns:
            True if the drink has chocolate; 
            False if not
        """
        return self.__chocolate
    
    @chocolate.setter
    def chocolate(self, value: bool) -> None:
        """Chocolate attribute setter method

        Sets the chocolate attribute of the class to 
        the desired setting.

        Args: 
            value: Boolean describing topping
            setting
        """
        self.__chocolate = value

    @property
    def vanilla(self) -> bool:
        """Vanilla attribute getter method

        Gets the vanilla attribute of the class.

        Returns:
            True if the drink has vanilla; 
            False if not
        """
        return self.__vanilla
    
    @vanilla.setter
    def vanilla(self, value: bool) -> None:
        """Vanilla attribute setter method

        Sets the vanilla attribute of the class to 
        the desired setting.

        Args: 
            value: Boolean describing topping
            setting
        """
        self.__vanilla = value

    @property
    def strawberry(self) -> bool:
        """Strawberry attribute getter method

        Gets the strawberry attribute of the class.

        Returns:
            True if the drink has strawberry; 
            False if not
        """
        return self.__strawberry
    
    @strawberry.setter
    def strawberry(self, value: bool) -> None:
        """Strawberry attribute setter method

        Sets the strawberry attribute of the class to 
        the desired setting.

        Args: 
            value: Boolean describing topping
            setting
        """
        self.__strawberry = value

    @property
    def instructions(self) -> List[str]:
        """Shows the list of instructions

        This method will return a list of the 
        special instructions given to the drink.

        Returns:
            List of strings containing the special instructions
        """
        instruct: List[str] = []
        if not self.__chocolate:
            instruct.append("Hold Chocolate")
        if self.__vanilla:
            instruct.append("Add Vanilla")
        if self.__strawberry:
            instruct.append("Add Strawberry")
        return instruct.copy()

    def __str__(self) -> str:
        """String overide method

        Creates a string of the drink
        menu item.

        Returns:
            str representing the size and drink
        """
        return "{} Candy Land Shake".format(self.__size)

    def __eq__(self, value: object) -> bool:
        """Equals overide method

        Checks to see if two menu items are equal.

        Args:
            value: Object representing a drink item
        Returns:
            True if items are equal; 
            False if not
        """
        if isinstance(value, CandyLandShake):
            return (self.__size == value.size and
                    self.__price == value.price and
                    self.__calories == value.calories and
                    self.__chocolate == value.chocolate and
                    self.__vanilla == value.vanilla and
                    self.__strawberry == value.strawberry)
        else:
            return False
