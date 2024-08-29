import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'experiment_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 6

    PREF_LIST = [
                [30, '40223 - LSS from 2023: 78.75 - Payoff: £0.40'],
                [13, '40411 - LSS from 2023: 83.00 - Payoff: £3.10'],
                [17, '40943 - LSS from 2023: 82.00 - Payoff: £2.30'],
                [29, '41507 - LSS from 2023: 79.00 - Payoff: £0.45'],
                [28, '42268 - LSS from 2023: 79.25 - Payoff: £0.50'],
                [19, '42867 - LSS from 2023: 81.50 - Payoff: £1.90'],
                [22, '43083 - LSS from 2023: 80.75 - Payoff: £1.30'],
                [18, '43185 - LSS from 2023: 81.75 - Payoff: £2.10'],
                [12, '43270 - LSS from 2023: 83.25 - Payoff: £3.30'],
                [9, '43513 - LSS from 2023: 84.00 - Payoff: £3.90'],
                [21, '43662 - LSS from 2023: 81.00 - Payoff: £1.50'],
                [6, '43968 - LSS from 2023: 84.75 - Payoff: £4.50'],
                [7, '43994 - LSS from 2023: 84.50 - Payoff: £4.30'],
                [5, '44045 - LSS from 2023: 85.00 - Payoff: £4.70'],
                [11, '44570 - LSS from 2023: 83.50 - Payoff: £3.50'],
                [16, '45082 - LSS from 2023: 82.25 - Payoff: £2.50'],
                [3, '45450 - LSS from 2023: 85.50 - Payoff: £5.10'],
                [10, '45468 - LSS from 2023: 83.75 - Payoff: £3.70'],
                [8, '45610 - LSS from 2023: 84.25 - Payoff: £4.10'],
                [14, '46703 - LSS from 2023: 82.75 - Payoff: £2.90'],
                [1, '46738 - LSS from 2023: 86.00 - Payoff: £5.50'],
                [2, '46830 - LSS from 2023: 85.75 - Payoff: £5.30'],
                [15, '47149 - LSS from 2023: 82.50 - Payoff: £2.70'],
                [26, '47295 - LSS from 2023: 79.75 - Payoff: £0.60 - Guaranteed Entry Course'],
                [4, '48297 - LSS from 2023: 85.25 - Payoff: £4.90'],
                [25, '49082 - LSS from 2023: 80.00 - Payoff: £0.70'],
                [23, '49739 - LSS from 2023: 80.50 - Payoff: £1.10'],
                [24, '49810 - LSS from 2023: 80.25 - Payoff: £0.90'],
                [27, '49970 - LSS from 2023: 79.50 - Payoff: £0.55'],
                [20, '49979 - LSS from 2023: 81.25 - Payoff: £1.70']]

    ACCEPT_RATE = [0.9, 0.16, 0.24, 0.9, 0.9, 0.28,
                   0.34, 0.26, 0.14, 0.09, 0.32, 0.06,
                   0.07, 0.05, 0.12, 0.22, 0.03, 0.1,
                   0.08, 0.18, 0.01, 0.02, 0.2, 1,
                   0.04, 0.4, 0.36, 0.38, 0.9, 0.3]

    PAYOFF_LIST = [cu(0.4), cu(3.1), cu(2.3), cu(0.45), cu(0.5), cu(1.9),
                   cu(1.3), cu(2.1), cu(3.3), cu(3.9), cu(1.5), cu(4.5),
                   cu(4.3), cu(4.7), cu(3.5), cu(2.5), cu(5.1), cu(3.7),
                   cu(4.1), cu(2.9), cu(5.5), cu(5.3), cu(2.7), cu(0.6),
                   cu(4.9), cu(0.7), cu(1.1), cu(0.9), cu(0.55), cu(1.7)]


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
    rank1 = models.IntegerField(label="First Preference")
    rank2 = models.IntegerField(label="Second Preference")
    rank3 = models.IntegerField(label="Third Preference")
    rank4 = models.IntegerField(label="Fourth Preference")
    rank5 = models.IntegerField(label="Fifth Preference")
    matched_course = models.StringField(initial='N/A')
    treatment_type = models.IntegerField()


def rank1_choices(player):
    player_in_previous_rounds = player.in_previous_rounds()
    prev_choices = [[p.rank1, p.rank2, p.rank3, p.rank4, p.rank5] for p in player_in_previous_rounds]
    flattened_prev_choices = sum(prev_choices, [])
    choices = [i for i in C.PREF_LIST if i[0] not in flattened_prev_choices]
    return choices


def rank2_choices(player):
    player_in_previous_rounds = player.in_previous_rounds()
    prev_choices = [[p.rank1, p.rank2, p.rank3, p.rank4, p.rank5] for p in player_in_previous_rounds]
    flattened_prev_choices = sum(prev_choices, [])
    choices = [i for i in C.PREF_LIST if i[0] not in flattened_prev_choices]
    return choices


def rank3_choices(player):
    player_in_previous_rounds = player.in_previous_rounds()
    prev_choices = [[p.rank1, p.rank2, p.rank3, p.rank4, p.rank5] for p in player_in_previous_rounds]
    flattened_prev_choices = sum(prev_choices, [])
    choices = [i for i in C.PREF_LIST if i[0] not in flattened_prev_choices]
    return choices


def rank4_choices(player):
    player_in_previous_rounds = player.in_previous_rounds()
    prev_choices = [[p.rank1, p.rank2, p.rank3, p.rank4, p.rank5] for p in player_in_previous_rounds]
    flattened_prev_choices = sum(prev_choices, [])
    choices = [i for i in C.PREF_LIST if i[0] not in flattened_prev_choices]
    return choices


def rank5_choices(player):
    player_in_previous_rounds = player.in_previous_rounds()
    prev_choices = [[p.rank1, p.rank2, p.rank3, p.rank4, p.rank5] for p in player_in_previous_rounds]
    flattened_prev_choices = sum(prev_choices, [])
    choices = [i for i in C.PREF_LIST if i[0] not in flattened_prev_choices]
    return choices


# FUNCTIONS
def sorting(player: Player):
    for rank in range(1, 6): #range(1,6) starts at 1 and ends at 5 (6 is the terminal number)
        for pref_index in range(30): #range(30) starts with 0 and ends at 29, where 0 is the 1st element and 29 is the 30th.
            if getattr(player, f"rank{rank}") == C.PREF_LIST[pref_index][0] and \
                    random.random() <= C.ACCEPT_RATE[pref_index]:
                player.payoff = C.PAYOFF_LIST[pref_index]
                player.matched_course = C.PREF_LIST[pref_index][1]
                return


class Selection(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4', 'rank5']

    @staticmethod
    def error_message(player: Player, values):
        choices = [values['rank1'], values['rank2'], values['rank3'], values['rank4'], values['rank5']]

        if len(set(choices)) != len(choices):
            return "You cannot choose the same item twice"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        sorting(player)


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        payoff = player.payoff
        matched_course = player.matched_course
        participant = player.participant
        participant.payoff = player.payoff
        return {
            "payoff": payoff,
            "matched_course": matched_course,
        }

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):

        if player.treatment_type == 1:
            return upcoming_apps[0]
        if player.treatment_type == 2 and player.payoff > 0:
            return upcoming_apps[0]
        if player.treatment_type == 3:
            return upcoming_apps[0]
        if player.treatment_type == 4 and player.payoff > 0:
            return upcoming_apps[0]


page_sequence = [Selection, Results]
