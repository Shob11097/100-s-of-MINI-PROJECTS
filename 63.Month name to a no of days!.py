#Month name to a no of days!

try:
    print("The months: January,February,March,April,May,June,July,August,September,October,November,December")
    month = input("Enter the month: ")
    if month == "February":
        print("The number of days: 28/29")
    elif month in ("January","March","May","July","August","October","December"):
        print("The number of days: 31")
    elif month in ("April","June","September","November"):
        print("The number of days: 30")
    else:
        print("You have entered the wrong month!")

except:
    print("Enter a valid month!")