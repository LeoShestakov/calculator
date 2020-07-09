pairs = {
    ('second', 'minute') : 1 / 60,
    ('second', 'hour') : 1 / 3600,
    ('second', 'day') : 1 / 86400,
    ('minute', 'hour') : 1 / 60,
    ('minute', 'day') : 1 / 1440,
    ('hour', 'day') : 1 / 24
}

def timecalc(choice):
    if((choice[1], choice[2]) in pairs.keys()):
        return choice[3] * pairs[(choice[1], choice[2])]
    else:
        return choice[3] / pairs[(choice[2], choice[1])]