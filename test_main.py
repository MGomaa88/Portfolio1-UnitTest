from main import *

# Create an empty list to store the dictionaries
boxes_list = []
# Creating empty dictionaries
box_dict1 = {}
box_dict2 = {}
box_dict3 = {}
'''
box_dict1['box_id'] = 15
box_dict1['order_id'] = 299
box_dict1['size'] = [0.5,0.1,0.3]
box_dict1['weight'] = 04.2
box_dict1['dest_id'] = 19
boxes_list.append(box_dict1)


box_dict2['box_id'] = 34
box_dict2['order_id'] = 313
box_dict2['size'] = [0.5,0.2,0.4]
box_dict2['weight'] = 01.2
box_dict2['dest_id'] = 19
boxes_list.append(box_dict2)

box_dict3['box_id'] = 103
box_dict3['order_id'] = 299
box_dict3['size'] = [0.5,0.9,0.5]
box_dict3['weight'] = 10.1
box_dict3['dest_id'] = 19
boxes_list.append(box_dict3)

'''
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

def test_destination():
    assert validate_destination(boxes_list,0,19) is True
    assert validate_destination(boxes_list,1,15) is True
    assert validate_destination(boxes_list,2,10) is False
    assert validate_destination(boxes_list,3,15) is True

def test_weight():
    assert validate_weight(boxes_list) is True


def test_order_id():
    assert validate_order_id(boxes_list,0,299) is True
    assert validate_order_id(boxes_list,1,313) is True
    assert validate_order_id(boxes_list,1,299) is False


def test_validate_pallet_same_destination():
    assert validate_pallet_same_destination(boxes_list,19) is True
    assert validate_pallet_same_destination(boxes_list,15) is True
    assert validate_pallet_same_destination(boxes_list, 10) is False


def test_validate_pallet_same_order():
    assert validate_pallet_same_order(boxes_list,313) is True
    assert validate_pallet_same_order(boxes_list,299) is True
    assert validate_pallet_same_order(boxes_list, 250) is False