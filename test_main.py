from main import *


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




#Here we Validate the weight for each list.
#def test_weight():
 #   assert validate_weight(boxes_unsorted_over_ton) is False
  #  assert validate_weight(boxes_unsorted_under_ton) is True



def test_validate_pallet_same_destination():
    assert validate_pallet_same_destination(boxes_unsorted_over_ton,10) is False
    assert validate_pallet_same_destination(boxes_unsorted_over_ton,19) is True
    assert validate_pallet_same_destination(boxes_unsorted_over_ton,15) is True


 