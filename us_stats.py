import pandas as pd
from math import ceil, floor, log
from datetime import datetime, timedelta

#? Is this nesting better or should I break out the classes?
#? If I break out the classes, how do I only load the data once?

MAGNITUDES = ['units', 'thousand', 'million', 'billion', 'trillion']

class USAStats:
    def __init__(self, recent_date=''):
        self._cpi_data = pd.read_csv('combined_cpi.csv')
        self._state_admissions = pd.read_csv('state_admissions.csv')
        self._us_population = pd.read_csv('us_population_by_year.csv')
        self._world_population = pd.read_csv('world_population.csv')
        #TODO: Flags, Maps and Presidents
        self._recent_date = recent_date if recent_date else f'{datetime.now():%Y-%m-%d}'

    def get_stats(self, date=''):
        date = date if date else self._recent_date
        return {'cpi': self._cpi_data.loc[self._cpi_data['Year and Month'] <= date].iloc[-1]['Adj CPI'],
                'us_population': self._us_population[self._us_population['Census year'] <= int(date[:4])].iloc[-1]['Population'],
                'world_population': self._world_population[self._world_population['year'] <= int(date[:4])].iloc[-1]['Population'],
                'state_admissions': self._state_admissions.loc[self._state_admissions['Clean Date'] <= date]}

class CPI:
    def __init__(self, cpi):
        self._cpi = cpi

    def __str__(self):
        return f'CPI for the period: {self._cpi:,.2f}'

class USPopulation:
    def __init__(self, us_population):
        self._us_population = us_population
        self._us_pop_magnitude = floor(log(us_population,1000))

    def __str__(self):
        return f'US Population for the period: {self._us_population/(1000**self._us_pop_magnitude):,.1f} {MAGNITUDES[self._us_pop_magnitude]}'

class WorldPopulation:
    def __init__(self, world_population):
        self._world_population = world_population
        self._world_pop_magnitude = floor(log(world_population,1000))

    def __str__(self):
        return f'World Population for the period: {self._world_population/(1000**self._world_pop_magnitude):,.1f} {MAGNITUDES[self._world_pop_magnitude]}'

class StateAdmissions:
    def __init__(self, states_admittied):
        self._states_admitted = states_admittied
    
    def __str__(self):
        return f'State Admissions for the period: {self._states_admitted}'


class PeriodDelta:
    def __init__(self, first_date, second_date, cpi_delta, first_us_pop, us_pop_change, first_world_pop, world_pop_change):
        self._first_date = first_date
        self._second_date = second_date
        self._cpi_delta = cpi_delta
        self._first_us_pop = first_us_pop
        self._us_pop_change = us_pop_change
        self._first_world_pop = first_world_pop
        self._world_pop_change = world_pop_change

class PeriodData:
    def __init__(self, date=''):
        #Figure out if there is a positional assignment from dictionary
        self._stats = USAStats()
        if date:
            date_stats = self._stats.get_stats(date)
        else:
            date_stats = self._stats.get_stats()
        self._cpi = CPI(date_stats['cpi'])
        self._us_population = USPopulation(date_stats['us_population'])
        self._world_population = WorldPopulation(date_stats['world_population'])
        self._state_admissions = StateAdmissions(date_stats['state_admissions'])
    
    def __str__(self):
        return str(self._cpi) + '\n' + str(self._us_population) + '\n' + str(self._world_population)

    def __neg__(self):
        """
        Calculates the PeriodDelta for the object compared to the current date
        """
        pass

    def __sub__(str, compare_date):
        """
        If the object is another date or PeriodData compares the statistics
        for a given date or other PeriodData instance and the date stored
        in the left side PeriodData. Returns a PeriodDelta.
        If the object is a time delta it adjusts the object the new data
        """
        if isinstance(compare_date, str):
            return 
            # get and compare all of the stats for that date
        elif isinstance(compare_date, PeriodData):
            return
            #get and compare 
        elif isinstance(compare_date, timedelta):
            return

    def __add__(str, add_interval):
        """
        Advances the statistics by a given interval
        """
        pass
    

if __name__ == '__main__':
    period_data = PeriodData('1871-03-18')
    print(str(period_data))