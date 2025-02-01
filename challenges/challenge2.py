class HauntedMansion:
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        object.__setattr__(self, 'spooky_' + name, value)

    def __getattr__(self, name):
        return 'Booooo, only ghosts here!'

