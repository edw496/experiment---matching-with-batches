
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'att_comp_checks'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    comprehension_1 = models.IntegerField(
        choices=[[1, 'Submit a preference list of university courses'],
                 [2, 'Answer questions about secondary school enrolments'],
                 [3, 'Nothing']],
        label="Based on the above paragraph, what will you be asked to do in this study?",
        widget=widgets.RadioSelect, )
    comprehension_2 = models.IntegerField(
        choices=[[1, 'A bonus monetary payment, regardless of which course offer'],
                 [2, 'A bonus monetary payment, depending to which course I am made an offer'],
                 [3, 'Nothing']],
        label="Based on the above paragraph, what kind of payment are you eligible for upon completion of this study?",
        widget=widgets.RadioSelect, )
    attention_1 = models.IntegerField(choices=[[1, 'Green'], [2, 'Purple'], [3, 'Yellow']],
        label="Based on the text you read above, what colour have you been asked to enter?",
        widget=widgets.RadioSelect,)
    attention_2 = models.IntegerField(choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Agree'], [4, 'Strongly Agree']],
        label="Please indicate your agreement with the following statement: 'I swim across the Pacific Ocean to get to work every day.'",
        widget=widgets.RadioSelectHorizontal, )

# PAGES

class Brief(Page):
    pass


class Comprehension_1(Page):
    form_model = 'player'
    form_fields = ['comprehension_1']

    # @staticmethod
    # def app_after_this_page(player: Player, upcoming_apps):
    #     if player.comprehension_1 != 1:
    #         return upcoming_apps[-1]


class Comprehension_2(Page):
    form_model = 'player'
    form_fields = ['comprehension_2']


class Attention_1(Page):
    form_model = 'player'
    form_fields = ['attention_1']


class Attention_2(Page):
    form_model = 'player'
    form_fields = ['attention_2']


page_sequence = [Brief, Comprehension_1, Comprehension_2, Attention_1, Attention_2]

