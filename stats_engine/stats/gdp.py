class USGDP:
    def __init__(self, us_gdp):
        self.us_gdp = us_gdp[1]
        self.per_capita = us_gdp[0]

    def __str__(self):
        return f'US GDP for the period: {self.pretty}\nPer Capita: {self.pretty_per_capita}'

    @property
    def us_gdp(self):
        return self._us_gdp
    
    @us_gdp.setter
    def us_gdp(self, value):
        self._us_gdp = value

    @property
    def per_capita(self):
        return self._per_capita
    
    @per_capita.setter
    def per_capita(self, value):
        self._per_capita = value

    @property
    def magnitude(self):
        return floor(log(self._us_gdp,1000))
    
    @property
    def magnitude_per_capita(self):
        return floor(log(self._per_capita,1000))

    @property
    def pretty(self):
        return f'{self.us_gdp/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude].title()}'
    
    @property
    def pretty_per_capita(self):
        return f'{self.per_capita/(1000**self.magnitude_per_capita):,.1f} {MAGNITUDES[self.magnitude_per_capita].title()}'

class USGDPDelta:
    def __init__(self, first_us_gdp, second_us_gdp):
        self.delta = (first_us_gdp, second_us_gdp)

    def __str__(self):
        return f'US GDP Delta for the period: {self.delta:.1%}\nPer Capita: {self.delta_per_capita:.1%}'
    
    @property
    def delta(self):
        return self._us_gdp_delta
    
    @property
    def delta_per_capita(self):
        return self._us_gdp_delta_per_capita

    @delta.setter
    def delta(self, value):
        self._us_gdp_delta = value[0].us_gdp / value[1][1]
        self._us_gdp_delta_per_capita = value[0].per_capita / value[1][0]

    @property
    def delta_pcts(self):
        #TODO find better key names
        return {'base year': int(round(self.delta * 100)), 'until current year': int(round((1 - self.delta) * 100))}

    @property
    def waffle(self):
        return {
            'rows':4,
            'columns':25,
            'starting_location':'SE',
            'values':self.delta_pcts,
            'colors':["#f5f54c", "#664f0e"],
            'icons':['$'],
            'figsize':(5, 3)
        }

class WorldGDP:
    def __init__(self, world_gdp):
        self.world_gdp = world_gdp[1]
        self.per_capita = world_gdp[0]

    def __str__(self):
        return f'World GDP for the period: {self.pretty}\nPer Capita: {self.pretty_per_capita}'
    
    @property
    def world_gdp(self):
        return self._world_gdp
    
    @world_gdp.setter
    def world_gdp(self, value):
        self._world_gdp = value

    @property
    def per_capita(self):
        return self._per_capita
    
    @per_capita.setter
    def per_capita(self, value):
        self._per_capita = value

    @property
    def magnitude(self):
        return floor(log(self._world_gdp,1000))
    
    @property
    def magnitude_per_capita(self):
        return floor(log(self._per_capita,1000))

    @property
    def pretty(self):
        return f'{self.world_gdp/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude].title()}'
    
    @property
    def pretty_per_capita(self):
        return f'{self.per_capita/(1000**self.magnitude_per_capita):,.1f} {MAGNITUDES[self.magnitude_per_capita].title()}'
    

class WorldGDPDelta:
    def __init__(self, first_world_gdp, second_world_gdp):
        self.delta = (first_world_gdp, second_world_gdp)

    def __str__(self):
        return f'World GDP Delta for the period: {self.delta:,.1%}\nPer Capita: {self.delta_per_capita:,.1%}'
    
    @property
    def delta(self):
        return self._world_gdp_delta

    @property
    def delta_per_capita(self):
        return self._world_gdp_delta_per_capita
    
    @delta.setter
    def delta(self, value):
        self._world_gdp_delta = value[0].world_gdp / value[1][1]
        self._world_gdp_delta_per_capita = value[0].per_capita / value[1][0]
    @property
    def delta_pcts(self):
        #TODO find better key names
        return {'base year': int(round(self.delta * 100)), 'until current year': int(round((1 - self.delta) * 100))}

    @property
    def waffle(self):
        return {
            'rows':4,
            'columns':25,
            'starting_location':'SE',
            'values':self.delta_pcts,
            'colors':["#f5f54c", "#664f0e"],
            'icons':['dollar','dollar'],
            'font_size':16,
            'figsize':(5, 3)
        }
