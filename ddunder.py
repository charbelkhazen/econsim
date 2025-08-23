class Agent:
    def __init__(self, age):
        self.age = age
    def __add__(self, other):
        x = self.age
        y = other.age
        return (x + y)

bob = Agent(12)
ray = Agent(11)
print(bob + ray);
