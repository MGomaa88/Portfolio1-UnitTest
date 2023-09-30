
# Create an empty list to store the dictionaries
boxes_list = []

# Creating empty dictionaries
box_dict1 = {}
box_dict2 = {}
box_dict3 = {}

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


# Create another 10 extra dictionaries to the list
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


for box_dict in boxes_list:
    print("Box:")
    print(f"Box ID: {box_dict['box_id']}")
    print(f"Order ID: {box_dict['order_id']}")
    print(f"Size: {box_dict['size']}")
    print(f"Weight: {box_dict['weight']}")
    print(f"Destination ID: {box_dict['dest_id']}")
    print()


def validate_destination(box_id,dest_id)->bool:
    return boxes_list[box_id]['dest_id'] == dest_id

