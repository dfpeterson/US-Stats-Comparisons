import pandas as pd
from math import ceil, floor, log
from datetime import date as datef
from dateutil.relativedelta import relativedelta

MAGNITUDES = ['units', 'thousand', 'million', 'billion', 'trillion',
              'quadrillion', 'quintillion', 'sextillion', 'septillion',
              'octillion', 'nonillion', 'decillion']

#TODO: Organize by comparative classes and factual classes

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
        #TODO: Maps
        self.payload = payload
        self.recent_date = recent_date if recent_date else datef.today()

    def get_stats(self, date=''):
        date = date if date else self.recent_datestr
        date = date.isoformat() if isinstance(date, datef) else date
        return {'cpi': self.cpi_data.loc[self.cpi_data['Year and Month'] <= date].iloc[-1]['Adj CPI'],
                'us_population': self.us_population[self.us_population['Census year'] <= int(date[:4])].iloc[-1]['Population'],
                'world_population': self.world_population[self.world_population['year'] <= int(date[:4])].iloc[-1]['Population'],
                'state_admissions': self.state_admissions.loc[self.state_admissions['Clean Date'] <= date],
                #Tuples because it passes multiple values like both per capita and total
                'us_gdp': tuple(self.us_gdp.loc[self.us_gdp['time']<=int(date[:4])][['Income per person','GDP total']].iloc[-1]),
                'world_gdp': tuple(self.world_gdp.loc[self.world_gdp['time']<=int(date[:4])][['Income per person','GDP total']].iloc[-1]),
                'presidents': tuple(self.presidents.loc[self.presidents['inauguration date'] <= date].iloc[-1]),
                'flags': tuple(self.flags.loc[self.flags['date'] <= date].iloc[-1]),
                'amendments': self.amendments.loc[self.amendments['date'] <= date].iloc[-1]['number'],
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
        self._payload = {name: pd.read_csv(f'data/{file}') for name, file in value.items()}
    
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
    
    @property
    def presidents(self):
        return self.payload['presidents']
    
    @property
    def flags(self):
        return self.payload['flags']
    
    @property
    def amendments(self):
        return self.payload['amendments']

_data_sets = {'cpi_data': 'combined_cpi.csv',
              'state_admissions': 'state_admissions.csv',
              'us_population': 'us_population_by_year.csv',
              'world_population': 'world_population.csv',
              'us_gdp': 'us_gdp.csv',
              'world_gdp': 'world_gdp.csv',
              'presidents': 'presidents.csv',
              'flags': 'flags.csv',
              #'maps': 'maps.csv',
              'amendments': 'amendments.csv',
              }

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

class StateAdmissions:
    def __init__(self, states_admittied):
        self._states_admitted = states_admittied
    
    def __str__(self):
        return f'State Admissions for the period: {self.num_states}'

    @property
    def states_admitted(self):
        return self._states_admitted
    
    @states_admitted.setter
    def states_admitted(self, value):
        self._states_admitted = value

    @property
    def num_states(self):
        return len(self._states_admitted)
    
    @property
    def last_state(self):
        return self._states_admitted[-1]

class President:
    def __init__(self, president):
        self.name = president[2]
        self.image = president[3]
        self.number = president[0]
        self.inauguration = president[1]

    def __str__(self):
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(self.number, 'th')
        return f'{self.name} the {self.number}{suffix} President'
    
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, value):
        self._image = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        self._number = value
    
    @property
    def inauguration(self):
        return self._inauguration
    
    @inauguration.setter
    def inauguration(self, value):
        self._inauguration = value

class Flag:
    def __init__(self, flag):
        self.stars = flag[1]
        self.image = flag[2]

    def __str__(self):
        return f'{self.stars}-Star Flag'
    
    @property
    def stars(self):
        return self._stars
    
    @stars.setter
    def stars(self, value):
        self._stars = value

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, value):
        self._image = value

class Amendments:
    def __init__(self, amendments):
        self.amendments = amendments

    def __str__(self):
        return f'{self.amendments}'
    
    @property
    def amendments(self):
        return self._amendments
    
    @amendments.setter
    def amendments(self, value):
        self._amendments = value

    def __eq__(self, value):
        return self.amendments == value
    
    def __ne__(self, value):
        return self.amendments != value
    
    def __gt__(self, value):
        return self.amendments > value
    
    def __ge__(self, value):
        return self.amendments >= value
    
    def __lt__(self, value):
        return self.amendments < value
    
    def __le__(self, value):
        return self.amendments <= value

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
        return f'{self.us_gdp/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude]}'
    
    @property
    def pretty_per_capita(self):
        return f'{self.per_capita/(1000**self.magnitude_per_capita):,.1f} {MAGNITUDES[self.magnitude_per_capita]}'

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
        return f'{self.world_gdp/(1000**self.magnitude):,.1f} {MAGNITUDES[self.magnitude]}'
    
    @property
    def pretty_per_capita(self):
        return f'{self.per_capita/(1000**self.magnitude_per_capita):,.1f} {MAGNITUDES[self.magnitude_per_capita]}'
    

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

class PeriodDelta:
    def __init__(self, first_date, second_date, first_cpi, second_cpi, first_us_pop, second_us_pop, first_world_pop, second_world_pop, first_us_gdp, second_us_gdp, first_world_gdp, second_world_gdp):
        self.first_date = first_date
        self.second_date = second_date
        self._cpi_delta = CPIDelta(first_cpi, second_cpi)
        self._us_pop_delta = USPopulationDelta(first_us_pop, second_us_pop)
        self._world_pop_delta = WorldPopulationDelta(first_world_pop, second_world_pop)
        self._us_gdp_delta = USGDPDelta(first_us_gdp, second_us_gdp)
        self._world_gdp_delta = WorldGDPDelta(first_world_gdp, second_world_gdp)

    def __str__(self):
        return f'Period Delta from {self.first_date} to {self.second_date}:\n{str(self.cpi_delta)}\n{str(self.us_pop_delta)}\n{str(self.world_pop_delta)}\n{str(self.us_gdp_delta)}\n{str(self.world_gdp_delta)}'
    
    @property
    def first_date(self):
        return self._first_date
    
    @first_date.setter
    def first_date(self, date):
        self._first_date = date

    @property
    def first_year(self):
        return self.first_date.year

    @property
    def second_date(self):
        return self._second_date
    
    @second_date.setter
    def second_date(self, date):
        self._second_date = date

    @property
    def second_year(self):
        return self.second_date.year

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
    
    @property
    def us_gdp_delta(self):
        return self._us_gdp_delta
    
    @property
    def world_gdp_delta(self):
        return self._world_gdp_delta
    
    @property
    def us_gdp_vis(self):
        vis = (round(self.us_gdp_delta.delta * 100) * ['']) + (round(((1-self.us_gdp_delta.delta) * 100)) * ['⬜'])
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
        self.president = date_stats['presidents']
        self.flag = date_stats['flags']
        self.amendments = date_stats['amendments']
    
    def __str__(self):
        return f'Stats for {self.datestr}\n{str(self.cpi)}\n{str(self.us_pop)}\n{str(self.world_pop)}\n{str(self.us_gdp)}\n{str(self.world_gdp)}'

    def __neg__(self):
        """
        Calculates the PeriodDelta for the object compared to the current date
        """
        second_stats = _usa_stats.get_stats()
        return PeriodDelta(self.date, self.recent_date, self.cpi, second_stats['cpi'], self.us_pop, second_stats['us_population'], self.world_pop, second_stats['world_population'], self.us_gdp, second_stats['us_gdp'], self.world_gdp, second_stats['world_gdp'])

    def __sub__(self, compare_date):
        """
        If the object is another date or PeriodData compares the statistics
        for a given date or other PeriodData instance and the date stored
        in the left side PeriodData. Returns a PeriodDelta.
        If the object is a time delta it adjusts the object the new data
        """
        if isinstance(compare_date, PeriodData):
            return PeriodDelta(self.date, compare_date.date, self.cpi, compare_date.cpi, self.us_pop, compare_date.us_pop, self.world_pop, compare_date.world_pop, self.us_gdp, compare_date.us_gdp, self.world_gdp, compare_date.world_gdp)
        elif isinstance(compare_date, relativedelta):
            new_date =self.date - compare_date
            return PeriodData(new_date)
        elif isinstance(compare_date, str):
            if len(compare_date.strip()) == 10 and compare_date[4] in ('-', '/'):
                compare_stats = _usa_stats.get_stats(compare_date)
                return PeriodDelta(self.date, compare_date, self.cpi, compare_stats['cpi'], self.us_pop, compare_stats['us_population'], self.world_pop, compare_stats['world_population'], self.us_gdp, compare_stats['us_gdp'], self.world_gdp, compare_stats['world_gdp'])
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
        self._state_admissions = StateAdmissions(new_state_admissions)

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

    @property
    def president(self):
        return self._president
    
    @president.setter
    def president(self, president):
        self._president = President(president)

    @property
    def flag(self):
        return self._flag
    
    @flag.setter
    def flag(self, flag):
        self._flag = Flag(flag)
    
    @property
    def amendments(self):
        return self._amendments
    
    @amendments.setter
    def amendments(self, amendments):
        self._amendments = Amendments(amendments)

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
