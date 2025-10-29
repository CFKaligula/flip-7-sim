import logbasic  # type: ignore

from flip_seven_sim.deck import Deck
from flip_seven_sim.player import Player
from flip_seven_sim.strategy import Strategy


class Simulation:
    def __init__(
        self,
        strategies: list[Strategy],
    ) -> None:
        self.players = self.create_players(strategies)

        self.score_board = {p.id: 0 for p in self.players}

    @property
    def non_stopped_players(self):
        return [player for player in self.players if not player.stopped]

    def create_players(self, strategies: list[Strategy]) -> list[Player]:
        return [Player(i, strategies[i]) for i in range(len(strategies))]

    def run(self, n_rounds: int = 20):
        logbasic.info(f'Simulating {n_rounds} rounds...')
        for round_no in range(n_rounds):
            deck = Deck()
            for player in self.players:
                player.reset_for_new_round()

            # first card
            for player in self.players:
                player.held_cards.append(deck.take_card())

            self.log_held_cards()

            while len(deck.cards) and len(self.non_stopped_players):
                for player in self.non_stopped_players:
                    player.play(deck)

            logbasic.debug(f'Round {round_no + 1} has ended!')
            self.calculate_scores()
        self.log_score_board()

    def calculate_scores(self):
        for player in self.players:
            score = sum(player.held_cards)
            self.score_board[player.id] += score

    def log_score_board(self):
        sorted_items_by_value = sorted(self.score_board.items(), key=lambda item: item[1], reverse=True)

        log_string = '\n************************Score Board************************'

        for player_id, score in sorted_items_by_value:
            player_strategy = [player.strategy for player in self.players if player.id == player_id][0]

            log_string += f'\n\tPlayer {player_id} ({player_strategy}): {score}'
        log_string += '\n**********************************************************'

        logbasic.success(log_string)

    def log_held_cards(self):
        log_string = '***Held Cards***'
        for player in self.players:
            log_string += f'\n\t\t Player {player.id} ({player.strategy}): {player.held_cards}'

        logbasic.debug(log_string)
