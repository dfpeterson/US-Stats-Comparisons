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
