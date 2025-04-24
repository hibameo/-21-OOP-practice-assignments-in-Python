
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
