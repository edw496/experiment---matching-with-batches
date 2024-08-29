
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'follow_ups'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import itertools
    treatments = itertools.cycle([4]) #1, 2, 3,
    for player in subsession.get_players():
        player.treatment_type = next(treatments)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment_type = models.IntegerField()
    how_choice = models.LongStringField(label="Why did you arrange your list of preferred courses in this specific order?")
    advice = models.BooleanField(choices=[[True, 'Yes'], [False, 'No']],
                                 label="Did you follow the advice to arrange your list of preferred courses?",
                                 widget=widgets.RadioSelect,)
    # feedback = models.LongStringField(label="Do you have any feedback that can help us to improve this study?", blank=True)


# PAGES
class Followups(Page):
    form_model = 'player'
    form_fields = ['how_choice', 'advice']

    @staticmethod
    def get_form_fields(player):
        if player.treatment_type == 3:
            return ['how_choice', 'advice']
        elif player.treatment_type == 4:
            return ['how_choice', 'advice']
        else:
            return ['how_choice']


# class Feedback(Page):
#     form_model = 'player'
#     form_fields = ['feedback']


page_sequence = [Followups]
