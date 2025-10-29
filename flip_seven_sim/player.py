import logbasic  # type: ignore

from flip_seven_sim.deck import Deck
from flip_seven_sim.strategy import Strategy


class Player:
    def __init__(self, id: int, strategy: Strategy):
        self.id = id
        self.strategy = strategy
        self.held_cards: list[int] = []
        self.stopped = False

    def reset_for_new_round(self) -> None:
        self.stopped = False
        self.held_cards = []

    def play(self, deck: Deck):
        if not self.stopped and self.strategy.decide_give(self.held_cards):
            new_card = deck.take_card()
            if new_card in self.held_cards:
                self.stopped = True
                self.held_cards = []
            else:
                self.held_cards.append(new_card)
        else:
            logbasic.debug(f'Player {self.id} has stopped')
            self.stopped = True
