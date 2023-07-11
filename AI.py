
from random import choice

answers = [
    'ахахаха',
    'баян',
    'видел',
    'АХАХАХАХАХАХАХАХАХА',
    '...',
    'не смешно',
    ''
]


def generate_answer():
    return choice(answers)
