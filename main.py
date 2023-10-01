
def validate_pallet_same_destination(boxes_list, dest_id) -> bool:
    pallet_list = []
    dest_id_exists = False
    total_boxes = 0
    if not validate_weight(boxes_list):
        return False
    for box_index,box in enumerate( boxes_list):
        if validate_destination(boxes_list, box_index, dest_id):
            dest_id_exists = True
            pallet_list.append(boxes_list[box_index])
            total_boxes = total_boxes + 1
            print("Number of pallet: ", total_boxes)
        elif box_index >= len(boxes_list) and total_boxes == 0:
            return False
    return dest_id_exists
        
    
def validate_pallet_same_order(boxes_list,order_id) -> bool:
    order_id_exists = False
    if not validate_weight(boxes_list):
        return False
    for box_index,box in enumerate( boxes_list):
        if validate_order_id(boxes_list, box_index, order_id):
            order_id_exists = True
        elif box_index >= len(boxes_list):
            return False
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







'''
def validate_destination(boxes_list, dest_id) -> bool:
    for box in boxes_list:
        if box.get('dest_id') == dest_id:
            return True
    return False
'''
'''
def validate_size(boxes_list)->bool:
    total_size = [0.0,0.0,0.0]
    for box_dictionary in boxes_list:
        size_list = box_dictionary.get('size',[0.0,0.0,0.0])
        total_size = [x +y for x,y in zip(total_size,size_list)]
        if (total_size >= [1.0,1.0,1.0]):
'''