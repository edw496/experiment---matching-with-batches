import random

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 6
    PREF_LIST = [[1, '1 - LSS from 2023: 89.00 - Payoff: £4.25'], [2, '2 - LSS from 2023: 88.50 - Payoff: £4.05'],
                 [3, '3 - LSS from 2023: 88.00 - Payoff: £3.85'], [4, '4 - LSS from 2023: 87.50 - Payoff: £3.65'],
                 [5, '5 - LSS from 2023: 87.00 - Payoff: £3.45'], [6, '6 - LSS from 2023: 86.50 - Payoff: £3.25'],
                 [7, '7 - LSS from 2023: 86.00 - Payoff: £3.05'], [8, '8 - LSS from 2023: 85.50 - Payoff: £2.85'],
                 [9, '9 - LSS from 2023: 85.00 - Payoff: £2.65'], [10, '10 - LSS from 2023: 84.50 - Payoff: £2.45'],
                 [11, '11 - LSS from 2023: 84.00 - Payoff: £2.25'], [12, '12 - LSS from 2023: 83.50 - Payoff: £2.05'],
                 [13, '13 - LSS from 2023: 83.00 - Payoff: £1.85'], [14, '14 - LSS from 2023: 82.50 - Payoff: £1.65'],
                 [15, '15 - LSS from 2023: 82.00 - Payoff: £1.45'], [16, '16 - LSS from 2023: 81.50 - Payoff: £1.25'],
                 [17, '17 - LSS from 2023: 81.00 - Payoff: £1.05'], [18, '18 - LSS from 2023: 80.50 - Payoff: £0.85'],
                 [19, '19 - LSS from 2023: 80.00 - Payoff: £0.80'], [20, '20 - LSS from 2023: 79.50 - Payoff: £0.75'],
                 [21, '21 - LSS from 2023: 79.00 - Payoff: £0.70'], [22, '22 - LSS from 2023: 78.50 - Payoff: £0.65'],
                 [23, '23 - LSS from 2023: 78.00 - Payoff: £0.60'], [24, '24 - LSS from 2023: 77.50 - Payoff: £0.55 - Guaranteed Entry'],
                 [25, '25 - LSS from 2023: 77.00 - Payoff: £0.50'], [26, '26 - LSS from 2023: 76.50 - Payoff: £0.45'],
                 [27, '27 - LSS from 2023: 76.00 - Payoff: £0.40'], [28, '28 - LSS from 2023: 75.50 - Payoff: £0.35'],
                 [29, '29 - LSS from 2023: 75.00 - Payoff: £0.30'], [30, '30 - LSS from 2023: 74.50 - Payoff: £0.25']]

    ACCEPT_RATE = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1,
                   0.15, 0.2, 0.25, 0.30, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6,
                   0.65, 0.7, 0.75, 1, 0.85, 0.9, 0.95, 1, 1, 1]

    PAYOFF_LIST = [
        cu(4.25), cu(4.05), cu(3.85), cu(3.65), cu(3.45), cu(3.25), cu(3.05), cu(2.85), cu(2.65), cu(2.45),
        cu(2.25), cu(2.05), cu(1.85), cu(1.65), cu(1.45), cu(1.25), cu(1.05), cu(0.85), cu(0.80), cu(0.75),
        cu(0.70), cu(0.65), cu(0.60), cu(0.55), cu(0.5), cu(0.45), cu(0.4), cu(0.35), cu(0.3), cu(0.25)]


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import itertools

    treatments = itertools.cycle([1, 2])

    for player in subsession.get_players():
        player.treatment_type = next(treatments)


class Group(BaseGroup):
    pass


def make_rank_field(label):
    return models.IntegerField(choices=C.PREF_LIST, label=label, initial=0)


class Player(BasePlayer):
    rank1 = make_rank_field("First Preference")
    rank2 = make_rank_field("Second Preference")
    rank3 = make_rank_field("Third Preference")
    rank4 = make_rank_field("Fourth Preference")
    rank5 = make_rank_field("Fifth Preference")

    matched_course = models.StringField(initial='N/A')
    treatment_type = models.IntegerField()


# FUNCTIONS
def sorting(player: Player):
    for rank in range(1, 6):
        for pref_index in range(30):
            if getattr(player, f"rank{rank}") == C.PREF_LIST[pref_index][0] and \
                    random.random() <= C.ACCEPT_RATE[pref_index]:
                player.payoff = C.PAYOFF_LIST[pref_index]
                player.matched_course = C.PREF_LIST[pref_index][1]
                return


# PAGES
# class Introduction(Page):
#     timeout_seconds = 100


class Selection(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3', 'rank4', 'rank5']

    @staticmethod
    def error_message(player: Player, values):
        choices = [values['rank1'], values['rank2'], values['rank3'], values['rank4'], values['rank5']]
        player_in_previous_rounds = player.in_previous_rounds()
        prev_choices = [[p.rank1 for p in player_in_previous_rounds],
                        [p.rank2 for p in player_in_previous_rounds],
                        [p.rank3 for p in player_in_previous_rounds],
                        [p.rank4 for p in player_in_previous_rounds],
                        [p.rank5 for p in player_in_previous_rounds]]

        if len(set(choices)) != len(choices):
            return "You cannot choose the same item twice"

        if player.treatment_type == 2:
            for prev_choice in prev_choices:
                for choice in choices:
                    if choice in prev_choice:
                        return "You cannot choose previously chosen courses"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        sorting(player)

    @staticmethod
    def vars_for_template(player: Player):
        player_in_previous_rounds = player.in_previous_rounds()
        prev_choices = [[p.rank1 for p in player_in_previous_rounds],
                        [p.rank2 for p in player_in_previous_rounds],
                        [p.rank3 for p in player_in_previous_rounds],
                        [p.rank4 for p in player_in_previous_rounds],
                        [p.rank5 for p in player_in_previous_rounds]]

        # flattened_prev_choices = sum(prev_choices, [])
        # ordered_list = sorted(flattened_prev_choices)
        # new_list = [i for i in flattened_prev_choices:
        #     #print(i)
        #     chosen_courses = C.PREF_LIST[i-1][1]]
        #     print(chosen_courses)
        # # new_list.append(chosen)
        # new = ', '.join(str(item) for item in new_list)
        # return {
        #     "chosen_courses": new,
        # }

        flattened_prev_choices = sum(prev_choices, [])
        ordered_list = sorted(flattened_prev_choices)
        new = ', '.join(str(item) for item in ordered_list)
        return {
            "chosen_courses": new,
        }

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
        if player.treatment_type == 2 and player.payoff > 0:
            return upcoming_apps[-1]
        if player.treatment_type == 1:
            return upcoming_apps[-1]


page_sequence = [Selection, Results]
