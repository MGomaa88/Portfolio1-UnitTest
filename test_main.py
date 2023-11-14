from main import *


# Create an 3 empty list to store the dictionaries(boxes). 
# One weights over 1 ton. 
boxes_unsorted_over_ton = []
#One weights under 1 ton.
boxes_unsorted_under_ton = []
#One has volume under 1^3 m.
boxes_unsorted_under_cubic = []
# Creating 6 empty dictionaries. One dictionary = One box
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
boxes_unsorted_under_cubic.append(box_dict1)


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


# NO add box_dict4 to the boxes_unsorted_under_ton, because we test weight function
box_dict4['box_id'] = 10
box_dict4['order_id'] = 313
box_dict4['size'] = [0.5,0.9,0.5]
box_dict4['weight'] = 999
box_dict4['dest_id'] = 19
boxes_unsorted_over_ton.append(box_dict4)


box_dict5['box_id'] = 66
box_dict5['order_id'] = 299
box_dict5['size'] = [1,0.9,0.9]
box_dict5['weight'] = 10.1
box_dict5['dest_id'] = 15
boxes_unsorted_over_ton.append(box_dict5)
boxes_unsorted_under_ton.append(box_dict5)


# This dic made for testing volume function
box_dict6['box_id'] = 15
box_dict6['order_id'] = 299
box_dict6['size'] = [0.2,0.5,0.4]
box_dict6['weight'] = 04.2
box_dict6['dest_id'] = 19
boxes_unsorted_under_cubic.append(box_dict6)



#Here we Validate the weight function.
def test_weight():
    assert validate_weight(boxes_unsorted_over_ton) is False
    assert validate_weight(boxes_unsorted_under_ton) is True


#Here we Validate the volume function.
def test_volume():
    assert validate_volume(boxes_unsorted_over_ton) is False
    assert validate_volume(boxes_unsorted_under_ton) is False
    assert validate_volume(boxes_unsorted_under_cubic) is True


def test_validate_pallet_same_destination():
    #No box has dest_id = 10
    assert validate_pallet_same_destination(boxes_unsorted_over_ton,10) is False
    #All boxes with dest_id = 19 in a pallet. The pallet is less than one ton and 1^3 m.
    assert validate_pallet_same_destination(boxes_unsorted_over_ton,19) is True
    #All boxes with dest_id = 15 in a pallet. The pallet is less than one ton and 1^3 m.  
    assert validate_pallet_same_destination(boxes_unsorted_over_ton,15) is True

def test_validate_pallet_same_order():
    #No boxes has order_id = 290
    assert validate_pallet_same_order(boxes_unsorted_over_ton,290) is False
    #All boxes with order_id = 299 in a pallet. The pallet is less than one ton and 1^3 m.
    assert validate_pallet_same_order(boxes_unsorted_over_ton,299) is True
    #All boxes with order_id = 313 in a pallet. The pallet is less than one ton and 1^3 m.
    assert validate_pallet_same_order(boxes_unsorted_over_ton,313) is True




 