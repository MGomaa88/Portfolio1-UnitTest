

# function to check a specific dest_id from list of boxes and check the weight
def distrebute_boxes(boxes_unsorted) -> list[dict] :
     
    list_dest = get_destinations( boxes_unsorted )
    pallets_out = []

    # counter to make sure that boxes in == boxes out
    total_boxes = 0
    print("Number of the unsorted boxes : ", len(boxes_unsorted))
    
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
                    print("pallet with dest: ", dest)
                    print("Weight = ", weight, "\t volume = ", volume)
                else:
                    weight = 0
                    volume = 0
                    pallets_out.append(pallet_with_dest)
                    pallet_with_dest = []
                    pallet_with_dest.append(box)
                    print("New pallet with dest: ", dest)

                total_boxes += 1
        pallets_out.append(pallet_with_dest)

    for idx , pallet in enumerate(pallets_out):
        print("pallet number: ", idx)
        for box in pallet:
            print("\t ",box," \t ")

    print("Number of the sorted boxes : ", total_boxes)
             
    return pallets_out
        
# function to validate a specific dest_id from list of boxes and validate the weight
def validate_pallet_same_order(boxes_list,order_id) -> bool:
    order_id_exists = False
    # This list/array is being used to save the boxes with same dest_id
    pallet_list = []
    # counter for how many boxes with same dest_id in the pallet
    total_boxes = 0

    for box_index in range(len( boxes_list)):
        if validate_order_id(boxes_list, box_index, order_id):
            order_id_exists = True
            pallet_list.append(boxes_list[box_index])
            total_boxes += 1
            print("Number of boxes in the pallet: ", total_boxes)
            print("box_index: ", box_index, "dest_id: ",
                  boxes_list[box_index]['dest_id'], 
                  " Order nr: ", boxes_list[box_index]['order_id'])
        
        elif validate_order_id(boxes_list,box_index,order_id) and total_boxes > 0 :
            order_id_exists = True
            
        elif not validate_order_id(boxes_list,box_index,order_id) and total_boxes ==0 :
            order_id_exists = False
    
    if not validate_weight(pallet_list):
        order_id_exists = False
       
    return order_id_exists



def make_pallet_for_destination(boxes_unsorted,dest_id):
    pallet = []
    for box in boxes_unsorted:
        if box['dest_id'] == dest_id:
            pallet.append(box)        
    if len(pallet) > 0:      
        return pallet

def get_destinations(boxes_unsorted):
    destinations = []
    
    for box in boxes_unsorted:
        destinations.append(box['dest_id'])
    unique_sorted_numbers = sorted(list(set(destinations)))
    return unique_sorted_numbers



def validate_order_id(boxes_list, box_index, order_id)->bool:
    return boxes_list[box_index]['order_id'] == order_id


# Calculate the weight of a pallet
def validate_weight(boxes_list)->bool:
    total_weight = 0

# Check if the weight is less than 1 ton
   
    for box in boxes_list:
        total_weight += box['weight']
    return total_weight <= 1000


# Calculate the volume of a pallet
def validate_volume(boxes_list)->bool:
    volume = 0
    
# Check if the volume is less than 1 cubic meter
    for box_index in boxes_list:
        volume += box_index['size'][0] * box_index['size'][1] * box_index['size'][2] 
    return volume <= 1.0



# Create an 2 empty list to store the dictionaries(boxes). One of these list weights under 1 ton. 
boxes_unsorted_over_ton = []
boxes_unsorted_under_ton = []

# Creating 5 empty dictionaries. One dictionary = One box
box_dict1 = {}
box_dict2 = {}
box_dict3 = {}
box_dict4 = {}
box_dict5 = {}


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



print("=========== Test with over ton=======\n")
distrebute_boxes(boxes_unsorted_over_ton)
print("=========== Test with under ton=======\n")
distrebute_boxes(boxes_unsorted_under_ton)
