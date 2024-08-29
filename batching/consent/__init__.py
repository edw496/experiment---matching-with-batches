
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']],
        label="Have you read the PIS",
        widget=widgets.RadioSelect,)


# PAGES

class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.consent is False:
            return upcoming_apps[-1]


page_sequence = [Consent]
