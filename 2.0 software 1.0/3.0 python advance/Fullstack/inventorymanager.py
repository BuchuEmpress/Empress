import streamlit as st
import time

from sup.exercise_2.inventory_manager import (
    add_item,
    list_inventory,
    update_stock,
    search_by_category,
    format_currency,
    low_stock_alert,
    calculate_total_value,
    display_inventory
)


# Initialize inventory
if 'inventory' not in st.session_state:
    st.session_state.inventory = {}

# Your inventory functions here...
 
# Adding sample items to the inventory
if not st.session_state.inventory:
    add_item(st.session_state.inventory, "Laptop", 1200.00, 5, "Electronics")
    add_item(st.session_state.inventory, "Mouse", 25.00, 20, "Electronics")
    add_item(st.session_state.inventory, "Keyboard", 75.00, 15, "Electronics")
    add_item(st.session_state.inventory, "T-Shirt", 15.00, 50, "Clothing")
    add_item(st.session_state.inventory, "Jeans", 40.00, 8, "Clothing")

st.title("Inventory Manager")

# Display inventory list
with st.container(height=400, border=True):
    st.header("Inventory List")
    st.write(display_inventory(st.session_state.inventory))

with st.container(height=400, border=True):
    st.header("Manage Inventory")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Add New Item")
        item_name = st.text_input("Item Name", key="item_name")
        price = st.number_input("Price", key="price")
        stock = st.number_input("Stock", min_value=0, key="stock")
        category = st.text_input("Category", key="category")
        if st.button("Add Item"):
            result = add_item(st.session_state.inventory, item_name, price, stock, category)
            st.write(result)

    with col2:
        st.subheader("Update Stock")
        item_name_update = st.text_input("Item Name to Update", key="item_name_update")
        new_stock = st.number_input("New Stock", min_value=0, key="new_stock")
        if st.button("Update Stock"):
            result = update_stock(st.session_state.inventory, item_name_update, new_stock)
            st.write(result)

    with col3:
        st.subheader("Delete Item")
        item_name_delete = st.text_input("Item Name to Delete", key="item_name_delete")
        if st.button("Delete Item"):
            if item_name_delete in st.session_state.inventory:
                del st.session_state.inventory[item_name_delete]
                st.write(f"Item '{item_name_delete}' deleted successfully.")
            else:
                st.write(f"Error: Item '{item_name_delete}' not found.")

with st.container(height=400, border=True):
    st.header("Inventory Insights")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total Value")
        st.write(f"Total Value: {format_currency(calculate_total_value(st.session_state.inventory))}")

    with col2:
        st.subheader("Low Stock Items")
        st.write(display_inventory(low_stock_alert(st.session_state.inventory, 5)))

with st.container(height=400, border=True):
    st.header("Category Insights")
    st.subheader("Electronics Category")
    st.write(display_inventory(search_by_category(st.session_state.inventory, "Electronics")))