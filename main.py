
#This function returns a list of either dest_id or order_id
def get_ids(boxes_unsorted, type_id):
    ids = []
    
    for box in boxes_unsorted:
        ids.append(box[type_id])
          
    sorted_ids = sorted(list(set(ids)))
    return sorted_ids


# function to distrebute the unsorted boxes on the pallets based on their dest_id 
def distribute_boxes_by_destination(boxes_unsorted) -> list[dict] :
     
    list_dest = get_ids( boxes_unsorted, 'dest_id' )
    list_boxesid = []
    pallets_out = []

    weight_pallet = 0
    volume_pallet = 0.0
    

    for dest in list_dest:
        pallet_with_dest = []
        for box in boxes_unsorted:
            if box['box_id'] not in list_boxesid:
           
                if box['dest_id'] == dest:
                    weight_pallet += box['weight'] 
                    volume_pallet += box['size'][0] * box['size'][1] * box['size'][2] 
                    if weight_pallet < 1000 and volume_pallet < 1.0:
                        list_boxesid.append(box['box_id']) 
                        pallet_with_dest.append(box)
                    
                    else:
                        pallets_out.append(pallet_with_dest)
                        weight_pallet = 0
                        volume_pallet = 0
                        pallet_with_dest = []

                        weight_pallet += box['weight'] 
                        volume_pallet += box['size'][0] * box['size'][1] * box['size'][2] 
                        if weight_pallet < 1000 and volume_pallet < 1.0:
                            pallet_with_dest.append(box)
                            list_boxesid.append(box['box_id'])                   
        pallets_out.append(pallet_with_dest)
    
    return pallets_out