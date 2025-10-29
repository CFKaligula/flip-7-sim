import random


class Deck:
    def __init__(self) -> None:
        self.cards: list[int] = self.make_cards()

    def make_cards(self):
        cards = []
        for i in range(12):
            iter_cards = [i] * i
            cards.extend(iter_cards)

        random.shuffle(cards)

        return cards

    def take_card(self):
        return self.cards.pop()


if __name__ == '__main__':
    deck = Deck()
    card = deck.take_card()
