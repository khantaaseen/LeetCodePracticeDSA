class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        cards = Counter(deck)
        w = list(set(cards.values()))
        div = 0

        if len(w) == 1:
            div = w[0]
        else:
            div = gcd(w[0], w[1])

            for i in range(1, len(w)-1):
                div = gcd(div, w[i + 1])
        return div > 1

        # for card in deck:
        #     if deck[card] in cards:
        #         cards[card] = 1 + cards.get(deck[card], 0)
        #     else:
        #         cards[card] = 1
        
        # for i in cards:
        #     if cards[i] < 1:
        #         return False
        # return True