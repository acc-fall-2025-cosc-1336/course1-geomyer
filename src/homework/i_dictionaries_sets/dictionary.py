cities = {'Georgia': 'Atlanta', 'New York': 'Albany', 'California': 'San Diego'}

if 'FL' in cities:
    del cities['FL']  # This will raise a NameError because FL is not defined
cities['FL'] = 'Tallahassee'  # This will also raise a NameError because FL is not defined    
print(cities)



#Homework #9 rite a non-value function named add_inventory with a widgets parameter of type dictionary, widget_name, and quantity.
#The function will add the widget to the dictionary if it doesn't exist. If the widget exists it will update the quantity of the widgets.


def add_inventory(widgets, widget_name, quantity):
    """Adds a specified quantity of a widget to the inventory."""
    if not isinstance(quantity, int) or quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return

    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity
        print(f"{quantity} '{widget_name}' added to inventory.")
class Inventory:
    def __init__(self):
        self.inventory = {}

def remove_inventory_widget(self, widget_name, quantity):
        """Removes a specified quantity of a widget from the inventory."""
        if not isinstance(quantity, int) or quantity <= 0:
            print("Error: Quantity must be a positive integer.")
            return

        if widget_name not in self.inventory:
            print(f"Error: '{widget_name}' not found in inventory.")
            return

        if self.inventory[widget_name] < quantity:
            print(f"Error: Insufficient quantity of '{widget_name}' to remove.")
            return

        self.inventory[widget_name] -= quantity
        if self.inventory[widget_name] == 0:
            del self.inventory[widget_name]  # Remove widget entirely if quantity reaches zero
        print(f"{quantity} '{widget_name}' removed from inventory.")

