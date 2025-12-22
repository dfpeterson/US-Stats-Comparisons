class Justice:
    def __init__(self, name, term_start, term_end, is_chief=False):
        self.name = name
        self.term_start = term_start
        self.term_end = term_end
        self.is_chief = is_chief


class SupremeCourt:
    def __init__(self, justices):
        #TODO: Figure out vacanices if under 9
        #for justice in justices:
        #    self.justices = Justice(justice)
        self.justices = justices
    
    @property
    def justices(self):
        self._justices
    
    @justices.setter
    def justices(self, value):
        self._justices = value