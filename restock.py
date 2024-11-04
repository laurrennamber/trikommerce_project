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
    print("current inventory records: " , inventory_records)
    ## TESTING ROW ISSUE:
    ##inventory_records.clear()
    print("current inventory records: " , inventory_records)
## MY COMMENTS
    # don't need to do for loop for 0-50 as the function itself is being called 49 times in simulation
    if current_day == 0:
        restock_needed = False

    elif ((current_day % 7) == 0) and available_items != 2000 :
        restock_needed = True
    else:
        restock_needed = False
    ## if statements rather than while?
    if restock_needed:
        restocked_units = 2000
        #running total of difference between 2000 items (total sales)
        
        # sold units will be updated in sales() after first day
        #inventory_records.append(current_day, sold_units, restocked_units, available_items)
        inventory_records.append(current_day)
        inventory_records.append(sold_units)
        inventory_records.append(restocked_units)
        inventory_records.append(available_items)
        print("inventory records (true): ", inventory_records)
        #current_day = current_day + 1

    elif restock_needed == False:
        restocked_units = 0
        inventory_records.append(current_day)
        inventory_records.append(sold_units)
        inventory_records.append(restocked_units)
        inventory_records.append(available_items)
        print("inventory records (false): ", inventory_records)
        #current_day = current_day + 1

    return available_items