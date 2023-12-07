# Mainly practiced OOP
# Once you implemented the comparison system -> Use Python's built-in sort (timsort)
# A significantly faster input function
import sys

# Imports here
from collections import Counter

# Classes and functions here
class Card:
    # part 1 
    # card_rank = {'A':13,'K':12,'Q':11,'J':10,'T':9,\
    #              '9':8,'8':7,'7':6,'6':5,'5':4,'4':3,'3':2,'2':1}
    # part 2
    card_rank = {'A':13,'K':12,'Q':11,'T':9,\
                 '9':8,'8':7,'7':6,'6':5,'5':4,'4':3,'3':2,'2':1,'J':0}

    def __init__(self,value):
        self.value = value

    def __eq__(self,other):
        return Card.card_rank[self.value] == Card.card_rank[other.value]

    def __gt__(self,other):
        return Card.card_rank[self.value] > Card.card_rank[other.value]

    def __lt__(self,other):
        return Card.card_rank[self.value] < Card.card_rank[other.value]

    def __repr__(self):
        return self.value
    
    def __hash__(self):
        return hash(str(self))

class Hand:
    # A hand has 5 cards and 7 classes
    hand_rank = {'five':7,'four':6,'full':5,'three':4,'two':3,'one':2,'high':1}

    def get_rank(self,counts):
        if len(counts) == 1:
            return 'five'
        if len(counts) == 2 and (4 in counts.values()):
            return 'four'
        if len(counts) == 2 and (3 in counts.values()):
            return 'full'
        if 3 in counts.values():
            return 'three'
        if 2 in counts.values():
            if len(counts) == 3:
                return 'two'
            else:
                return 'one'
        return 'high'
    
    def get_counts(self,Cards):
        # Used mainly in part 2
        c = Counter(Cards)
        # print([x.value for x in c.keys()])
        if 'J' in [x.value for x in c.keys()]:
            if len(c) == 1:
                return c
            t = {k:v for k,v in c.items() if k.value != 'J'}
            k = max(t,key=t.get)
            j_v = c.pop(Card('J'))
            c[k] += j_v
        return c
    def __init__(self,Cards):
        self.Cards = Cards # -> Cards is a list of cards
        # self.__counts = Counter(Cards)
        self.__counts = self.get_counts(Cards)
        self.type = self.get_rank(self.__counts)
        self.power_level = Hand.hand_rank[self.type]

    def __repr__(self):
        return str(self.Cards)
    
    # def __eq__(self,other):
    #     if self.power_level == other.power_level:
    #         return self.power_level == other.power_level
    #     else:
    #         for i in range(5):
    #             if self.Cards[i] != other.Cards[i]:
    #                 return self.power_level == other.power_level
    #             else:
    #                 return True
            
    def __gt__(self,other):
        if self.power_level != other.power_level:
            return self.power_level > other.power_level
        else:
            for i in range(5):
                if self.Cards[i] == other.Cards[i]:
                    continue
                else:
                    return self.Cards[i] > other.Cards[i]
    def __lt__(self,other):
        if self.power_level != other.power_level:
            return self.power_level < other.power_level
        else:
            for i in range(5):
                if self.Cards[i] == other.Cards[i]:
                    continue
                else:
                    return self.Cards[i] < other.Cards[i]
        
def solve():
    # n = "QQQQJ"
    # a = "2222Q"
    # n_h = Hand([Card(x) for x in n])
    # a_h = Hand([Card(x) for x in a])
    # print(n_h > a_h)
    n = sys.stdin.readlines()
    t = []
    out = 0
    for line in n:
        cards, value = line.strip().split()
        c = Hand([Card(x) for x in cards])
        t.append((c,int(value)))
    t.sort(key=lambda x: x[0])
    i = 1
    for x in t:
        out += x[1] * (i)
        i += 1
    # print(t)
    print(out)

def main():
    for _ in range(1):
        solve()


if __name__ == "__main__":
    # Declare any global variables here
    main()
