import pytest
from main import *

def test_flush():
    is_flush = Hand(Card("A", "H"), Card("3", "H"), Card("T", "H"))
    not_flush = Hand(Card("A", "H"), Card("3", "H"), Card("T", "S"))
    
    assert is_flush.is_flush()
    assert not_flush.is_flush() == False


def test_straight():
    hand_1 = Hand(Card("A", "H"), Card("2", "H"), Card("3", "H"))
    hand_2 = Hand(Card("A", "H"), Card("3", "H"), Card("2", "S"))
    hand_3 = Hand(Card("A", "H"), Card("3", "H"), Card("2", "S"))
    hand_4 = Hand(Card("3", "H"), Card("5", "H"), Card("4", "S"))
    hand_5 = Hand(Card("A", "H"), Card("Q", "H"), Card("K", "S"))

    assert hand_1.is_straight()
    assert hand_2.is_straight()
    assert hand_3.is_straight()
    assert hand_4.is_straight()
    assert hand_5.is_straight()
    
def test_replacement():
    return True
    random_hand_repr_list = [
        [c.__repr__() for c in get_random_hand()]
        for i in range(10)
    ]


    assert list(random_hand_repr_list) == [3, 2, 1]