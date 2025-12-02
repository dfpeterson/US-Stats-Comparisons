from dateutil.relativedelta import relativedelta
from datetime import date
from stats_engine.helpers import MAGNITUDES, parse_interval, _data_sets
from stats_engine.stats.country.usa_stats import USAStats
from stats_engine.stats.cpi import CPI, CPIDelta
from stats_engine.stats.population import Population, PopulationDelta
from stats_engine.stats.gdp import GDP, GDPDelta
from stats_engine.stats.country.us.fct.us_const_amendments import Amendments
from stats_engine.stats.country.us.fct.us_flags import Flag
from stats_engine.stats.country.us.fct.us_presidents import President
from stats_engine.stats.country.us.fct.us_state_admissions import StateAdmissions

#This is a cache of the stats so if I need to get comparisons I can do it without reloading the file
_usa_stats = USAStats(_data_sets)

#TODO: Implement generic classes
class PeriodDelta:
    def __init__(self, first_period: dict, second_period: dict):
        self.first_date = first_period['period_date']
        self.second_date = second_period['period_date']
        self.cpi_delta = CPIDelta(first_period['cpi'], second_period['cpi'])
        self.us_pop_delta = PopulationDelta(first_period['us_pop'], second_period['us_pop'])
        self.world_pop_delta = PopulationDelta(first_period['world_pop'], second_period['world_pop'])
        self.us_gdp_delta = GDPDelta(first_period['us_gdp'], second_period['us_gdp'])
        self.world_gdp_delta = GDPDelta(first_period['world_gdp'], second_period['world_gdp'])

    def __str__(self):
        return f'Period Delta from {self.first_date} to {self.second_date}:\n{str(self.cpi_delta)}\n{str(self.us_pop_delta)}\n{str(self.world_pop_delta)}\n{str(self.us_gdp_delta)}\n{str(self.world_gdp_delta)}'
    
    @property
    def first_date(self):
        return self._first_date
    
    @first_date.setter
    def first_date(self, first_date):
        self._first_date = first_date

    @property
    def first_year(self):
        return self.first_date.year

    @property
    def second_date(self):
        return self._second_date
    
    @second_date.setter
    def second_date(self, second_date):
        self._second_date = second_date

    @property
    def second_year(self):
        return self.second_date.year

    @property
    def cpi_delta(self):
        return self._cpi_delta
    
    @cpi_delta.setter
    def cpi_delta(self, value):
        self._cpi_delta = value
    
    @property
    def us_pop_delta(self):
        return self._us_pop_delta
    
    @us_pop_delta.setter
    def us_pop_delta(self, value):
        self._us_pop_delta = value

    @property
    def world_pop_delta(self):
        return self._world_pop_delta
    
    @world_pop_delta.setter
    def world_pop_delta(self, value):
        self._world_pop_delta = value
        
    @property
    def us_gdp_delta(self):
        return self._us_gdp_delta

    @us_gdp_delta.setter
    def us_gdp_delta(self, value):
        self._us_gdp_delta = value

    @property
    def world_gdp_delta(self):
        return self._world_gdp_delta
    
    @world_gdp_delta.setter
    def world_gdp_delta(self, value):
        self._world_gdp_delta = value

class PeriodData:
    def __init__(self, period_date=''):
        #TODO: Refactor dates from string to datetime
        if period_date:
            date_stats = _usa_stats.get_stats(period_date)
            self.period_date = period_date
        else:
            date_stats = _usa_stats.get_stats()
            self.period_date = _usa_stats.recent_date
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
        #TODO: Generate 2nd PeriodData object and convert to PeriodDelta pass-alongs
        #second_stats = _usa_stats.get_stats()
        return PeriodDelta(self.dict, PeriodData().dict)
        #return PeriodDelta(self.period_date, self.recent_date, self.cpi, second_stats['cpi'], self.us_pop, second_stats['us_population'], self.world_pop, second_stats['world_population'], self.us_gdp, second_stats['us_gdp'], self.world_gdp, second_stats['world_gdp'])

    def __sub__(self, compare_date):
        """
        If the object is another date or PeriodData compares the statistics
        for a given date or other PeriodData instance and the date stored
        in the left side PeriodData. Returns a PeriodDelta.
        If the object is a time delta it adjusts the object the new data
        """
        if isinstance(compare_date, PeriodData):
            return PeriodDelta(self.dict, compare_date.dict)
        elif isinstance(compare_date, relativedelta):
            new_date = self.period_date - compare_date
            return PeriodData(new_date)
        elif isinstance(compare_date, str):
            if len(compare_date.strip()) == 10 and compare_date[4] in ('-', '/'):
                compare_stats = _usa_stats.get_stats(compare_date)
                return PeriodDelta(self.dict, PeriodData(compare_date).dict)
                #return PeriodDelta(self.period_date, compare_date, self.cpi, compare_stats['cpi'], self.us_pop, compare_stats['us_population'], self.world_pop, compare_stats['world_population'], self.us_gdp, compare_stats['us_gdp'], self.world_gdp, compare_stats['world_gdp'])
            else:
                new_date = self.period_date - parse_interval(compare_date)
                return PeriodData(new_date)

    def __add__(self, add_interval):
        """
        Advances the statistics by a given interval
        """
        new_date = self.period_date + parse_interval(add_interval)
        return PeriodData(new_date)

    @property
    def stats(self):
        return self._stats
    
    @stats.setter
    def stats(self, stats):
        self._stats = stats

    @property
    def period_date(self):
        return self._period_date

    @property
    def datestr(self):
        return f'{self._date::%Y-%m-%d}'

    @period_date.setter
    def period_date(self, new_date):
        if isinstance(new_date, str):
            self._period_date = date.fromisoformat(new_date)
        else:
            self._period_date = new_date

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
        self._us_population = Population(**new_us_pop)
    
    @property
    def world_pop(self):
        return self._world_population
    
    @world_pop.setter
    def world_pop(self, new_world_pop):
        self._world_population = Population(**new_world_pop)
    
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
        self._us_gdp = GDP(self.period_date, 'United States', new_us_gdp['GDP total'], new_us_gdp['Income per person'])

    @property
    def world_gdp(self):
        return self._world_gdp

    @world_gdp.setter
    def world_gdp(self, new_world_gdp):
        self._world_gdp = GDP(self.period_date, 'World', new_world_gdp['GDP total'], new_world_gdp['Income per person'])

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

    @property
    def dict(self):
        return {'period_date': self.period_date,
            'cpi': self.cpi.cpi,
            'us_pop': self.us_pop,
            'world_pop': self.world_pop,
            'state_admissions': self.state_admissions,
            'us_gdp': self.us_gdp,
            'world_gdp': self.world_gdp,
            'president': self.president,
            'flag': self.flag,
            'amendments': self.amendments
        }
