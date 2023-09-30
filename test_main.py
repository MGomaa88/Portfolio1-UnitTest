from boxes_dic import *

def test_destination():
    assert validate_destination(1,19) is True
    assert validate_destination(1,15) is False
    assert validate_destination(4,15) is True
    