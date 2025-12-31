from stats_engine.helpers import date_pretty

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
        return self._states_admitted.iloc[-1].to_dict()

    @property
    def last_state_name(self):
        return self.last_state['State']
    
    @property
    def last_state_date(self):
        return self.last_state['Clean Date']
    
    @property
    def last_state_pretty_date(self):
        return date_pretty(self.last_state_date)