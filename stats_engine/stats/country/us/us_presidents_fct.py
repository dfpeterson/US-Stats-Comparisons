class President:
    def __init__(self, president):
        self.name = president[2]
        self.image = president[3]
        self.number = president[0]
        self.inauguration = president[1]

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
