def roll_call_dwarves(names):
    for index, name in enumerate(names, start=1):
        print(f"{index}. {name}")

def summon_captain_planet(names):
    return [(name.capitalize() + '!') for name in names]

def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(list):
    for word in list:
        if (word == "cheddar") or (word == "cheddar") or (word == "cheddar"):
            return word
    return None
