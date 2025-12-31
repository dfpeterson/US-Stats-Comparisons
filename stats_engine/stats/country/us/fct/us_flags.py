from stats_engine.helpers import date_pretty

class Flag:
    def __init__(self, flag):
        self.date = flag['date']
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

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        self._date = value

    @property
    def pretty_date(self):
        return date_pretty(self.date)