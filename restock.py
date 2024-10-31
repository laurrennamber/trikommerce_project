def restock_inventory(available_items, sold_units, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 
----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
## the first stocking begins on day 0
    #occurs every 7 days
## initial stock level is set to 2000 units (and may not exceed this value)

## MY COMMENTS
    # don't need to do for loop for 0-50 as the function itself is being called 49 times in simulation
    if current_day == 0:
        restock_needed = False

    elif (current_day % 7) == 0:
        restock_needed = True
    else:
        restock_needed = False
        
    total_sales = 2000 - available_items
    sales_for_day = total_sales - sold_units
    
    while restock_needed:
        restocked_units = 2000
        #running total of difference between 2000 items (total sales)
        
        # sold units needs to be updated in sales()
        inventory_records.append(current_day, sales_for_day, restocked_units, available_items)
        break

    while restock_needed == False:
        restocked_units = 0
        inventory_records.append(current_day, sales_for_day, restocked_units, available_items)
        break

    return available_items