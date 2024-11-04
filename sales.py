import random

def daily_sales(available_items, sold_units, inventory_records, current_day, restocked_units):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
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

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
     ## generating sales
   ######################################
   # CODE FROM W3 SCHOOLS:
   #import random
   #print(random.randrange(1,10))
   ########################################
    #inventory_records.remove(current_day)
    #inventory_records.remove(available_items)

    #current_day = current_day + 1
    import random
    if ((current_day % 7) == 0):
        sold_units = 0
    elif current_day == 0:
        sold_units = 0   
    else:
        sold_units =  random.randrange(0,201) ### check this range
        


    available_items = available_items - sold_units
    subset = [current_day, sold_units, restocked_units, available_items]
    position_of_subset = int(current_day)
    inventory_records[position_of_subset][1] = sold_units
    #inventory_records.update(current_day, available_items)
    #current_day = current_day + 1
   ## don't need to update current day?
   ## don't need to update inventory records as this is current not past?
   #inventory_records.update(available_items)
    
    return available_items