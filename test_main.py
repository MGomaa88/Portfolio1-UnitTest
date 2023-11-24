from main import *


boxes_unsorted = []

# Creating 5 empty dictionaries.
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
boxes_unsorted.append(box_dict1)


box_dict2['box_id'] = 34
box_dict2['order_id'] = 313
box_dict2['size'] = [0.5,0.2,0.4]
box_dict2['weight'] = 01.2
box_dict2['dest_id'] = 19
boxes_unsorted.append(box_dict2)

                                
box_dict3['box_id'] = 103
box_dict3['order_id'] = 299
box_dict3['size'] = [0.5,0.2,0.5]
box_dict3['weight'] = 10.1
box_dict3['dest_id'] = 15
boxes_unsorted.append(box_dict3)


# This dict made for testing weight 
#This box has weight over 1000 kg.
boxes_unsorted_over_ton= []
box_dict4['box_id'] = 10
box_dict4['order_id'] = 313
box_dict4['size'] = [0.5,0.3,0.5]
box_dict4['weight'] = 1000
box_dict4['dest_id'] = 19
boxes_unsorted_over_ton.append(box_dict4)


# This dict made for testing volume 
#This box has volume over 1 m^3.
boxes_unsorted_over_cubic = []
box_dict5['box_id'] = 15
box_dict5['order_id'] = 299
box_dict5['size'] = [1.2,1.5,0.9]
box_dict5['weight'] = 04.2
box_dict5['dest_id'] = 19
boxes_unsorted_over_cubic.append(box_dict5)


def check_get_ids(boxes_unsorted, dest_id)-> bool:
    if dest_id not in get_ids(boxes_unsorted,'dest_id'):
        return False
    return True

def check_distribute_boxes_by_destination(boxes_unsorted,dest_id)->bool:
    #Sort the boxes on the different destinations
    pallets = distribute_boxes_by_destination( boxes_unsorted)
    
    #Make sure all the boxes in one pallet have same dest_id
    for index,pallet in enumerate(pallets):
        if pallet[0]['dest_id'] == dest_id:
            for box in pallet:
                if box['dest_id'] != dest_id:
                    return False     
    return True


#Make sure we dont miss any boxes by Checking boxes out == boxes in
def check_total_boxes_out(boxes_unsorted)->bool:
    #Sort the boxes on the different destinations
    pallets = distribute_boxes_by_destination( boxes_unsorted)
    total_boxes = 0

    for pallet in pallets:
        if len(pallet) == 0:
            return False
        for box in pallet:
            total_boxes +=1

    if total_boxes != len(boxes_unsorted):
        return False 
    return True




# Check the weight and volume of a pallet
def check_weight(boxes_list)->bool:
    total_weight = 0
    
# Check if the weight is less than 1 ton
    for box in boxes_list:
        total_weight += box['weight']
    if total_weight >= 1000:
        return False
    return True

def check_volume(boxes_list)->bool:
    volume = 0
    # Check if the weight is less than 1 ton
    for box in boxes_list:
        volume += box['size'][0] * box['size'][1] * box['size'][2]
    if volume >= 1.0:
        return False
    return True



#Testing the weight.
def test_weight():
    assert check_weight(boxes_unsorted_over_ton) is False
    assert check_weight(boxes_unsorted) is True



#Testing the volume.
def test_volume():
    assert check_volume(boxes_unsorted_over_cubic) is False
    assert check_volume(boxes_unsorted) is True



#Testing that we not miss any boxes
def test_total_boxes_out():
    assert check_total_boxes_out(boxes_unsorted) is True




#Testing get_ids function
def test_get_ids():

    #No box has dest_id = 10 in boxes_unsorted
    assert check_get_ids(boxes_unsorted,10) is False

    #No box has dest_id = 0 in boxes_unsorted
    assert check_get_ids(boxes_unsorted,0) is False

    # dect1 has a dest_id = 15  
    assert check_get_ids(boxes_unsorted,15) is True

    # dect2 has a dest_id = 19 
    assert check_get_ids(boxes_unsorted,19) is True




def test_distribute_boxes_by_destination():

    #All boxes with dest_id = 19 in a pallet. 
    assert check_distribute_boxes_by_destination(boxes_unsorted,19) is True

    #All boxes with dest_id = 15 in a pallet.   
    assert check_distribute_boxes_by_destination(boxes_unsorted,15) is True






 