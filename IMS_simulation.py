from restock import restock_inventory
from sales import daily_sales

def run_simulation(total_days, inventory_records):
    available_items = 2000
    sold_units = 0
    restocked_units = None
    for current_day in range(0, total_days):
        available_items = restock_inventory(available_items, sold_units, inventory_records, current_day)
        available_items = daily_sales(available_items, sold_units, inventory_records, current_day, restocked_units)