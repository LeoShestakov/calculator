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
    print("CHOICES: " + str(units_dictionary.keys())[10:-1])
    print("--ENTER WITH NO QUOTES--")
    choice = input("Enter your unit: ")

ask_input()