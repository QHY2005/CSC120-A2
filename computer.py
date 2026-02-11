class Computer:
    """
    This is the computer store that contains the information about a single computer in the resale shop.
    """

    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        """Initialize and define the computer information."""
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def Update_Price(self, new_price: int) -> None:
        self.price = new_price

    def Update_OS(self, new_os: str) -> None:
        self.operating_system = new_os

    def __str__(self):
        description = self.description
        processor = " Processor: " + self.processor_type
        storage = " Storage: " + str(self.hard_drive_capacity)
        memory = " Memory: " + str(self.memory)
        os = " OS: " + self.operating_system
        year = " Year: " + str(self.year_made)
        price = " Price: " + str(self.price)
        return description + processor + storage + memory + os + year + price

