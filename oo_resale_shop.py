class ResaleShop:
    """This file tells readers that this is a resale shop."""
    
    def __init__(self):
        """Initialize the resale shop with an empty inventory."""
        self.inventory = []  

    def buy(self, computer):
        """After buy in a computer, this add a computer to the inventory."""
        self.inventory.append(computer)

    def sell(self, computer):
        """After sell a computer, this remove a computer from the inventory."""
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Sorry, computer not found in inventory.")


    def update_price(self, computer, new_price):
        """If there's a change in price of a certain computer, this enables us to update the price of a computer in the inventory."""         # ⭐
        if computer in self.inventory:
            computer.update_price(new_price)
        else:
            print("Error: computer not found in inventory.")  

    def refurbish(self, computer, new_os=None):
        if computer in self.inventory:
            if computer.year_made < 2000:
                computer.price = 0
            elif computer.year_made < 2012:
                computer.price = 250
            elif computer.year_made < 2018:
                computer.price = 550
        else:
            computer.price = 1000

        if new_os != None:
            computer.operating_system = new_os
        else:
            print("Computer not found. Please select another item to refurbish.")


    def print_inventory(self):
        """ This prints all computers in inventory with quantity."""
        if not self.inventory:
            print("Inventory empty.")
            return
        printed = []

        for c in self.inventory:
            if c not in printed:
                qty = self.inventory.count(c)
                print(c, "Quantity:", qty)
                printed.append(c)

