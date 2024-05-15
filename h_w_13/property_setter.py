class Workers:

    def __init__(self, name, position, bonus, rate):
        self._name = name
        self._position = position
        self.bonus = bonus
        self.rate = rate

    def __str__(self):
        return (f'{self.__class__.__name__}. Employee {self._name} in the position {self._position} '
                f', bonus {self.bonus}, rate {self.rate} and salary {self.salary}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name.isalpha():
            raise ValueError('Name should contain only letter')
        self._name = new_name

    @name.deleter
    def name(self):
        raise PermissionError('You can\t chose attribute')

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if not new_position.isalpha():
            raise ValueError('Name should contain only letter')
        self._position = new_position

    @position.deleter
    def position(self):
        raise PermissionError('You can\t chose attribute')

    @property
    def salary(self):
        return (self.bonus * self.rate // 100) + self.rate

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Experience should contain only number')
        if not value >= 0:
            raise ValueError('Experience should contain only positive')
        self._bonus = float(value)

    @bonus.deleter
    def bonus(self):
        raise PermissionError('You can\t chose attribute')

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Experience should contain only number')
        if not value >= 0:
            raise ValueError('Experience should contain only positive')
        self._rate = float(value)


if __name__ == '__main__':
    oleh = Workers('Oleh', 'Director', 32, 45000)
    print(oleh)
    anna = Workers('Anna', 'Deputy', 28, 38000)
    print(anna)
    inna = Workers('Inna', 'Head of department', 16, 30000)
    print(inna)
    stanislav = Workers('Stanislav', 'Head of department', 15, 28000)
    print(stanislav)
    ihor = Workers('Ihor', 'Head of department', 8, 29000)
    print(ihor)
    ira = Workers('Ira', 'Doctor', 30, 28000)
    print(ira)
    maya = Workers('Maya', 'Doctor', 22, 24000)
    print(maya)
    nazar = Workers('Nazar', 'Doctor', 14, 23000)
    print(nazar)
    anatoliy = Workers('Anatoliy', 'Doctor', 10, 24000)
    print(anatoliy)
    marat = Workers('Marat', 'Intern', 1, 13000)
    print(marat)
    misha = Workers('Misha', 'Intern', 1, 13000)
    misha.bonus = 5
    print(misha)
