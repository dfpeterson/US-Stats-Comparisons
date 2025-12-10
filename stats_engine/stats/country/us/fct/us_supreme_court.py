class SupremeCourt:
    class Justice:
        def __init__(self, name, term_start, term_end, is_chief=False):
            self.name = name
            self.term_start = term_start
            self.term_end = term_end
            self.is_chief = is_chief
    def __init__(self, justices):
        self.justices = justices