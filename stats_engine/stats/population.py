from math import floor, log
from stats_engine.helpers import MAGNITUDES

#TODO: check for and remove "US"
class Population:
    def __init__(self, pop_date, population, country):
        self.population = population
        self.country = country
        self.pop_date = pop_date
    
    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, value):
        self._population = value

    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        self._country = value

    @property
    def pop_date(self):
        return self._pop_date
    
    @pop_date.setter
    def pop_date(self, value):
        self._pop_date = value

    @property
    def magnitude(self):
        return floor(log(self._population,1000))
    
    @property
    def pretty(self):
        return f'{self.population/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude].title()}'
    
class PopulationDelta:
    def __init__(self, first_pop, second_pop):
        self.first_pop = first_pop.population
        self.second_pop = second_pop.population
        self.country = first_pop.country
        self.first_date = first_pop.pop_date
        self.second_date = second_pop.pop_date

    def __str__(self):
        return f'{self.country} Population Delta for the period: {self.delta:.1%}'

    @property
    def first_pop(self):
        return self._first_pop
    
    @first_pop.setter
    def first_pop(self, value):
        self._first_pop = value

    @property
    def second_pop(self):
        return self._second_pop
    
    @second_pop.setter
    def second_pop(self, value):
        self._second_pop = value

    @property
    def delta(self):
        return self.first_pop / self.second_pop

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
    def first_date(self):
        return self._first_date
    
    @first_date.setter
    def first_date(self, value):
        self._first_date = value

    @property
    def second_date(self):
        return self._second_date
    
    @second_date.setter
    def second_date(self, value):
        self._second_date = value


    @property
    def delta_pcts(self):
        #TODO find better key names
        return {'base year': int(round(self.delta * 100)), 'until current year': int(round((1 - self.delta) * 100))}

    @property
    def waffle(self):
        #adjust size of icons or make flexible
        return {
            'rows':5,
            'columns':20,
            'values':self.delta_pcts,
            'colors':['#424242', '#ababab'],
            'icons':['person','person'],
            'figsize':(5, 3)
        }