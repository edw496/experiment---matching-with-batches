from os import environ

SESSION_CONFIGS = [
    dict(
        name='experiment',
        display_name="experiment",
        app_sequence=['PIS', 'att_comp_checks', 'introduction', 'experiment_test', 'follow_ups', 'experiment_end'], #'PIS', 'att_comp_checks', 'introduction', 'experiment_test',
        num_demo_participants=100,
    ),
]
ROOMS = [
    dict(
        name='experiment',
        display_name='Experimental study'
    ),
]
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=1.50, doc=""
)

PARTICIPANT_FIELDS = ['finished']
SESSION_FIELDS = ['prolific_completion_url']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4396942923786'
