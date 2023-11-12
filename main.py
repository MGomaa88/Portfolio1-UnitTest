

# function to check a specific dest_id from list of boxes and check the weight
def distrebute_boxes(boxes_unsorted) -> list[dict] :
     
    list_dest = get_destinations( boxes_unsorted )
    pallets_out = []

    # counter to make sure that boxes in == boxes out
    total_boxes = 0  
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
                total_boxes += 1
        pallets_out.append(pallet_with_dest)
           
    return pallets_out
 
def validate_pallet_same_destination(boxes_unsorted,dest_id)->bool:

    pallets = distrebute_boxes( boxes_unsorted)
    list_dest = get_destinations( boxes_unsorted )
    if dest_id not in list_dest:
        return False
    

    for index,pallet in enumerate(pallets):
        if pallet[0]['dest_id'] == dest_id:
            for box in pallet:
                if box['dest_id'] != dest_id:
                  return False
        if not validate_weight(pallet):
            return False
        if not validate_volume(pallet):
            return False
    return True


def get_destinations(boxes_unsorted):
    destinations = []
    
    for box in boxes_unsorted:
        destinations.append(box['dest_id'])
    sorted_destinations = sorted(list(set(destinations)))
    return sorted_destinations

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

# Create an 2 empty list to store the dictionaries(boxes). One of these list weights under 1 ton. 
boxes_unsorted_over_ton = []
boxes_unsorted_under_ton = []

# Creating 5 empty dictionaries. One dictionary = One box
box_dict1 = {}
box_dict2 = {}
box_dict3 = {}
box_dict4 = {}
box_dict5 = {}
box_dict6 = {}


box_dict1['box_id'] = 15
box_dict1['order_id'] = 299
box_dict1['size'] = [0.5,0.1,0.3]
box_dict1['weight'] = 04.2
box_dict1['dest_id'] = 19
boxes_unsorted_over_ton.append(box_dict1)
boxes_unsorted_under_ton.append(box_dict1)


box_dict2['box_id'] = 34
box_dict2['order_id'] = 313
box_dict2['size'] = [0.5,0.2,0.4]
box_dict2['weight'] = 01.2
box_dict2['dest_id'] = 19
boxes_unsorted_over_ton.append(box_dict2)
boxes_unsorted_under_ton.append(box_dict2)

                                
box_dict3['box_id'] = 103
box_dict3['order_id'] = 299
box_dict3['size'] = [0.5,0.9,0.5]
box_dict3['weight'] = 10.1
box_dict3['dest_id'] = 15
boxes_unsorted_over_ton.append(box_dict3)
boxes_unsorted_under_ton.append(box_dict3)


box_dict4['box_id'] = 10
box_dict4['order_id'] = 313
box_dict4['size'] = [0.5,0.9,0.5]
box_dict4['weight'] = 999
box_dict4['dest_id'] = 19
boxes_unsorted_over_ton.append(box_dict4)
# Here we won't add box_dict4 to the boxes_unsorted_under_ton

box_dict5['box_id'] = 66
box_dict5['order_id'] = 299
box_dict5['size'] = [1,0.9,0.9]
box_dict5['weight'] = 10.1
box_dict5['dest_id'] = 15
boxes_unsorted_over_ton.append(box_dict5)
boxes_unsorted_under_ton.append(box_dict5)

box_dict6['box_id'] = 20
box_dict6['order_id'] = 250
box_dict6['size'] = [1,0.9,0.9]
box_dict6['weight'] = 10.1
box_dict6['dest_id'] = 652
boxes_unsorted_over_ton.append(box_dict6)
boxes_unsorted_under_ton.append(box_dict6)



print("=========== Test with over ton=======\n")
#validate_pallet_same_destination(distrebute_boxes(boxes_unsorted_over_ton),19)
#print("=========== Test with under ton=======\n")
#distrebute_boxes(boxes_unsorted_under_ton)
'''