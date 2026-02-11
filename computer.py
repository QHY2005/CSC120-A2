class Computer:
    """
    This is the computer store that contains the information about a single computer in the resale shop.
    """

    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        """Initialize and define the information of computer, with all the detailed information"""
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def Update_Price(self, new_price: int) -> None:
        """This will update the price of the computer if there's ever changes in the price of the computers in the resale shop."""
        self.price = new_price

    def Update_OS(self, new_os: str) -> None:
        """This will update the OS of the computer if there's ever changes in the OS of the computers in the resale shop."""
        self.operating_system = new_os

    

    def __str__(self):
        """This return a string that represent all the information we have collected of the computer."""
        description = self.description
        processor = " Processor: " + self.processor_type
        storage = " Storage: " + str(self.hard_drive_capacity)
        memory = " Memory: " + str(self.memory)
        os = " OS: " + self.operating_system
        year = " Year: " + str(self.year_made)
        price = " Price: " + str(self.price)
        return description + processor + storage + memory + os + year + price

