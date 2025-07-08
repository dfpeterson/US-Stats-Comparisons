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
