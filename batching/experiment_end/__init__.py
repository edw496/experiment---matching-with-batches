
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'experiment_end'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES


class End(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        participant.finished = True


page_sequence = [End]
