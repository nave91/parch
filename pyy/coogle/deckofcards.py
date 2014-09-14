class Deck:
    color = ["R","B"]

    def __init__(self):
        self.cards = []
        
    def __len__(self):
        return len(self.cards)
        
    def __contains__(self,card):
        return card in self.cards

    def checkcard(self,card):
        first = (card[0] in color)
        second = (card[1] in ["0","1"])
        third = (card[2] in [str(i) for i in range(2,10)])
        return first and second and third

    def insert(self,loc,card):
        if self.checkcard(card):
            self.cards.insert(loc,card)


    def shuffle(self):
        import random
        random.shuffle(self.cards)
        print self


    def __repr__(self):
        s = ""
        for i in self.items: s+=str(i)
        return s        


import random 

card = random.choice(["R","B"])+random.choice(["0","1"])+random.choice([str(i) for i in range(2,10)])

print card
