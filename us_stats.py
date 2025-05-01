import pandas as pd
from math import ceil, floor, log
from datetime import datetime, timedelta

MAGNITUDES = ['units', 'thousand', 'million', 'billion', 'trillion',
              'quadrillion', 'quintillion', 'sextillion', 'septillion',
              'octillion', 'nonillion', 'decillion']

class USAStats:
    def __init__(self, recent_date=''):
        #? Can I change this into a payload with a property?
        #TODO: I should invoke this further down and use it once
        self._cpi_data = pd.read_csv('combined_cpi.csv')
        self._state_admissions = pd.read_csv('state_admissions.csv')
        self._us_population = pd.read_csv('us_population_by_year.csv')
        self._world_population = pd.read_csv('world_population.csv')
        #TODO: Flags, Maps and Presidents
        self.recent_date = recent_date if recent_date else f'{datetime.now():%Y-%m-%d}'

    def get_stats(self, date=''):
        date = date if date else self._recent_date
        return {'cpi': self._cpi_data.loc[self._cpi_data['Year and Month'] <= date].iloc[-1]['Adj CPI'],
                'us_population': self._us_population[self._us_population['Census year'] <= int(date[:4])].iloc[-1]['Population'],
                'world_population': self._world_population[self._world_population['year'] <= int(date[:4])].iloc[-1]['Population'],
                'state_admissions': self._state_admissions.loc[self._state_admissions['Clean Date'] <= date]}
    
    @property
    def recent_date(self):
        return self._recent_date
    
    @recent_date.setter
    def recent_date(self, value):
        self._recent_date = value

_data_sets = {'cpi_data': 'combined_cpi.csv',
        'state_admissions': 'state_admissions.csv',
        'us_population': 'us_population_by_year.csv',
        'world_population': 'world_population.csv'}

#? Is this going to work outside of this file?
_usa_stats = USAStats()

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
    
    def __mul__(self, amt):
        return self.delta * amt
    
    @property
    def delta(self):
        return self._cpi_delta
    
    @delta.setter
    def delta(self, value):
        self._cpi_delta = value[0] / value[1]

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
        return f'{self.us_pop/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude]}'
    
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
        return f'{self.world_pop/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude]}'


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

class StateAdmissions:
    def __init__(self, states_admittied):
        self._states_admitted = states_admittied
    
    def __str__(self):
        return f'State Admissions for the period: {self._states_admitted}'


class PeriodDelta:
    def __init__(self, first_date, second_date, first_cpi, second_cpi, first_us_pop, second_us_pop, first_world_pop, second_world_pop):
        self.first_date = first_date
        self.second_date = second_date
        self._cpi_delta = CPIDelta(first_cpi, second_cpi)
        self._us_pop_delta = USPopulationDelta(first_us_pop, second_us_pop)
        self._world_pop_delta = WorldPopulationDelta(first_world_pop, second_world_pop)

    def __str__(self):
        return f'Period Delta from {self.first_date} to {self.second_date}:\n{str(self.cpi_delta)}\n{str(self.us_pop_delta)}\n{str(self.world_pop_delta)}'
    
    @property
    def first_date(self):
        return self._first_date
    
    @first_date.setter
    def first_date(self, date):
        self._first_date = date

    @property
    def second_date(self):
        return self._second_date
    
    @second_date.setter
    def second_date(self, date):
        self._second_date = date

    @property
    def cpi_delta(self):
        return self._cpi_delta
    
    @property
    def us_pop_delta(self):
        return self._us_pop_delta

    @property
    def world_pop_delta(self):
        return self._world_pop_delta

class PeriodData:
    def __init__(self, date=''):
        #TODO: Refactor dates from string to datetime
        _usa_stats = USAStats()
        if date:
            date_stats = _usa_stats.get_stats(date)
            self.date = date
        else:
            date_stats = _usa_stats.get_stats()
            self.date = _usa_stats.recent_date
        self.cpi = date_stats['cpi']
        self.us_pop = date_stats['us_population']
        self.world_pop = date_stats['world_population']
        self.state_admissions = date_stats['state_admissions']
    
    def __str__(self):
        return f'{str(self.cpi)}\n{str(self.us_pop)}\n{str(self.world_pop)}'

    def __neg__(self):
        """
        Calculates the PeriodDelta for the object compared to the current date
        """
        second_stats = _usa_stats.get_stats()
        return PeriodDelta(self.date, self.recent_date, self.cpi, second_stats['cpi'], self.us_pop, second_stats['us_population'], self.world_pop, second_stats['world_population'])

    def __sub__(self, compare_date):
        """
        If the object is another date or PeriodData compares the statistics
        for a given date or other PeriodData instance and the date stored
        in the left side PeriodData. Returns a PeriodDelta.
        If the object is a time delta it adjusts the object the new data
        """
        if isinstance(compare_date, PeriodData):
            return PeriodDelta(self.date, compare_date.date, self.cpi, compare_date.cpi, self.us_pop, compare_date.us_pop, self.world_pop, compare_date.world_pop)
            #get and compare 
        elif isinstance(compare_date, timedelta):
            #this subtracts X interval from the object and sets the new properties 
            self.date = self.date - timedelta(compare_date)
            new_stats = _usa_stats.get_stats(self.date)
            self.cpi = new_stats['CPI']
            self.us_pop = new_stats['us_population']
            self.world_pop = new_stats['world_population']
            self.state_admissions = new_stats['state_admissions']
        elif isinstance(compare_date, str):
            if len(compare_date.strip()) == 10 and compare_date[4] in ('-', '/'):
                compare_stats = _usa_stats.get_stats(compare_date)
                return PeriodDelta(self.date, compare_date, self.cpi, compare_stats['CPI'], self.us_pop, compare_stats['us_population'], self.world_pop, compare_stats['world_population'])
            else:
                self.date = self.date - timedelta(compare_date)
                new_stats = _usa_stats.get_stats(self.date)
                self.cpi = new_stats['CPI']
                self.us_pop = new_stats['us_population']
                self.world_pop = new_stats['world_population']
                self.state_admissions = new_stats['state_admissions']

    def __add__(self, add_interval):
        """
        Advances the statistics by a given interval
        """
        self.date = self.date + timedelta(add_interval)
        new_stats = _usa_stats.get_stats(self._date)
        self.cpi = new_stats['CPI']
        self.us_pop = new_stats['us_population']
        self.world_pop = new_stats['world_population']
        self.state_admissions = new_stats['state_admissions']
    
    @property
    def stats(self):
        return self._stats
    
    @stats.setter
    def stats(self, stats):
        self._stats = stats

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        self._date = new_date
    
    @property
    def cpi(self):
        return self._cpi
    
    @cpi.setter
    def cpi(self, new_cpi):
        self._cpi = CPI(new_cpi)
    
    @property
    def us_pop(self):
        return self._us_population
    
    @us_pop.setter
    def us_pop(self, new_us_pop):
        self._us_population = USPopulation(new_us_pop)
    
    @property
    def world_pop(self):
        return self._world_population
    
    @world_pop.setter
    def world_pop(self, new_world_pop):
        self._world_population = WorldPopulation(new_world_pop)
    
    @property
    def recent_date(self):
        return _usa_stats.recent_date
    
    @property
    def state_admissions(self):
        return self._state_admissions

    @state_admissions.setter
    def state_admissions(self, new_state_admissions):
        self._state_admissions = new_state_admissions

if __name__ == '__main__':
    period_data = PeriodData('1871-03-18')
    print(str(period_data))
    print(str(PeriodData()))
    print(str(-period_data))