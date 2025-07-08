import pandas as pd
from math import ceil, floor, log
from datetime import date as datef
from dateutil.relativedelta import relativedelta
from stats_engine.usa_stats import USAStats



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
