
# function to validate a specific dest_id from list of boxes and validate the weight as well
def validate_pallet_same_destination(boxes_list, dest_id) -> bool:
    # This list/array is being used to save the boxes with same dest_id
    pallet_list = []
    # flag to make sure that the specific dest_id exist
    dest_id_exists = False
    # counter for how many boxes with same dest_id in the pallet
    total_boxes = 0
   
    for box_index in range(len( boxes_list)):
        if validate_destination(boxes_list, box_index, dest_id):
            dest_id_exists = True
            pallet_list.append(boxes_list[box_index])
            total_boxes += 1
            print("Number of boxes in the pallet: ", total_boxes)
            print("box_index: ", box_index, "dest_id: ",boxes_list[box_index]['dest_id'])
        elif not validate_order_id(boxes_list,box_index,dest_id) and total_boxes ==0 :
            dest_id_exists = False
       
    #Here we make sure that the pallet is less than 1 ton
    if not validate_weight(pallet_list): 
        dest_id_exists = False
    
    return dest_id_exists
        
# function to validate a specific dest_id from list of boxes and validate the weight as well 
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
        elif not validate_order_id(boxes_list,box_index,order_id) and total_boxes ==0 :
            order_id_exists = False
    
    if not validate_weight(pallet_list):
        order_id_exists = False
       
    return order_id_exists


def validate_destination(boxes_list,box_index,dest_id)->bool:
    return boxes_list[box_index]['dest_id'] == dest_id


def validate_order_id(boxes_list, box_index, order_id)->bool:
    return boxes_list[box_index]['order_id'] == order_id

def validate_weight(boxes_list)->bool:
    weight = 0
    for box_index in boxes_list:
        weight += box_index['weight']
    return weight <= 1000


boxes_list = []
# Create 10 dictionaries to make test on them
for i in range(10):
    box_dict = {}  
    
    box_dict['box_id'] = i + 1  # start at index 3
    if (i%2 == 0):
        box_dict['order_id'] = 299  
        box_dict['dest_id'] = 19  
    else:
        box_dict['order_id'] = 313
        box_dict['dest_id'] = 15  
    
     # Adjust size
    size_value = [round(0.5, 2), round(0.1 + i * 0.1, 2), round(0.3 + i * 0.1, 2)]
    box_dict['size'] = size_value
    box_dict['weight'] = 0.4 + i * 1     
    
    # Add the dictionary to the list
    boxes_list.append(box_dict)


box_dict1 = {}

box_dict1['box_id'] = 15
box_dict1['order_id'] = 299
box_dict1['size'] = [0.5,0.1,0.3]
box_dict1['weight'] = 04.2
box_dict1['dest_id'] = 15
boxes_list.append(box_dict1)

print("=========== Test with dest_id 19=======\n")
validate_pallet_same_destination(boxes_list, 19)
print("=========== Test with dest_id 15=======\n")
validate_pallet_same_destination(boxes_list, 15)
print("=========== Test with dest_id 10=======\n")
validate_pallet_same_destination(boxes_list, 10)


print("=========== Test with order_id 313=======\n")
validate_pallet_same_order(boxes_list, 313)
print("=========== Test with order_id 299 =======\n")
validate_pallet_same_order(boxes_list, 299)
print("=========== Test with order_id 250=======\n")
validate_pallet_same_order(boxes_list, 250)