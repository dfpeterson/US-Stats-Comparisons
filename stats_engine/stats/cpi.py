class CPI:
    def __init__(self, cpi):
        self.cpi = cpi

    def __str__(self):
        return f'CPI for the period: {self.cpi:,.2f}'
    
    def __truediv__(self, amt):
        return self.cpi / amt

    @property
    def cpi(self):
        return self._cpi
    
    @cpi.setter
    def cpi(self, value):
        self._cpi = value
    
class CPIDelta:
    def __init__(self, first_cpi, second_cpi):
        self.delta = (first_cpi, second_cpi)
    
    def __str__(self):
        return f'CPI Delta for the period: {self.delta:,.2f}'
    
    def __truediv__(self, amt):
        return self.delta / amt
    
    def __rtruediv__(self, amt):
        return amt / self.delta

    def __mul__(self, amt):
        return self.delta * amt

    def __rmul__(self, amt):
        return amt * self.delta
    
    @property
    def delta(self):
        return self._cpi_delta
    
    @delta.setter
    def delta(self, value):
        self._cpi_delta = value[0] / value[1]

    @property
    def delta_pcts(self):
        return {'base year': self._cpi_delta, 'until current year': 1-self._cpi_delta}

    @property
    def waffle(self):
        return {
            'rows':5,
            'columns':20,
            'values':self.delta_pcts,
            'vertical':True,
            'figsize':(5, 3)
            }
