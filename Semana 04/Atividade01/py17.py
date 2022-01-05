import datetime

d = datetime.date(2016, 7, 24)
print(d)

hoje = datetime.date.today()
print(hoje)
print(hoje.year)
print(hoje.month)
print(hoje.day)

tdelta = datetime.timedelta(days=7)

print(hoje + tdelta)

aniv = datetime.date(2022, 6, 13)

print(aniv - hoje)
print((aniv - hoje).total_seconds())


# TIME ZONE
import pytz

dt = datetime.datetime(2022, 6, 13, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

for tz in pytz.all_timezones:
    print(tz)


hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%Y')  # com y ele retorna os dois últimos dígitos do ano
print(hoje_formatado)