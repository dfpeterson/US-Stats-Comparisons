from math import floor, log
from stats_engine.helpers import MAGNITUDES

#TODO: check for and remove "US"
class Population:
    def __init__(self, population, country, currency, pop_date):
        self.population = population
        self.country = country
        self.currency = currency
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
    def currency(self):
        return self._currency
    
    @currency.setter
    def currency(self, value):
        self._currency = value

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
    def __init__(self, first_pop, second_pop, country, first_date, second_date):
        self.first_pop = first_pop
        self.second_pop = second_pop
        self.country = country
        self.first_date = first_date
        self.second_date = second_date

    def __str__(self):
        return f'US Population Delta for the period: {self.delta:.1%}'

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



#TODO: Make generic and not country specific
class USPopulation:
    def __init__(self, us_population):
        self.us_pop = us_population

    def __str__(self):
        return f'US Population for the period: {self.pretty}'
    
    def __truediv__(self, amt):
        return self.us_pop / amt

    @property
    def us_pop(self):
        return self._us_population
    
    @us_pop.setter
    def us_pop(self, value):
        self._us_population = value

    @property
    def magnitude(self):
        return floor(log(self._us_population,1000))
    
    @property
    def pretty(self):
        return f'{self.us_pop/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude].title()}'
    
class USPopulationDelta:
    def __init__(self, first_us_pop, second_us_pop):
        self.delta = (first_us_pop, second_us_pop)

    def __str__(self):
        return f'US Population Delta for the period: {self.delta:.1%}'
    @property
    def delta(self):
        return self._us_pop_delta

    @delta.setter
    def delta(self, value):
        self._us_pop_delta = value[0] / value[1]
    
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

class WorldPopulation:
    def __init__(self, world_population):
        self.world_pop = world_population

    def __str__(self):
        return f'World Population for the period: {self.pretty}'

    def __truediv__(self, amt):
        return self.world_pop / amt

    @property
    def world_pop(self):
        return self._world_population
    
    @world_pop.setter
    def world_pop(self, value):
        self._world_population = value
    
    @property
    def magnitude(self):
        return floor(log(self._world_population,1000))
    
    @property
    def pretty(self):
        return f'{self.world_pop/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude].title()}'

class WorldPopulationDelta:
    def __init__(self, first_world_pop, second_world_pop):
        self.delta = (first_world_pop, second_world_pop)

    def __str__(self):
        return f'World Population Delta for the period: {self.delta:.1%}'
    
    @property
    def delta(self):
        return self._world_pop_delta
    
    @delta.setter
    def delta(self, value):
        self._world_pop_delta = (value[0] / value[1])

    @property
    def delta_pcts(self):
        #TODO find better key names
        return {'base year': int(round(self.delta * 100)), 'until current year': int(round((1 - self.delta) * 100))}

    @property
    def waffle(self):
        return {
            'rows':5,
            'columns':20,
            'values':self.delta_pcts,
            'colors':['#424242', '#ababab'],
            'icons':['person'],
            'figsize':(5, 3)
        }
