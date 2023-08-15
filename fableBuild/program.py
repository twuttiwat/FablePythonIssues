from __future__ import annotations
from dataclasses import dataclass
from typing import (Any, Optional, Tuple)
from fable_modules.fable_library.date import (now, today as today_1, add_days, add_months, specify_kind, days_in_month as days_in_month_1, to_string, day, month, date, hour, minute, second, millisecond, to_universal_time, to_local_time, min_value, try_parse as try_parse_1)
from fable_modules.fable_library.date_offset import (now as now_1, day as day_1, month as month_1, date as date_1, hour as hour_1, minute as minute_1, second as second_1, millisecond as millisecond_1, to_universal_time as to_universal_time_1, to_local_time as to_local_time_1, min_value as min_value_1, try_parse as try_parse_2)
from fable_modules.fable_library.reflection import (full_name, uint64_type, TypeInfo, string_type, option_type, record_type)
from fable_modules.fable_library.string_ import (to_console, printf)
from fable_modules.fable_library.time_span import (create, try_parse)
from fable_modules.fable_library.types import (uint64, Record, FSharpRef)
from fable_modules.fable_library.util import equals

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

an_unit64: uint64 = uint64(1)

def _arrow84(__unit: None=None) -> Any:
    copy_of_struct: uint64 = an_unit64
    return uint64_type


to_console(("FullName of Uint64 Type is " + full_name(_arrow84())) + ".")

def _expr85() -> TypeInfo:
    return record_type("Program.RecordWithNone", [], RecordWithNone, lambda: [("FieldA", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RecordWithNone(Record):
    FieldA: Optional[str]

RecordWithNone_reflection = _expr85

r1: RecordWithNone = RecordWithNone(None)

r2: RecordWithNone = RecordWithNone(None)

to_console(("Record with None should equal: " + str(equals(r1, r2))) + "")

def _expr86() -> TypeInfo:
    return record_type("Program.RecordWithNil", [], RecordWithNil, lambda: [("FieldA", string_type)])


@dataclass(eq = False, repr = False)
class RecordWithNil(Record):
    FieldA: str

RecordWithNil_reflection = _expr86

r3: RecordWithNil = RecordWithNil(None)

r4: RecordWithNil = RecordWithNil(None)

to_console(("Record with null should equal: " + str(equals(r3, r4))) + "")

tupled_arg: Tuple[bool, Any]

out_arg: Any = create(0)

def _arrow87(__unit: None=None) -> Any:
    return out_arg


def _arrow88(v: Any) -> None:
    global out_arg
    out_arg = v



tupled_arg = (try_parse("12:34", FSharpRef(_arrow87, _arrow88)), out_arg)

to_console(printf("TimeSpan TryParse %A"))((tupled_arg[0], tupled_arg[1]))

tupled_arg: Tuple[bool, Any]

out_arg: Any = min_value()

def _arrow89(__unit: None=None) -> Any:
    return out_arg


def _arrow90(v: Any) -> None:
    global out_arg
    out_arg = v



tupled_arg = (try_parse_1("1/1/2000", FSharpRef(_arrow89, _arrow90)), out_arg)

to_console(printf("DateTime TryParse %A"))((tupled_arg[0], tupled_arg[1]))

tupled_arg: Tuple[bool, Any]

out_arg: Any = min_value_1()

def _arrow91(__unit: None=None) -> Any:
    return out_arg


def _arrow92(v: Any) -> None:
    global out_arg
    out_arg = v



tupled_arg = (try_parse_2("1/1/2000", FSharpRef(_arrow91, _arrow92)), out_arg)

to_console(printf("DateTimeOffset TryParse %A"))((tupled_arg[0], tupled_arg[1]))

