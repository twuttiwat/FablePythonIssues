open System

let today = DateTime.Today
let currentDate = DateTime.Now
let tomorrow = currentDate.AddDays(1)
let nextMonth = currentDate.AddMonths(1)
let localToday = DateTime.SpecifyKind(currentDate, DateTimeKind.Local)
let daysInMonth = DateTime.DaysInMonth(2000, 1)

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