class Flag:
    def __init__(self, flag):
        self.stars = flag['number of stars']
        self.image = flag['file name']

    def __str__(self):
        return f'{self.stars}-Star Flag'
    
    @property
    def stars(self):
        return self._stars
    
    @stars.setter
    def stars(self, value):
        self._stars = value

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, value):
        self._image = value
