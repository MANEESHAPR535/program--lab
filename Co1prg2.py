start = int(input("Enter current year: "))
end = int(input("Enter end year: "))

if start <= end:
    leap_years = [str(x + start) for x in range(end-start) if x % 4 == 0 and x % 100 != 0]
    leap_years[-1] += "."
    print(f"Here is a list of leap years between {start} and {end}:\n{(', '.join(leap_years))}")
else:
    print("Check your input years again!")