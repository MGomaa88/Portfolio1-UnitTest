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

weight = 0

for box_index in boxes_list:
        weight += box_index['weight']
        if (weight > 10):
            print("Weight: ",weight)

def validate_destination(boxes_list,box_index,dest_id)->bool:
    return boxes_list[box_index]['dest_id'] == dest_id

def validate_weight(boxes_list)->bool:
    weight = 0
    for box_index in boxes_list:
        weight += box_index['weight']
        if weight > 999:
            return False
    return True


'''
def validate_size(boxes_list)->bool:
    total_size = [0.0,0.0,0.0]
    for box_dictionary in boxes_list:
        size_list = box_dictionary.get('size',[0.0,0.0,0.0])
        total_size = [x +y for x,y in zip(total_size,size_list)]
        if (total_size >= [1.0,1.0,1.0]):
'''