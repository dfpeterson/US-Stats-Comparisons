from dateutil.relativedelta import relativedelta

MAGNITUDES = ['units', 'thousand', 'million', 'billion', 'trillion',
              'quadrillion', 'quintillion', 'sextillion', 'septillion',
              'octillion', 'nonillion', 'decillion']

COUNTRY_CODES = {'wld': 'World', 'usa': 'United States'}

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
              'populations': 'populations.csv',
              'us_population': 'us_population_by_year.csv',
              'world_population': 'world_population.csv',
              'us_gdp': 'us_gdp.csv',
              'world_gdp': 'world_gdp.csv',
              'presidents': 'presidents.csv',
              #'congress': 'congress.csv',
              'supreme_court': 'supreme_court.csv',
              'flags': 'flags.csv',
              #'maps': 'maps.csv',
              'amendments': 'amendments.csv',
              }