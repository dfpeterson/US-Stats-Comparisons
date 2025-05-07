import pandas as pd
from math import ceil, floor, log
from datetime import date as datef
from dateutil.relativedelta import relativedelta

PEOPLE_BAR = [''.join([[ '🧍🏿', '🧍🏻', '🧍🏽', '🧍', '🧍🏾', '🧍🏼'][person%6] for person in range(k * 25, (k + 1) * 25)]) for k in range(4)]

MAGNITUDES = ['units', 'thousand', 'million', 'billion', 'trillion',
              'quadrillion', 'quintillion', 'sextillion', 'septillion',
              'octillion', 'nonillion', 'decillion']

def parse_interval(interval):
    intervals = {}
    for num, period in zip(interval.split(' '),interval.split(' ')[1:]):
        if period.startswith('day'):
            intervals['days'] = int(num)
        elif period.startswith('month'):
            intervals['months'] = int(num)
        elif period.startswith('year'):
            intervals['years'] = int(num)
    return relativedelta(**intervals)
    
class USAStats:
    def __init__(self, payload, recent_date=''):
        #? Can I change this into a payload with a property?
        self.payload = payload
        #TODO: Flags, Maps and Presidents
        self.recent_date = recent_date if recent_date else datef.today()

    def get_stats(self, date=''):
        date = date if date else self.recent_datestr
        date = date.isoformat() if isinstance(date, datef) else date
        return {'cpi': self.cpi_data.loc[self.cpi_data['Year and Month'] <= date].iloc[-1]['Adj CPI'],
                'us_population': self.us_population[self.us_population['Census year'] <= int(date[:4])].iloc[-1]['Population'],
                'world_population': self.world_population[self.world_population['year'] <= int(date[:4])].iloc[-1]['Population'],
                'state_admissions': self.state_admissions.loc[self.state_admissions['Clean Date'] <= date],
                'us_gdp': tuple(self.us_gdp.loc[self.us_gdp['time']<=int(date[:4])][['Income per person','GDP total']].iloc[-1]),
                'world_gdp': tuple(self.world_gdp.loc[self.world_gdp['time']<=int(date[:4])][['Income per person','GDP total']].iloc[-1])
                }
    
    @property
    def recent_date(self):
        return self._recent_date
    
    @property
    def recent_datestr(self):
        return f'{self._recent_date:%Y-%m-%d}'
    
    @recent_date.setter
    def recent_date(self, value):
        if isinstance(value, str):
            value = datef.fromisoformat(value)
        self._recent_date = value

    @property
    def year(self):
        return self._recent_date.year

    @property
    def yearstr(self):
        return f'{self._recent_date.year}'

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = {name: pd.read_csv(file) for name, file in value.items()}
    
    @property
    def cpi_data(self):
        return self.payload['cpi_data']
    
    @property
    def state_admissions(self):
        return self.payload['state_admissions']
    
    @property
    def us_population(self):
        return self.payload['us_population']
    
    @property
    def world_population(self):
        return self.payload['world_population']
    
    @property
    def us_gdp(self):
        return self.payload['us_gdp']
    
    @property
    def world_gdp(self):
        return self.payload['world_gdp']

_data_sets = {'cpi_data': 'combined_cpi.csv',
              'state_admissions': 'state_admissions.csv',
              'us_population': 'us_population_by_year.csv',
              'world_population': 'world_population.csv',
              'us_gdp': 'us_gdp.csv',
              'world_gdp': 'world_gdp.csv'}

_usa_stats = USAStats(_data_sets)

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

class USGDP:
    def __init__(self, us_gdp):
        self.us_gdp = us_gdp[1]
        self.per_capita = us_gdp[0]

    def __str__(self):
        return f'US GDP for the period: {self.us_gdp:,.2f}'

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

class USGDPDelta:
    def __init__(self, first_us_gdp, second_us_gdp):
        self.delta = (first_us_gdp, second_us_gdp)

    def __str__(self):
        return f'US GDP Delta for the period: {self.delta:,.2f}'
    
    @property
    def delta(self):
        return self._us_gdp_delta
    
    @delta.setter
    def delta(self, value):
        self._us_gdp_delta = value[0] / value[1]

class WorldGDP:
    def __init__(self, world_gdp):
        self.world_gdp = world_gdp
        
    def __str__(self):
        return f'World GDP for the period: {self.world_gdp:,.2f}'
    
    @property
    def world_gdp(self):
        return self._world_gdp
    
    @world_gdp.setter
    def world_gdp(self, value):
        self._world_gdp = value[1]

    @property
    def per_capita(self):
        return self._per_capita
    
    @per_capita.setter
    def per_capita(self, value):
        self._per_capita = value[0]

class WorldGDPDelta:
    def __init__(self, first_world_gdp, second_world_gdp):
        self.delta = (first_world_gdp, second_world_gdp)

    def __str__(self):
        return f'World GDP Delta for the period: {self.delta:,.2f}'
    
    @property
    def delta(self):
        return self._world_gdp_delta
    
    @delta.setter
    def delta(self, value):
        self._world_gdp_delta = value[0] / value[1]

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
    def us_pop_vis(self):
        vis = (round(self.us_pop_delta.delta * 100) * ['']) + (round(((1-self.us_pop_delta.delta) * 100)) * ['⬜'])
        return '\n'.join([''.join(vis[row:row+24]) for row in range(0, len(vis), 25)])

    @property
    def world_pop_delta(self):
        return self._world_pop_delta
    
    @property
    def world_pop_vis(self):
        vis = (round(self.us_pop_delta.delta * 100) * ['👨‍👩‍👧‍👧']) + (round(((1-self.us_pop_delta.delta) * 100)) * ['⬜'])
        return '\n'.join([''.join(vis[row:row+24]) for row in range(0, len(vis), 25)])

class PeriodData:
    def __init__(self, date=''):
        #TODO: Refactor dates from string to datetime
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
        self.us_gdp = date_stats['us_gdp']
        self.world_gdp = date_stats['world_gdp']
    
    def __str__(self):
        return f'Stats for {self.datestr}\n{str(self.cpi)}\n{str(self.us_pop)}\n{str(self.world_pop)}\n{str(self.us_gdp)}\n{str(self.world_gdp)}'

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
        elif isinstance(compare_date, relativedelta):
            new_date =self.date - compare_date
            return PeriodData(new_date)
        elif isinstance(compare_date, str):
            if len(compare_date.strip()) == 10 and compare_date[4] in ('-', '/'):
                compare_stats = _usa_stats.get_stats(compare_date)
                return PeriodDelta(self.date, compare_date, self.cpi, compare_stats['cpi'], self.us_pop, compare_stats['us_population'], self.world_pop, compare_stats['world_population'])
            else:
                new_date = self.date - parse_interval(compare_date)
                return PeriodData(new_date)

    def __add__(self, add_interval):
        """
        Advances the statistics by a given interval
        """
        new_date = self.date + parse_interval(add_interval)
        return PeriodData(new_date)

    @property
    def stats(self):
        return self._stats
    
    @stats.setter
    def stats(self, stats):
        self._stats = stats

    @property
    def date(self):
        return self._date

    @property
    def datestr(self):
        return f'{self._date::%Y-%m-%d}'

    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = datef.fromisoformat(new_date)
        else:
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

    @property
    def us_gdp(self):
        return self._us_gdp

    @us_gdp.setter
    def us_gdp(self, new_us_gdp):
        self._us_gdp = USGDP(new_us_gdp)

    @property
    def world_gdp(self):
        return self._world_gdp

    @world_gdp.setter
    def world_gdp(self, new_world_gdp):
        self._world_gdp = WorldGDP(new_world_gdp)

if __name__ == '__main__':
    period_data = PeriodData('1871-03-18')
    print(str(period_data))
    print(str(PeriodData()))
    print(str(-period_data))
    print(parse_interval('1 day, 2 months and 4 years'))
    print(period_data - '1 day, 2 months and 4 years')
    print(period_data.datestr)
    print(parse_interval('9 years, 101 days and 3 months'))
    print(period_data + '9 years, 101 days and 3 months')
    print(period_data.datestr)
