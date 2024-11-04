import random

def daily_sales(available_items, sold_units, inventory_records, current_day):
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


    import random
    sold_units =  random.randrange(0,2000) ### check this range


    available_items = available_items - sold_units


   ## don't need to update current day?
   ## don't need to update inventory records as this is current not past?
   #inventory_records.update(available_items)
    
    return available_items