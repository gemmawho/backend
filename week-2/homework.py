import datetime as dt

TODAY = f'{dt.date.today().day}.{dt.date.today().month}.{dt.date.today().year}'


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for record in self.records:
            if record.date == dt.date.today():
                today_stats += record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        for record in self.records:
            if record.date >= dt.date.today() - dt.timedelta(7):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        for record in self.records:
            if record.date == dt.datetime.strptime(TODAY, '%d.%m.%Y').date():
                self.limit -= record.amount
        if self.limit > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit} кКал'
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        for record in self.records:
            if record.date == dt.datetime.strptime(TODAY, '%d.%m.%Y').date():
                self.limit -= record.amount
        if currency == 'usd':
            left_money = round(self.limit / self.USD_RATE, 2)
            currency = 'USD'
        elif currency == 'eur':
            left_money = round(self.limit / self.EURO_RATE, 2)
            currency = 'Euro'
        else:
            left_money = round(self.limit / 1, 2)
            currency = 'руб'
        if self.limit > 0:
            return f'На сегодня осталось {left_money} {currency}'
        elif self.limit == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {abs(left_money)} {currency}'


class Record:
    def __init__(self, amount, comment, date=TODAY):
        self.amount = amount
        self.comment = comment
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
