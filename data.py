pairs = {
    ('MB', 'GB') : 1 / 1000,
    ('MB', 'KB') : 1000,
    ('MB', 'TB') : 10 ** -6,
    ('GB', 'KB') : 10 ** 6,
    ('GB', 'TB') : 1 / 1000,
    ('KB', 'TB') : 10 ** -9
}

def data(choice):
    if((choice[1], choice[2]) in pairs.keys()):
        return choice[3] * pairs[(choice[1], choice[2])]
    else:
        return choice[3] / pairs[(choice[2], choice[1])]