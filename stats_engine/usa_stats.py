class USAStats:
    def __init__(self, payload, recent_date=''):
        #TODO: Maps
        self.payload = payload
        self.recent_date = recent_date if recent_date else datef.today()

    def get_stats(self, date=''):
        #! This is functional, but not correct for presidents, amendments and states before 1800 or the constitutional convention
        def safe_get(frame, date_field, date, return_field):
            if isinstance(return_field, str):
                return_value = frame[frame[date_field] <= date]
                if len(return_value):
                    return return_value.iloc[-1][return_field]
                else:
                    return frame.iloc[0][return_field]
            elif isinstance(return_field, list):
                return_value = frame[frame[date_field] <= date]
                if len(return_value):
                    return return_value[return_field].iloc[-1]
                else:
                    return frame.iloc[0][return_field]


        date = date if date else self.recent_datestr
        date = date.isoformat() if isinstance(date, datef) else date
        year = int(date[:4])
        return {'cpi': safe_get(self.cpi_data, 'Year and Month', date, 'Adj CPI'), #self.cpi_data.loc[self.cpi_data['Year and Month'] <= date].iloc[-1]['Adj CPI'],
                'us_population': safe_get(self.us_population, 'Census year', year, 'Population'), # self.us_population[self.us_population['Census year'] <= int(date[:4])].iloc[-1]['Population'],
                'world_population': safe_get(self.world_population, 'year', year, 'Population'), # self.world_population[self.world_population['year'] <= int(date[:4])].iloc[-1]['Population'],
                'state_admissions': self.state_admissions.loc[self.state_admissions['Clean Date'] <= date],
                #Tuples because it passes multiple values like both per capita and total
                'us_gdp': tuple(safe_get(self.us_gdp, 'time', year, ['Income per person','GDP total'])), #self.us_gdp.loc[self.us_gdp['time']<=int(date[:4])][['Income per person','GDP total']].iloc[-1]),
                'world_gdp': tuple(safe_get(self.world_gdp, 'time', year, ['Income per person','GDP total'])), #self.world_gdp.loc[self.world_gdp['time']<=int(date[:4])][['Income per person','GDP total']].iloc[-1]),
                'presidents': tuple(safe_get(self.presidents, 'inauguration date', date, ['number','inauguration date','name','file'])),  #self.presidents.loc[self.presidents['inauguration date'] <= date].iloc[-1]),
                'flags': tuple(safe_get(self.flags, 'date', date, ['date','number of stars','file name'])), #self.flags.loc[self.flags['date'] <= date].iloc[-1]),
                'amendments': safe_get(self.amendments, 'date', date, 'number'), #self.amendments.loc[self.amendments['date'] <= date].iloc[-1]['number'],
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