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
        restocked_units = 2000 - available_items
        #running total of difference between 2000 items (total sales)
        
        # sold units will be updated in sales() after first day
        #inventory_records.append(current_day, sold_units, restocked_units, available_items)
        # TESTING ROW ISSUE:
        # inventory_records.append(current_day)
        # inventory_records.append(sold_units)
        # inventory_records.append(restocked_units)
        # inventory_records.append(available_items)
        # initializing list
        available_items = available_items + restocked_units 
        sub_list = [current_day, sold_units, restocked_units, available_items]
        inventory_records.append(sub_list)
        # res = []
        # for row in inventory_records:
 
        #     flag = True
 
        #     # checking for all elements in list
        #     for ele in sub_list:
        #         if ele not in row:
        #             flag = False
 
        #     if flag:
        #         res.append(row)
 
        # # printing result
        # print("Rows with list elements : " + str(res))
        print("inventory records (true): ", inventory_records)
        #current_day = current_day + 1

    elif restock_needed == False:
        restocked_units = 0
        # inventory_records.append(current_day)
        # inventory_records.append(sold_units)
        # inventory_records.append(restocked_units)
        # inventory_records.append(available_items)
        sub_list = [current_day, sold_units, restocked_units, available_items]
        inventory_records.append(sub_list)
        print("inventory records (false): ", inventory_records)
        #current_day = current_day + 1

    return available_items