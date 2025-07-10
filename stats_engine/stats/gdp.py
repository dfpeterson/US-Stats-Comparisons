from math import floor, log
from stats_engine.helpers import MAGNITUDES

class GDP:
    def __init__(self, gdp_date, country, currency, total_gdp, per_capita_gdp):
        self.total_gdp = total_gdp
        self.per_capita_gdp = per_capita_gdp
        self.country = country
        self.currency = currency
        self.gdp_date = gdp_date

    def __str__(self):
        return f'{self.country} GDP for the period: {self.pretty}\nPer Capita: {self.pretty_per_capita}'

    @property
    def total_gdp(self):
        return self._total_gdp
    
    @total_gdp.setter
    def total_gdp(self, value):
        self._total_gdp = value

    @property
    def per_capita_gdp(self):
        return self._per_capita_gdp
    
    @per_capita_gdp.setter
    def per_capita_gdp(self, value):
        self._per_capita_gdp = value

    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        self._country = value
    
    @property
    def currency(self):
        return self._currency
    
    @currency.setter
    def currency(self, value):
        self._currency = value

    @property
    def gdp_date(self):
        return self._gdp_date
    
    @gdp_date.setter
    def gdp_date(self, value):
        self._gdp_date = value

    @property
    def magnitude(self):
        return floor(log(self.total_gdp,1000))
    
    @property
    def magnitude_per_capita(self):
        return floor(log(self.per_capita_gdp,1000))

    @property
    def pretty(self):
        return f'{self.us_gdp/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude].title()}'
    
    @property
    def pretty_per_capita(self):
        return f'{self.per_capita_gdp/(1000**self.magnitude_per_capita):,.1f} {MAGNITUDES[self.magnitude_per_capita].title()}'

class GDPDelta:
    def __init__(self, first_total_gdp, second_total_gdp, first_per_capita_gdp, second_per_capita_gdp
                 , country, currency, first_gdp_date, second_gdp_date):
        self.first_total_gdp = first_total_gdp
        self.second_total_gdp = second_total_gdp
        self.first_per_capita_gdp = first_per_capita_gdp
        self.second_per_capita_gdp = second_per_capita_gdp
        self.country = country
        self.currency = currency
        self.first_gdp_date = first_gdp_date
        self.second_gdp_date = second_gdp_date

    def __str__(self):
        return f'{self.country} GDP Delta for the period: {self.delta:.1%}\nPer Capita: {self.delta_per_capita:.1%}'
    
    @property
    def delta(self):
        return self.first_total_gdp / self.second_total_gdp
    
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

#TODO: Make generic and not country specific
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
