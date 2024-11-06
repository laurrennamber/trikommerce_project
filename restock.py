def restock_inventory(available_items, sold_units, inventory_records, current_day):

## MY COMMENTS
    # don't need to do for loop for 0-50 as the function itself is being called 49 times in simulation
    ## the first stocking begins on day 0
    #occurs every 7 days
    ## initial stock level is set to 2000 units (and may not exceed this value)

    #checking whether restock is necessary
    if current_day == 0:
        restock_needed = True

    elif ((current_day % 7) == 0) and available_items != 2000 :
        restock_needed = True
    else:
        restock_needed = False
    #if true, work out difference between 2000 (max stock level) and items available to know how much stock is to be replenished
    if restock_needed:
        restocked_units = 2000 - available_items
        #running total of difference between 2000 items (total sales)
        # sold units will be updated in sales() after first day
        
        # TESTING ROW ISSUE:
        # inventory_records.append(current_day)
        # inventory_records.append(sold_units)
        # inventory_records.append(restocked_units)
        # inventory_records.append(available_items)
        # initializing list

        ## updating items available after restock (always 2000 but used this line for testing)
        available_items = available_items + restocked_units 

    ##if stock does not need to be replenished, restocked items must be 0
    elif restock_needed == False:
        restocked_units = 0


    ## use of sub list to update inventory records
    sub_list = [current_day, sold_units, restocked_units, available_items]
    inventory_records.append(sub_list)

    return available_items