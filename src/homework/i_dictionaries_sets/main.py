#Homework9 - Dictionaries and Sets

def get_inventory_display(inventory):
    """Returns a string representation of the current inventory."""
    if not inventory:
        return "Inventory is empty."
    display_lines = ["Current Inventory:"]
    for widget, quantity in inventory.items():
        display_lines.append(f"- {widget}: {quantity}")
    return "\n".join(display_lines)

def add_inventory(inventory, widget_name, quantity):
    """Add quantity to inventory for widget_name (require positive int)."""
    if quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return
    inventory[widget_name] = inventory.get(widget_name, 0) + quantity

def remove_inventory(inventory, widget_name, quantity):
    """Remove quantity from inventory; delete item if quantity becomes zero or less."""
    if quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return
    if widget_name not in inventory:
        print(f"Error: '{widget_name}' not found in inventory.")
        return
    if inventory[widget_name] < quantity:
        print(f"Error: Insufficient quantity of '{widget_name}' to remove.")
        return
    inventory[widget_name] -= quantity
    if inventory[widget_name] == 0:
        del inventory[widget_name]
    print(f"{quantity} '{widget_name}' removed from inventory.")    

    # Write code to create the following menu.Inventory Menu1-Add or Update Item 2-Delete Item 3-Exit
    # The program runs until the user chooses option 3.
if __name__ == "__main__":
    inventory = {}
    while True:
        print("Inventory Menu:")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")
        choice = input("Please enter your choice (1, 2, or 3): ")
        if choice == '1':
            widget_name = input("Enter widget name to add/update: ")
            quantity = int(input("Enter quantity to add: "))
            add_inventory(inventory, widget_name, quantity)
            print(get_inventory_display(inventory))
        elif choice == '2':
            widget_name = input("Enter widget name to delete: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_inventory(inventory, widget_name, quantity)
            print(get_inventory_display(inventory))
        elif choice == '3':
            print("Exiting Inventory Menu.")
            break
        else:
            print("Invalid choice. Please try again.")