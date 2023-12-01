from main import *

# Creating 3 empty dictionaries.
box_dict1 = {}
box_dict2 = {}
box_dict3 = {}


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




#Testing that we not miss any boxes
def test_total_boxes_out():

    total_boxes_in = len(multi_dest_boxes_under_ton_cubic)
    pallets = distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic)
    total_boxes_out = sum(len(pallet) for pallet in pallets)

    assert total_boxes_in == total_boxes_out




def test_pallets_only_have_one_dest_id():
    for pallet in distribute_boxes_by_destination(multi_dest_boxes_under_ton_cubic):
        assert len(set([box['dest_id'] for box in pallet])) == 1



#Testing get_ids function
def test_get_ids():

    dest_id_result = get_ids(multi_dest_boxes_under_ton_cubic,'dest_id')
    expected_dest_id_result = [15,19]
    assert dest_id_result == expected_dest_id_result

    
    order_id_result = get_ids(multi_dest_boxes_under_ton_cubic,'order_id')
    expected_order_id_result = [299,313]
    assert order_id_result == expected_order_id_result

    # Test when the input list is empty
    boxes = []
    result = get_ids(boxes, 'dest_id')
    expected_result = []
    assert result == expected_result



boxes = [
        {'box_id': 1, 'order_id': 313, 'dest_id': 1, 'weight': 200,  'size': (0.1, 0.2, 0.3)},
        {'box_id': 2, 'order_id': 299, 'dest_id': 1, 'weight': 300,  'size': (0.2, 0.2, 0.2)},
        {'box_id': 3, 'order_id': 299, 'dest_id': 2, 'weight': 500,  'size': (1.1, 2.1, 1.1)},
        {'box_id': 4, 'order_id': 313, 'dest_id': 2, 'weight': 1100, 'size': (0.1, 0.1, 0.1)},
    ]

pallets = distribute_boxes_by_destination(boxes)

def test_weight():
    for pallet in pallets:
        total_weight = sum(box['weight'] for box in pallet)
        assert total_weight < 1000

def test_volume():   
    for pallet in pallets:
        total_volume = sum(box['size'][0] * box['size'][1] * box['size'][2] for box in pallet)
        assert total_volume < 1.0




 