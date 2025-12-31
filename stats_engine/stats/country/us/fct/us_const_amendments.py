class Amendments:
    def __init__(self, amendments):
        self.amendments = amendments['number']
        self.numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII']

    def __str__(self):
        return f'{self.amendments}'
    
    @property
    def amendments(self):
        return self._amendments
    
    @amendments.setter
    def amendments(self, value):
        self._amendments = value

    def __eq__(self, value):
        return self.amendments == value
    
    def __ne__(self, value):
        return self.amendments != value
    
    def __gt__(self, value):
        return self.amendments > value
    
    def __ge__(self, value):
        return self.amendments >= value
    
    def __lt__(self, value):
        return self.amendments < value
    
    def __le__(self, value):
        return self.amendments <= value

    @property
    def as_numeral(self):
        return self.numerals[self.amendments - 1]
    
    @property
    def html(self):
        html_friendly = []
        for digit in range(1, self.amendments + 1):
            numeral = self.numerals[digit - 1]
            if digit > 10:
                if digit == 18 and self.amendments >= 21:
                    html_friendly.append(f'<a href="https://www.archives.gov/founding-docs/amendments-11-27#{numeral.lower()}"><s>{numeral}</s></a>')
                else:
                    html_friendly.append(f'<a href="https://www.archives.gov/founding-docs/amendments-11-27#{numeral.lower()}">{numeral}</a>')
            else:
                html_friendly.append(f'<a href="https://www.archives.gov/founding-docs/bill-of-rights-transcript#toc-amendment-{numeral.lower()}">{numeral}</a>')
        return '<br>\n'.join(html_friendly)