from typing import Any
from fable_modules.fable_library.date import (today as today_1, now, add_days, add_months, specify_kind, days_in_month as days_in_month_1, day, month, date, hour, minute, second, millisecond)
from fable_modules.fable_library.string_ import to_console

today: Any = today_1()

current_date: Any = now()

tomorrow: Any = add_days(current_date, 1)

next_month: Any = add_months(current_date, 1)

local_today: Any = specify_kind(current_date, 2)

days_in_month: int = days_in_month_1(2000, 1)

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

