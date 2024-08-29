
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Intro_0(Page):
    pass

class Intro_1(Page):
    pass

class Intro_2(Page):
    pass

class Intro_3(Page):
    pass


page_sequence = [Intro_0, Intro_1, Intro_2, Intro_3]
