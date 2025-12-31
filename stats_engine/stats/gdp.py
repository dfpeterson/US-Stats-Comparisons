from math import floor, log
from stats_engine.helpers import magnitude

class GDP:
    def __init__(self, gdp_date, country, total_gdp, per_capita_gdp,
                 currency_symbol='$', currency_code='USD',
                 currency_name='United States Dollars',
                 is_currency_preceding=True):
        self.total_gdp = total_gdp
        self.per_capita_gdp = per_capita_gdp
        self.country = country
        self.currency = currency_code
        self.currency_symbol = currency_symbol
        self.currency_name = currency_name
        self.is_currency_preceding = is_currency_preceding
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
        return f'{self.currency_symbol if self.is_currency_preceding else ""}{self.total_gdp/(1000**self.magnitude):,.1f}{self.currency_symbol if not self.is_currency_preceding else ""} {magnitude(self.total_gdp).title()}'
    
    @property
    def pretty_per_capita(self):
        return f'{self.currency_symbol if self.is_currency_preceding else ""}{self.per_capita_gdp/(1000**self.magnitude_per_capita):,.1f}{self.currency_symbol if not self.is_currency_preceding else ""} {magnitude(self.per_capita_gdp).title()}'

class GDPDelta:
    def __init__(self, first_gdp, second_gdp):
        self.first_total_gdp = first_gdp.total_gdp
        self.second_total_gdp = second_gdp.total_gdp
        self.first_per_capita_gdp = first_gdp.per_capita_gdp
        self.second_per_capita_gdp = second_gdp.per_capita_gdp
        self.country = first_gdp.country
        self.currency = first_gdp.currency
        self.first_gdp_date = first_gdp.gdp_date
        self.second_gdp_date = second_gdp.gdp_date
        self.currency_symbol = first_gdp.currency_symbol
        self.currency_name = first_gdp.currency_name
        self.is_currency_preceding = first_gdp.is_currency_preceding


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
        self._us_gdp_delta = value[0].us_gdp / value[1].us_gdp
        self._us_gdp_delta_per_capita = value[0].per_capita / value[1].per_capita

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