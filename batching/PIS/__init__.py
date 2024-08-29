
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'PIS'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    confirmation = models.BooleanField()


# PAGES

class PIS(Page):
    form_model = 'player'
    form_fields = ['confirmation']

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.confirmation is True:
            return upcoming_apps[0]


class Cancel(Page):
    pass


page_sequence = [PIS, Cancel]
