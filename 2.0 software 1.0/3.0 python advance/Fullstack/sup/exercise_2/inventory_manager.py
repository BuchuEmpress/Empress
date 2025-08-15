import datetime

# Initialize the inventory dictionary
# Each item is a key with a value being a dictionary of its details
inventory = {}

def add_item(inventory, item_name, price, stock, category):
    """Adds a new item to the inventory. Checks if the item already exists to prevent duplicates."""
    if item_name in inventory:
        return f"Error: Item '{item_name}' already exists."
    # Add the new item with provided details
    inventory[item_name] = {
        'price': price,
        'stock': stock,
        'category': category,
        'last_updated': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Record timestamp
    }
    return f"Item '{item_name}' added successfully."

def list_inventory(inventory):
    """Lists the inventory with item numbers."""
    if not inventory:
        return "Inventory is empty."
    inventory_str = "Inventory Items:\n"
    for idx, (item_name, item_details) in enumerate(inventory.items(), start=1):
        inventory_str += f"{idx}. {item_name}:\n"
        inventory_str += f" Price: FCFA{item_details['price']:.2f}\n"
        inventory_str += f" Stock: {item_details['stock']}\n"
        inventory_str += f" Category: {item_details['category']}\n"
        inventory_str += f" Last Updated: {item_details['last_updated']}\n"
        inventory_str += "-" * 20 + "\n"
    return inventory_str

def update_stock(inventory, item_name, new_stock):
    """Updates the stock quantity for an existing item."""
    if item_name not in inventory:
        return f"Error: Item '{item_name}' not found."
    # Update stock and timestamp
    inventory[item_name]['stock'] = new_stock
    inventory[item_name]['last_updated'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Stock for '{item_name}' updated successfully."

def search_by_category(inventory, category):
    """Returns a dictionary of items matching the given category."""
    matching_items = {}
    for item_name, item_data in inventory.items():
        if item_data['category'].lower() == category.lower():
            matching_items[item_name] = item_data
    return matching_items

def format_currency(amount):
    return "FCFA{:,.2f}".format(amount)

def low_stock_alert(inventory, low_threshold):
    """Finds all items with stock less than the threshold."""
    low_stock_items = {}
    for item_name, item_data in inventory.items():
        if item_data['stock'] < low_threshold:
            low_stock_items[item_name] = item_data
    return low_stock_items

def calculate_total_value(inventory):
    """Calculates total value by summing (price * stock) for all items."""
    total_value = 0
    for item_name, item_data in inventory.items():
        total_value += item_data['price'] * item_data['stock']
    return total_value

def display_inventory(inventory):
    """Returns the current inventory items in a formatted manner."""
    if not inventory:
        return "Inventory is empty."
    inventory_str = ""
    for item_name, item_data in inventory.items():
        inventory_str += "--" * 10 + "\n"
        inventory_str += f"Item: {item_name}\n"
        inventory_str += f" Price: FCFA{item_data['price']:.2f}\n"
        inventory_str += f" Stock: {item_data['stock']}\n"
        inventory_str += f" Category: {item_data['category']}\n"
        inventory_str += f" Last Updated: {item_data['last_updated']}\n\n"
    return inventory_str

# Adding sample items to the inventory
add_item(inventory, "Laptop", 1200.00, 5, "Electronics")
add_item(inventory, "Mouse", 25.00, 20, "Electronics")
add_item(inventory, "Keyboard", 75.00, 15, "Electronics")
add_item(inventory, "T-Shirt", 15.00, 50, "Clothing")
add_item(inventory, "Jeans", 40.00, 8, "Clothing")

# Now you can call these functions and store the returned values in variables
added_item = add_item(inventory, "Shoes", 80.00, 10, "Footwear")
inventory_list = list_inventory(inventory)
updated_stock = update_stock(inventory, "Laptop", 3)
electronics = search_by_category(inventory, "Electronics")
low_stock_items = low_stock_alert(inventory, 5)
total_value = calculate_total_value(inventory)
full_inventory = display_inventory(inventory)