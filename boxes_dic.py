
def validate_destination(boxes_list,box_index,dest_id)->bool:
    return boxes_list[box_index]['dest_id'] == dest_id

def validate_weight(boxes_list)->bool:
    weight = 0
    for box_index in boxes_list:
        weight += box_index['weight']
    return weight <= 1000

'''
def validate_size(boxes_list)->bool:
    total_size = [0.0,0.0,0.0]
    for box_dictionary in boxes_list:
        size_list = box_dictionary.get('size',[0.0,0.0,0.0])
        total_size = [x +y for x,y in zip(total_size,size_list)]
        if (total_size >= [1.0,1.0,1.0]):
'''