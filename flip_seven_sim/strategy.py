import re
from abc import abstractmethod
from random import choice


def add_spaces_before_caps(text):
    """Adds a space before any capital letter in a string."""
    # Pattern: '([A-Z])' captures a single capital letter (A-Z).
    # Replacement: ' r'\1' inserts a space followed by the captured letter.
    return re.sub(r'([A-Z])', r' \1', text).lstrip()


class Strategy:
    def __str__(self) -> str:
        return add_spaces_before_caps(f'{type(self)}'.rsplit('.', 1)[1])[:-2]

    @staticmethod
    @abstractmethod
    def decide_give(held_cards: list[int]) -> bool:
        raise NotImplementedError


class NeverGiveUp(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        return True


class AlwaysGiveUp(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        return False


class GiveUpAfterFive(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        return len(held_cards) < 5


class GiveUpAfterFour(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        return len(held_cards) < 4


class GiveUpAfterThree(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        return len(held_cards) < 3


class GiveUpAfterTwo(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        return len(held_cards) < 2


class NoHigh(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        for card in held_cards:
            if card > 10:
                return False

        return True


class NoMid(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        """
        Stop if we have any 10 or higher in our held cards
        """
        for card in held_cards:
            if card > 6:
                return False

        return True


class Random(Strategy):
    @staticmethod
    def decide_give(held_cards: list[int]) -> bool:
        return choice([True, False])
