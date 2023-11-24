
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
 







       


'''
I don't really understand this following condition
"Hvis det er muligt, vil de ogs ̊a gerne samle kasser med samme ordrenummer
pa den samme palle, men ikke hvis det betyder, at der skal sendes flere
paller afsted, end hvis de ikke var separeret mht. ordernummer"


So i did the following implementation where all the boxes with same 
order nr sorted in one pallet(pallet_order_dest), then I add other boxes 
 with different order_id but have same destination as one of the boxes to pallet_oneOrder.
   
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
    return pallets_out


# Creating 6 empty dictionaries. One dictionary = One box
box_dict1 = {}
box_dict2 = {}
box_dict3 = {}
box_dict4 = {}
box_dict5 = {}
box_dict6 = {}
boxes_unsorted = []
#One weights under 1 ton.
boxes_unsorted_under_ton = []
#One has volume under 1^3 m.
boxes_unsorted_under_cubic = []

box_dict1['box_id'] = 15
box_dict1['order_id'] = 299
box_dict1['size'] = [0.5,0.1,0.3]
box_dict1['weight'] = 04.2
box_dict1['dest_id'] = 19
boxes_unsorted.append(box_dict1)
boxes_unsorted_under_ton.append(box_dict1)
boxes_unsorted_under_cubic.append(box_dict1)


box_dict2['box_id'] = 34
box_dict2['order_id'] = 313
box_dict2['size'] = [0.5,0.2,0.4]
box_dict2['weight'] = 01.2
box_dict2['dest_id'] = 19
boxes_unsorted.append(box_dict2)
boxes_unsorted_under_ton.append(box_dict2)

                                
box_dict3['box_id'] = 103
box_dict3['order_id'] = 299
box_dict3['size'] = [0.5,0.9,0.5]
box_dict3['weight'] = 10.1
box_dict3['dest_id'] = 15
boxes_unsorted.append(box_dict3)
boxes_unsorted_under_ton.append(box_dict3)


# NO add box_dict4 to the boxes_unsorted_under_ton, because we test weight function
box_dict4['box_id'] = 10
box_dict4['order_id'] = 313
box_dict4['size'] = [0.5,0.9,0.5]
box_dict4['weight'] = 999
box_dict4['dest_id'] = 19
boxes_unsorted.append(box_dict4)


box_dict5['box_id'] = 66
box_dict5['order_id'] = 299
box_dict5['size'] = [1,0.9,0.9]
box_dict5['weight'] = 10.1
box_dict5['dest_id'] = 15
boxes_unsorted.append(box_dict5)
boxes_unsorted_under_ton.append(box_dict5)

distribute_boxes_by_destination(boxes_unsorted)
'''