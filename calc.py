import data
import custom_time
import volume

units_dictionary = {}
#units_dictionary['length'] = ['inch', 'foot', 'meter', 'centimeter']
units_dictionary['volume'] = ['liter', 'gallon', 'pint', 'quart', 'cup']
units_dictionary['time'] = ['second', 'minute', 'hour', 'day']
#units_dictionary['temperature'] = ['kelvin', 'fahrenheit', 'celsius']
#units_dictionary['mass'] = ['gram', 'pound', 'ounce']
units_dictionary['data'] = ['MB', 'GB', 'KB', 'TB']
#units_dictionary['energy'] = ['joule', 'watt', 'BTU']
# units_dictionary['gravity']

# Choice[Category, From Unit, To Unit, Value]
def ask_input():
    choice = []

    print("CHOICES: " + str(units_dictionary.keys())[10:-1])
    print("--ENTER WITH NO QUOTES--")

    choice.append(input("Enter your Category: "))

    print("CHOICES: " + str(units_dictionary[choice[0]]))
    choice.append(input("Enter Unit you're Converting from: "))

    choice.append(input(f"Converting from {choice[1]} to : "))
    choice.append(int(input(f"How many {choice[1]}: ")))
    print(f"{calc(choice)} {choice[2]}")

def calc(choice):
    category = choice[0]
    if category == "data":
        return data.data(choice)
    if category == "time":
        return custom_time.timecalc(choice)
    if category == "volume":
        return volume.volume(choice)
    else:
        print("ERROR")
        return


while(True):
    ask_input()


ask_input()