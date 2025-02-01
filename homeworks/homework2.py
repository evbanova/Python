def function_that_says_ni(*args, **kwargs):
    costs = 0
    unique_letters = set()

    for el in args:
        if type(el) == dict:
            for key, value in el.items():
                if key == 'name':
                    if value.lower() not in ('храст', 'shrub', 'bush'):
                        break
                if key == 'cost':
                    costs += round(value, 2)
    
    for key, value in kwargs.items():
        if type(value) == dict:
            for inner_key, inner_value in value.items():
                if inner_key == 'name':
                    if inner_value.lower() not in ('храст', 'shrub', 'bush'):
                        break
                if inner_key == 'cost':
                    costs += round(inner_value, 2)
            for letter in key:
                if letter not in unique_letters:
                    unique_letters.add(letter)

    letters_count = len(unique_letters)    

    if costs <= 42.00 and not int(costs) == 0:
        if not letters_count % int(costs):
            return '{:.2f}'.format(costs) + 'лв'

    return 'Ni!'
