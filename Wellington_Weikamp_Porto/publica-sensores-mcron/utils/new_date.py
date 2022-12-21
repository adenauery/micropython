import time

TIME = time.localtime()

class NewDate:
    def __init__(self):
        self.__year = TIME[0]
        self.__month = TIME[1]
        self.__day = TIME[2]
        self.__local_hour = TIME[3]
        self.__minute = TIME[4]
        self.__second = TIME[5]

    @property
    def year(self):
        return str(self.__year)

    @property
    def month(self):
        return str(self.__month)

    @property
    def day(self):
        return str(self.__day)

    @property
    def local_hour(self):
        return str(self.__local_hour)
    
    @property
    def minute(self):
        return str(self.__minute)

    @property
    def second(self):
        return str(self.__second)

    @property
    def get_date(self):
        return f'{self.year}-{self.month}-{self.day} {self.local_hour}:{self.minute}:{self.second}'
        
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day} {self.local_hour}:{self.minute}:{self.second}'