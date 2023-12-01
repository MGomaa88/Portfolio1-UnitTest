from main import *

# Creating 5 empty dictionaries.
box_dict1 = {}
box_dict2 = {}
box_dict3 = {}
box_dict4 = {}
box_dict5 = {}

#the following 3 dictionaries for testing distribute_boxes_by_destination()
multi_dest_boxes_under_ton_cubic = []

box_dict1['box_id'] = 15
box_dict1['order_id'] = 299
box_dict1['size'] = [0.5,0.1,0.3]
box_dict1['weight'] = 04.2
box_dict1['dest_id'] = 19
multi_dest_boxes_under_ton_cubic.append(box_dict1)


box_dict2['box_id'] = 34
box_dict2['order_id'] = 313
box_dict2['size'] = [0.5,0.2,0.4]
box_dict2['weight'] = 01.2
box_dict2['dest_id'] = 19
multi_dest_boxes_under_ton_cubic.append(box_dict2)

                                
box_dict3['box_id'] = 103
box_dict3['order_id'] = 299
box_dict3['size'] = [0.5,0.2,0.5]
box_dict3['weight'] = 10.1
box_dict3['dest_id'] = 15
multi_dest_boxes_under_ton_cubic.append(box_dict3)


# The following list for testing weight 
#This box has weight over 1000 kg.
boxes_same_dest_but_over_ton= []
box_dict4['box_id'] = 10
box_dict4['order_id'] = 313
box_dict4['size'] = [0.5,0.3,0.5]
box_dict4['weight'] = 1000
box_dict4['dest_id'] = 19
boxes_same_dest_but_over_ton.append(box_dict4)

# The following list for testing volume 
#This box has volume over 1 m^3.
boxes_same_dest_but_over_cubic = []
box_dict5['box_id'] = 15
box_dict5['order_id'] = 299
box_dict5['size'] = [1.0,1.0,1.0]
box_dict5['weight'] = 04.2
box_dict5['dest_id'] = 19
boxes_same_dest_but_over_cubic.append(box_dict5)


def is_dest_id_in_boxlist(boxes_unsorted, dest_id)-> bool:
    return dest_id in get_ids(boxes_unsorted,'dest_id')
       

#Make sure we dont miss any boxes by Checking boxes out == boxes in
def check_boxes_out_equal_boxes_in(boxes_unsorted)->bool:
    #Sort the boxes on the different destinations
    pallets = distribute_boxes_by_destination( boxes_unsorted)
    total_boxes = 0

    for pallet in pallets:
        if len(pallet) == 0:
            return False
        for box in pallet:
            total_boxes +=1

    return total_boxes == len(boxes_unsorted)
       


# Check the weight and volume of a pallet
def check_weight(boxes_list)->bool:
    total_weight = 0
# Check if the weight is less than 1 ton
    for box in boxes_list:
        total_weight += box['weight']
    return total_weight < 1000

def check_volume(boxes_list)->bool:
    volume = 0
    # Check if the volume is less than 1 m^3
    for box in boxes_list:
        volume += box['size'][0] * box['size'][1] * box['size'][2]
    return volume < 1.0



def test_pallets_only_have_one_dest_id():
    for pallet in distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic):
        assert len(set([box['dest_id'] for box in pallet])) == 1


#Testing the weight.
def test_weight():
    for pallet in distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic):
        assert check_weight(pallet) is True

    for pallet in distribute_boxes_by_destination(boxes_same_dest_but_over_ton):
        assert check_weight(pallet) is False


#Testing the volume.
def test_volume():
    for pallet in distribute_boxes_by_destination(boxes_same_dest_but_over_cubic):
        assert check_volume(pallet) is False

    for pallet in distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic):
        assert check_volume(pallet) is True



#Testing that we not miss any boxes
def test_total_boxes_out():
    assert check_boxes_out_equal_boxes_in(multi_dest_boxes_under_ton_cubic) is True




#Testing get_ids function
def test_get_ids():

    #No box has dest_id = 10 in boxes_unsorted
    assert is_dest_id_in_boxlist(multi_dest_boxes_under_ton_cubic,10) is False

    #No box has dest_id = 0 in boxes_unsorted
    assert is_dest_id_in_boxlist(multi_dest_boxes_under_ton_cubic,0) is False

    # dect1 has a dest_id = 15  
    assert is_dest_id_in_boxlist(multi_dest_boxes_under_ton_cubic,15) is True

    # dect2 has a dest_id = 19 
    assert is_dest_id_in_boxlist(multi_dest_boxes_under_ton_cubic,19) is True




def test_distribute_boxes_by_destination():

    #All boxes with dest_id = 19 in a pallet. 
    assert check_distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic,19) is True

    #All boxes with dest_id = 15 in a pallet.   
    assert check_distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic,15) is True

    #The dest_id = 5, doesn't exist in the boxes_unsorted list.     
    assert check_distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic,5) is False






 