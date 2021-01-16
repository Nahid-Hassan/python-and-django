txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are object in python']

# map(function, iterable)
# apply function to each elements in this iterable
# mark = map(function, list)
# mark = map(lambda x: ..., txt)

"""
lambda s: Here 's' is a variable
ternary operator: (True, s) if 'anonymous' in s else (False, s): "True if .... else False"
"""

# ternary operator example
# print(2 + 2 if 2 < 0 else 4 + 4)

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

# map simply return an iterable that's why we need to convert it a list
print(list(mark))

# output = [(True, 'lambda functions....'),
        #   (True, 'anonym ....'),
        #   (False, 'functions....')]
