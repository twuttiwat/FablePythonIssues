open System

/// DateTime issues
let currentDate = DateTime.Now
let today = DateTime.Today
let tomorrow = currentDate.AddDays(1)
let nextMonth = currentDate.AddMonths(1)
let localToday = DateTime.SpecifyKind(currentDate, DateTimeKind.Local)
let daysInMonth = DateTime.DaysInMonth(2000, 1)
let dateToString = currentDate.ToString("O")


printf $"Today is {today}"
printf $"Tomorrow is {tomorrow}"
printf $"Next month is {nextMonth}"
printf $"Current Day is {currentDate.Day}"
printf $"Current Month is {currentDate.Month}"
printf $"Current Date is {currentDate.Date}"
printf $"Current Hour is {currentDate.Hour}"
printf $"Current Minute is {currentDate.Minute}"
printf $"Current Second is {currentDate.Second}"
printf $"Current Millisecond is {currentDate.Millisecond}"
printf $"Local date for today is {localToday}"
printf $"Days in Months is {daysInMonth}"
printf $"Current UniversalTime is {currentDate.ToUniversalTime()}"
printf $"Current Offset LocalTime is {currentDate.ToLocalTime()}"
printf $"Current Date ToString is {dateToString}"

/// DateOffset issues
let currentDateOffset = DateTimeOffset.Now

printf $"Current Offset Day is {currentDateOffset.Day}"
printf $"Current Offset Month is {currentDateOffset.Month}"
printf $"Current Offset Date is {currentDateOffset.Date}"
printf $"Current Offset Hour is {currentDateOffset.Hour}"
printf $"Current Offset Minute is {currentDateOffset.Minute}"
printf $"Current Offset Second is {currentDateOffset.Second}"
printf $"Current Offset Millisecond is {currentDateOffset.Millisecond}"
printf $"Current Offset UniversalTime is {currentDateOffset.ToUniversalTime()}"
printf $"Current Offset LocalTime is {currentDateOffset.ToLocalTime()}"

/// Reflection issues
let anUnit64 = 1UL
printf $"FullName of Uint64 Type is {anUnit64.GetType().FullName}."

/// Compare None  
type RecordWithNone = {
    FieldA: string option
}
let r1 = { FieldA = None }
let r2 = { FieldA = None }

printf $"Record with None should equal: {r1 = r2}" 

type RecordWithNil = {
    FieldA: string
}
let r3 = { FieldA = null }
let r4 = { FieldA = null }

printf $"Record with null should equal: {r3 = r4}" 

// Try parse TimeSpan
TimeSpan.TryParse("12:34") |> printfn "TimeSpan TryParse %A"

open System
// Try parse DateTime
DateTime.TryParse("1/1/2000") |> printfn "DateTime TryParse %A"

// Try parse DateTimeOffset
DateTimeOffset.TryParse("1/1/2000") |> printfn "DateTimeOffset TryParse %A"

// Missing all Array.Parallel functions

/// Sort in place issues
let arr1 = [| 4;3;2 |]
Array.sortInPlace arr1
printf $"arr1 is {arr1}"

let arr2 = [| 4;3;2 |]
Array.sortInPlaceWith (-) arr2
printf $"arr2 is {arr2}"
 
/// Missing compare_primitive comparer
let dgetf2(m: int, n: int, lda: int): unit =
    for j = 0 to (min m n)-1 do
        printf $"{j}"
 