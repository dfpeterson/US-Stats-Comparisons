from datetime import date
import pandas as pd

class Justice:
    def __init__(self, justice, *base_date):
        self.name = justice['name']
        self.state = justice['state']
        self.president = justice['president']
        self.chief = justice['chief']
        self.oath_date = justice['oath_date']
        self.term_end_date = justice['term_end_date']
        if base_date:
            self.tenure = self.get_tenure(base_date[0])
        else:
            self.tenure = None

    def __str__(self):
        return f'{self.name}'
    
    @property
    def pretty(self):
        return f'{self.name} ({self.state})'

    @property
    def html(self): 
        if self.tenure:
            return f'<strong>Chief {self.name}</strong> ({self.tenure} days)' if self.chief else f'Assoc. {self.name} ({self.tenure} days)'
        else:
            return f'<strong>Chief {self.name}</strong> ' if self.chief else f'Assoc. {self.name}'
    
    @property
    def bar_chart(self):
        return {
            'Name': self.name,
            'State': self.state,
            'President': self.president,
            'Chief': self.chief,
            'Role': 'Chief' if self.chief else 'Associate',
            'Assoc. Tenure': self.tenure if not self.chief else 0,
            'Chief Tenure': self.tenure if self.chief else 0,
            'Tenure': self.tenure
        }

    def get_tenure(self, to_date):
        return (to_date - self.oath_date).days if to_date > self.oath_date else to_date - self.oath_date

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value

    @property
    def president(self):
        return self._president
    
    @president.setter
    def president(self, value):
        self._president = value

    @property
    def chief(self):
        return self._chief
    
    @chief.setter
    def chief(self, value):
        self._chief = value

    @property
    def oath_date(self):
        return self._oath_date
    
    @oath_date.setter
    def oath_date(self, value):
        self._oath_date = date.fromisoformat(value)

    @property
    def term_end_date(self):
        return self._term_end_date
    
    @term_end_date.setter
    def term_end_date(self, value):
        self._term_end_date = date.fromisoformat(value)

    @property
    def tenure(self):
        return round(self._tenure / 365.25, 2)
    
    @tenure.setter
    def tenure(self, value):
        self._tenure = value

class SupremeCourt:
    def __init__(self, court_justices, base_date):
        #TODO: Figure out vacancies if under 9
        if base_date:
            self.justices = [Justice(justice, base_date) for justice in court_justices.to_dict(orient='records')]
        else:
            self.justices = [Justice(justice) for justice in court_justices.to_dict(orient='records')]

    def __str__(self):
        return '\n'.join([str(justice) for justice in self.justices])
    
    @property
    def justices(self):
        return self._justices
    
    @justices.setter
    def justices(self, value):
        self._justices = value

    @property
    def html(self):
        return '\n<br>'.join([justice.html for justice in self.justices])
    
    @property
    def bar_chart(self):
        return pd.DataFrame([justice.bar_chart for justice in self.justices]).sort_values('Tenure', ascending=False)