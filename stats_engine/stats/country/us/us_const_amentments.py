class Amendments:
    def __init__(self, amendments):
        self.amendments = amendments

    def __str__(self):
        return f'{self.amendments}'
    
    @property
    def amendments(self):
        return self._amendments
    
    @amendments.setter
    def amendments(self, value):
        self._amendments = value

    def __eq__(self, value):
        return self.amendments == value
    
    def __ne__(self, value):
        return self.amendments != value
    
    def __gt__(self, value):
        return self.amendments > value
    
    def __ge__(self, value):
        return self.amendments >= value
    
    def __lt__(self, value):
        return self.amendments < value
    
    def __le__(self, value):
        return self.amendments <= value
