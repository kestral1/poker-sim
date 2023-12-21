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
    # probabalistic test, might fail randomly
    SAMPLE_SIZE = 10_000
    random_hand_str_list = [
        [str(c) for c in get_random_hand().cards]
        for i in range(SAMPLE_SIZE)
    ]

    unique_count_hand_list = [len(set(h)) for h in random_hand_str_list]

    assert set(unique_count_hand_list) == set([3, 2, 1])