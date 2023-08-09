from typing import Any
from fable_modules.fable_library.date import (now, today as today_1, add_days, add_months, specify_kind, days_in_month as days_in_month_1, to_string, day, month, date, hour, minute, second, millisecond, to_universal_time, to_local_time)
from fable_modules.fable_library.date_offset import (now as now_1, day as day_1, month as month_1, date as date_1, hour as hour_1, minute as minute_1, second as second_1, millisecond as millisecond_1, to_universal_time as to_universal_time_1, to_local_time as to_local_time_1)
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

to_console(("Current UniversalTime is " + str(to_universal_time(current_date))) + "")

to_console(("Current Offset LocalTime is " + str(to_local_time(current_date))) + "")

to_console(("Current Date ToString is " + date_to_string) + "")

current_date_offset: Any = now_1()

to_console(("Current Offset Day is " + str(day_1(current_date_offset))) + "")

to_console(("Current Offset Month is " + str(month_1(current_date_offset))) + "")

to_console(("Current Offset Date is " + str(date_1(current_date_offset))) + "")

to_console(("Current Offset Hour is " + str(hour_1(current_date_offset))) + "")

to_console(("Current Offset Minute is " + str(minute_1(current_date_offset))) + "")

to_console(("Current Offset Second is " + str(second_1(current_date_offset))) + "")

to_console(("Current Offset Millisecond is " + str(millisecond_1(current_date_offset))) + "")

to_console(("Current Offset UniversalTime is " + str(to_universal_time_1(current_date_offset))) + "")

to_console(("Current Offset LocalTime is " + str(to_local_time_1(current_date_offset))) + "")

