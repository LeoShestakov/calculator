pairs = {
    ('liter', 'gallon') : 1 / 3.785,
    ('liter', 'pint'): 2.113,
    ('liter', 'quart'): 1.057,
    ('liter', 'cup'): 4.167,
    ('gallon', 'pint'): 8,
    ('gallon', 'quart'): 4,
    ('gallon', 'cup'): 15.773,
    ('pint', 'quart'): 0.5,
    ('pint', 'cup'): 1.972,
    ('quart', 'cup'): 3.943
}


def volume(choice):
    if((choice[1], choice[2]) in pairs.keys()):
        return choice[3] * pairs[(choice[1], choice[2])]
    else:
        return choice[3] / pairs[(choice[2], choice[1])]

