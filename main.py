from random import sample

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
SUITS = ["D", "C", "S", "H"]
RANK_TO_INT = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13,}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return self.rank + self.suit

    def __eq__(self, __value: object) -> bool:
        return (self.get_rank() == __value.get_rank()) and (self.get_suit() == __value.get_suit())

    def __hash__(self) -> int:
        return f"{self.get_rank()}{self.get_rank()}"

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_rank_int(self):
        return RANK_TO_INT[self.get_rank()]


CARDS = [
    Card(rank, suit)
    for rank in RANKS
    for suit in SUITS
]

class Hand:
    def __init__(self, *cards):
        assert len(cards) == 3
        self.cards = cards

    def __repr__(self):
        return ", ".join([str(c) for c in self.cards])

    def get_ranks(self):
        return [c.get_rank() for c in self.cards]

    def get_suits(self):
        return [c.get_suit() for c in self.cards]

    def is_flush(self):
        suits = self.get_suits()
        return len(set(suits)) == 1
    
    def is_straight(self):
        ranks_sorted = sorted([c.get_rank_int() for c in self.cards])
        if ranks_sorted == [1, 12, 13]:
            return True
        else:
            return (ranks_sorted[0] + 1 == ranks_sorted[1]) and (ranks_sorted[0] + 2 == ranks_sorted[2])
    
    def is_trips(self):
        ranks = [c.get_rank() for c in self.cards]
        return len(set(ranks)) == 1
    
    def is_straight_flush(self):
        return self.is_flush() and self.is_straight()
    
    def is_suited_trips(self):
        return self.is_flush() and self.is_trips()


def get_random_card() -> Card:
    return sample(CARDS, 1)[0]


def get_random_hand() -> Hand:
    card_list = [get_random_card() for i in range(3)]
    return Hand(*card_list)

def main():
    SAMPLE_SIZE = 100_000
    
    outcomes = {
        "Suited Trips": 0,
        "Straight Flush": 0,
        "Three of a kind": 0,
        "Straight": 0,
        "Flush": 0,
        "None": 0,
    }

    payouts = {
        "Suited Trips": 101,
        "Straight Flush": 41,
        "Three of a kind": 31,
        "Straight": 11,
        "Flush": 6,
        "None": 0,
    }

    incrament = SAMPLE_SIZE // 10
    
    for i in range(SAMPLE_SIZE):
        if (i % incrament) == 0:
            print(f"{round(100 * i/SAMPLE_SIZE)}%")
        
        hand = get_random_hand()

        if hand.is_suited_trips():
            outcomes["Suited Trips"] += 1
        elif hand.is_straight_flush():
            outcomes["Straight Flush"] += 1
        elif hand.is_trips():
            outcomes["Three of a kind"] += 1
        elif hand.is_straight():
            outcomes["Straight"] += 1
        elif hand.is_flush():
            outcomes["Flush"] += 1
        else:
            outcomes["None"] += 1
    assert sum([v for v in outcomes.values()]) == SAMPLE_SIZE
    sample_probabilities = {
        win_type: count/SAMPLE_SIZE
        for win_type, count in outcomes.items()
    }

    sample_winnings = {
        win_type: outcomes[win_type] * payouts[win_type]
        for win_type, prob in sample_probabilities.items()
    }

    print(
        *[
            (f"{win_type}: {count} out of {SAMPLE_SIZE}\n") + 
            (f"prob:\t=> {sample_probabilities[win_type]}\n") +
            (f"$ won:\t=> ${sample_winnings[win_type]}\n") + 
            "\n"
            for win_type, count in outcomes.items()
        ]
    )

    expected_win_per_hand = sum(sample_winnings.values()) / SAMPLE_SIZE
    print(f"Expected win / hand = ${expected_win_per_hand}")
    
if __name__ == "__main__":
    main()
