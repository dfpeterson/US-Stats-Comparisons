class President:
    def __init__(self, president):
        self.name = president['name']
        self.image = president['file']
        self.number = president['number']
        self.inauguration = president['inauguration date']
        self.term_start = ''
        self.term_number = 0
        self.party = 'None'

    def __str__(self):
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(self.number, 'th')
        return f'{self.name} the {self.number}{suffix} President'
    
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, value):
        self._image = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        self._number = value
    
    @property
    def inauguration(self):
        return self._inauguration
    
    @inauguration.setter
    def inauguration(self, value):
        self._inauguration = value

    @property
    def party(self):
        return self._party
    
    @party.setter
    def party(self, value):
        self._party = value

    @property
    def term_number(self):
        return self._term_number
    
    @term_number.setter
    def term_number(self, value):
        self._term_number = value

    @property
    def term_start(self):
        return self._term_start
    

    @term_start.setter
    def term_start(self, value):
        self._term_start = value

    def calc_days(self, calc_date):
        if calc_date and self.term_start and self.term:
            return f'{calc_date - self.term_start} days into his {self.term_number}{["st", "nd", "rd", "th"][self.term_number - 1]} term'
        else:
            return f'{self.term_number} term calc in progress'
        