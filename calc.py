units_dictionary = {}
units_dictionary['length'] = ['inch', 'foot', 'meter', 'centimeter']
units_dictionary['volume'] = ['liter', 'gallon', 'pint', 'quart', 'cup']
units_dictionary['time'] = ['second', 'minute', 'hour', 'day', 'week']
units_dictionary['temperature'] = ['kelvin', 'fahrenheit', 'celsius']
units_dictionary['mass'] = ['gram', 'pound', 'ounce']
units_dictionary['data'] = ['MB', 'GB', 'KB', 'TB']
units_dictionary['energy'] = ['joule', 'watt', 'BTU']
# units_dictionary['gravity']

def ask_input():
    choice = []

    print("CHOICES: " + str(units_dictionary.keys())[10:-1])
    print("--ENTER WITH NO QUOTES--")

    choice.append(input("Enter your Category: "))

    print("CHOICES: " + str(units_dictionary[choice[0]])[9:-1])
    choice.append(input("Enter Unit Your Converting To: "))

    choice.append(input(f"Converting from {choice[1]} to : "))
    choice.append(int(input(f"How many {choice[1]}: ")))
    return choice
ask_input()