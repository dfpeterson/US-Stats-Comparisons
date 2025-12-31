from dateutil.relativedelta import relativedelta
from math import floor, log
from datetime import datetime


MAGNITUDES = ['units', 'thousand', 'million', 'billion', 'trillion',
              'quadrillion', 'quintillion', 'sextillion', 'septillion',
              'octillion', 'nonillion', 'decillion']

COUNTRY_CODES = {'wld': 'World', 'usa': 'United States'}

STATE_NAMES = {'alabama': 'al', 'alaska': 'ak', 'arizona': 'az', 'arkansas': 'ar', 'california': 'ca', 'colorado': 'co', 'connecticut': 'ct', 'delaware': 'de',
               'florida': 'fl', 'georgia': 'ga', 'hawaii': 'hi', 'idaho': 'id', 'illinois': 'il', 'indiana': 'in', 'iowa': 'ia', 'kansas': 'ks', 'kentucky': 'ky',
               'louisiana': 'la', 'maine': 'me', 'maryland': 'md', 'massachusetts': 'ma', 'michigan': 'mi', 'minnesota': 'mn', 'mississippi': 'ms', 'missouri': 'mo',
               'montana': 'mt', 'nebraska': 'ne', 'nevada': 'nv', 'new hampshire': 'nh', 'new jersey': 'nj', 'new mexico': 'nm', 'new york': 'ny', 'north carolina': 'nc',
               'north dakota': 'nd', 'ohio': 'oh', 'oklahoma': 'ok', 'oregon': 'or', 'pennsylvania': 'pa', 'rhode island': 'ri', 'south carolina': 'sc',
               'south dakota': 'sd', 'tennessee': 'tn', 'texas': 'tx', 'utah': 'ut', 'vermont': 'vt', 'virginia': 'va', 'washington': 'wa', 'west virginia': 'wv',
               'wisconsin': 'wi', 'wyoming': 'wy', 'district of columbia': 'dc', 'washington d.c.': 'dc', 'puerto rico': 'pr', 'virgin islands': 'vi', 'guam': 'gu',
               'american samoa': 'as', 'northern mariana islands': 'mp'}

def magnitude(num):
    return MAGNITUDES[floor(log(num, 1000))]

def code_to_name(code):
    if code.lower() in COUNTRY_CODES:
        return COUNTRY_CODES[code.lower()]
    if code.lower in STATE_NAMES:
        return STATE_NAMES[code.lower()]
    return code
def date_pretty(ugly_date):
    if isinstance(ugly_date, str):
        ugly_date = datetime.strptime(ugly_date, '%Y-%m-%d')
    return ugly_date.strftime('%B %d, %Y')

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