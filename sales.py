import random

def daily_sales(available_items, sold_units, inventory_records, current_day, restocked_units):

   # CODE FROM W3 SCHOOLS:
   #import random
   #print(random.randrange(1,10))
   ########################################
   #CODE FROM STACK OVERFLOW (NOT IMPLEMENTED HOWEVER HELPED MY CODE TESTING)
    #inventory_records.remove(current_day)
    #inventory_records.remove(available_items)
    ########################################
    #CODE FROM GEEKFORGEEKS
    #(Specifically the syntax for indexing a list of lists)
    #inventory_records[position_of_subset][1] = sold_units
    #inventory_records[position_of_subset][3] = available_items

    ## generating random number on sales days, on restock days sales = 0
    import random
    if ((current_day % 7) == 0) or current_day == 0:
        sold_units = 0
    else:
        sold_units =  random.randrange(0,201) ### random number between 0 and 200 (inclusive)
        
    #updating items available
    available_items = available_items - sold_units
    #used sublist to make indexing easier
    subset = [current_day, sold_units, restocked_units, available_items]
    #this variable was used to differentiate and make code more readable
    position_of_subset = int(current_day)
    # updating these two variables using indexing
    inventory_records[position_of_subset][1] = sold_units
    inventory_records[position_of_subset][3] = available_items
     
    return available_items