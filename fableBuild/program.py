from typing import Any
from fable_modules.fable_library.date import (now, today as today_1, add_days, add_months, specify_kind, days_in_month as days_in_month_1, to_string, day, month, date, hour, minute, second, millisecond, to_universal_time)
from fable_modules.fable_library.string_ import to_console

current_date: Any = now()

today: Any = today_1()

tomorrow: Any = add_days(current_date, 1)

next_month: Any = add_months(current_date, 1)

local_today: Any = specify_kind(current_date, 2)

days_in_month: int = days_in_month_1(2000, 1)

date_to_string: str = to_string(current_date, "O")

to_console(("Today is " + str(today)) + "")

to_console(("Tomorrow is " + str(tomorrow)) + "")

to_console(("Next month is " + str(next_month)) + "")

to_console(("Current Day is " + str(day(current_date))) + "")

to_console(("Current Month is " + str(month(current_date))) + "")

to_console(("Current Date is " + str(date(current_date))) + "")

to_console(("Current Hour is " + str(hour(current_date))) + "")

to_console(("Current Minute is " + str(minute(current_date))) + "")

to_console(("Current Second is " + str(second(current_date))) + "")

to_console(("Current Millisecond is " + str(millisecond(current_date))) + "")

to_console(("Local date for today is " + str(local_today)) + "")

to_console(("Days in Months is " + str(days_in_month)) + "")

to_console(("UniversalTime is " + str(to_universal_time(current_date))) + "")

to_console(("Current Date ToString is " + date_to_string) + "")

