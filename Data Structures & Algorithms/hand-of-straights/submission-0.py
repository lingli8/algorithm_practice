class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for card in sorted(count.keys()):
            c = count[card]
            if c > 0:
                for i in range(groupSize):
                    target = card + i
                    if count[target] < c:
                        return False
                    count[target] -= c
        return True