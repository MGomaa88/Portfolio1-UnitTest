from boxes_dic import *


# Create an empty list to store the dictionaries
boxes_list = []
# Create 10 dictionaries to make test on them
for i in range(10):
    box_dict = {}  
    
    box_dict['box_id'] = i + 1  
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

''''
for box_dict in boxes_list:
    print("Box:")
    print(f"Box ID: {box_dict['box_id']}")
    print(f"Order ID: {box_dict['order_id']}")
    print(f"Size: {box_dict['size']}")
    print(f"Weight: {box_dict['weight']}")
    print(f"Destination ID: {box_dict['dest_id']}")
    print()
'''




def test_destination():
    assert validate_destination(boxes_list,1,19) is False
    assert validate_destination(boxes_list,1,15) is True
    assert validate_destination(boxes_list,4,19) is True

def test_weight():
    assert validate_weight(boxes_list) is True