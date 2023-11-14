
#function to get a list of all the dest_id from all the boxes
def get_destinations(boxes_unsorted):
    destinations = []
    
    for box in boxes_unsorted:
        destinations.append(box['dest_id'])
    sorted_destinations = sorted(list(set(destinations)))
    return sorted_destinations

#function to get a list of all the order_id from all the boxes
def get_ordres(boxes_unsorted):
    ordres = []
    
    for box in boxes_unsorted:
        ordres.append(box['order_id'])
    sorted_ordres = sorted(list(set(ordres)))
    return sorted_ordres

# function to distrebute the unsorted boxes on the pallets based on their dest_id 
def distribute_boxes_by_destination(boxes_unsorted) -> list[dict] :
     
    list_dest = get_destinations( boxes_unsorted )
    pallets_out = []

    weight = 0
    volume = 0.0

    for dest in list_dest:
        pallet_with_dest = []
        for box in boxes_unsorted:
           
           if box['dest_id'] == dest:
                weight += box['weight'] 
                volume += box['size'][0] * box['size'][1] * box['size'][2] 
                if weight <= 1000 and volume <= 1: 
                    pallet_with_dest.append(box)
                   
                else:
                    weight = 0
                    volume = 0
                    pallets_out.append(pallet_with_dest)
                    pallet_with_dest = []
                    pallet_with_dest.append(box)                   
        pallets_out.append(pallet_with_dest)
    
    return pallets_out
 
def validate_pallet_same_destination(boxes_unsorted,dest_id)->bool:
    #Sort the boxes on the different destinations
    pallets = distribute_boxes_by_destination( boxes_unsorted)
    #get a list of destinations
    list_dest = get_destinations( boxes_unsorted )
    #counter to check boxes in == boxes out
    total_boxes = 0
    
    
    if dest_id not in list_dest:
        return False
    
    #Make sure all the boxes in one pallet have same dest_id
    for index,pallet in enumerate(pallets):
        for box in pallet:
            total_boxes +=1
                
        if pallet[0]['dest_id'] == dest_id:
            for box in pallet:
                
                if box['dest_id'] != dest_id:
                    return False
        
        if not validate_weight(pallet):
            return False
        if not validate_volume(pallet):
            return False
    #Make sure we dont miss any boxes by Checking boxes out == boxes in
    if total_boxes != len(boxes_unsorted):
        return False      
    return True


# function to distrebute the unsorted boxes on the pallets based on their order_id
def distribute_boxes_by_ordrenr(boxes_unsorted) -> list[dict] :
     
    list_ordre = get_ordres( boxes_unsorted )
    pallets_out = []

    weight = 0
    volume = 0.0

    for order in list_ordre:
        pallet_with_order = []
        for box in boxes_unsorted:
           
           if box['order_id'] == order:
                weight += box['weight'] 
                volume += box['size'][0] * box['size'][1] * box['size'][2] 
                if weight <= 1000 and volume <= 1: 
                    pallet_with_order.append(box)
                   
                else:
                    weight = 0
                    volume = 0
                    pallets_out.append(pallet_with_order)
                    pallet_with_order = []
                    pallet_with_order.append(box)                   
        pallets_out.append(pallet_with_order)
    return pallets_out

def validate_pallet_same_order(boxes_unsorted,order_id)->bool:
    #Sort the boxes on the different pallets
    pallets = distribute_boxes_by_ordrenr( boxes_unsorted)
    #get a list of ordres
    list_ordres = get_ordres( boxes_unsorted )
    #counter to check boxes in == boxes out
    total_boxes = 0
    
    if order_id not in list_ordres:
        return False
    
    for index,pallet in enumerate(pallets):
        for box in pallet:
            total_boxes +=1
                
        if pallet[0]['order_id'] == order_id:
            for box in pallet:
                
                if box['order_id'] != order_id:
                    return False
        
        if not validate_weight(pallet):
            return False
        if not validate_volume(pallet):
            return False
        
    if total_boxes != len(boxes_unsorted):
        return False
    
    print("Number of boxes: ",total_boxes) 
       
    return True



# Calculate the weight of a pallet
def validate_weight(boxes_list)->bool:
    if len(boxes_list) == 0:
       return True
    
    total_weight = 0
# Check if the weight is less than 1 ton
    for box in boxes_list:
        total_weight += box['weight']
    return total_weight <= 1000
       


# Calculate the volume of a pallet
def validate_volume(boxes_list)->bool:
    if len(boxes_list) == 0:
       return True
    
    volume = 0
# Check if the volume is less than 1 cubic meter
    for box_index in boxes_list:
        volume += box_index['size'][0] * box_index['size'][1] * box_index['size'][2] 
    return volume <= 1.0

'''
I don't really understand this following condition
"Hvis det er muligt, vil de ogs ̊a gerne samle kasser med samme ordrenummer
pa den samme palle, men ikke hvis det betyder, at der skal sendes flere
paller afsted, end hvis de ikke var separeret mht. ordernummer"


So i did the following implementation where all the boxes with same 
order nr sorted in one pallet(pallet_order_dest), then I add other boxes 
 with different order_id but have same destination as one of the boxes to pallet_oneOrder.
   '''
def distribute_boxes_by_order_dest(unsorted_boxes)-> list[dict]:
   
    pallets_sorted_order = distribute_boxes_by_ordrenr(unsorted_boxes)
    pallets_out = []
    ton = 999
    cubic_meter= 0.9
    weight = 0
    volume = 0.0
    
    for pallet in pallets_sorted_order:
        pallet_order_dest = []
        # A list of box_id of the boxes in that specific pallet.
        list_boxesid = []
        for box in pallet:
            weight += box['weight'] 
            volume += box['size'][0] * box['size'][1] * box['size'][2]
            list_boxesid.append(box['box_id'])
            pallet_order_dest.append(box) 
        
        for box in pallet_order_dest:
            for unsorted_box in unsorted_boxes:
                if unsorted_box['box_id'] not in list_boxesid:
                    if unsorted_box['dest_id'] == box['dest_id']:                          
                        weight += unsorted_box['weight'] 
                        volume += unsorted_box['size'][0] * unsorted_box['size'][1] * unsorted_box['size'][2]
                        if  weight < ton and volume < cubic_meter:
                            pallet_order_dest.append(unsorted_box)
                            list_boxesid.append(unsorted_box['box_id'])
                        else:
                            weight -= unsorted_box['weight'] 
                            volume -= unsorted_box['size'][0] * unsorted_box['size'][1] * unsorted_box['size'][2]
        pallets_out.append(pallet_order_dest)
        weight = 0
        volume = 0

    for pallet in pallets_out:
        #print("\tPallet nr",pallet)
        for box in pallet:
            print("total boxes in that pallet",len(pallet))
            print(f"\tdest_id: {box['dest_id']} \torder_id: {box['order_id']}")
    return pallets_out