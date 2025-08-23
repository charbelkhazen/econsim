class Agent:
    def __init__(self, asset, liab):
        self.asset = asset
        self.liab = liab
        self.bal = asset + liab
    def __add__(self, other):
        x = self.asset + other.asset
        y = self.liab + other.liab
        return (x - y)
    def __repr__(self):
        return (f'Agent({self.asset!r}, {self.liab!r})')
    def __str__(self):
        return (f"Assets: {self.asset}, Liabilities: {self.liab}")
