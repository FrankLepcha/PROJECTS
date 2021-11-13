print("This program will calculate what number of day is from a year using the given input from the user")

def main():
    date = (input("Enter a date in this format. month/day/year: ")) #input for the data
    month, day, year = date.split("/") #using .split to split
     #making variables

    month = int(month) #variables now contain ints
    day = int(day)
    year = int(year)

    _31_days_month = ["1", "3", "5", "7", "8", "10", "12"] #months with 31 days

    if (year % 4 == 0): #leap year functin
        leap_year = True
        if (year % 100 == 0):
            if (year % 400 != 0):
                leap_year = False
    else:
        leap_year = False

    if (month > 12 or month < 1): #if the month is vaild or not
            print("The date is invalid")
    if (day >  31): #seeing if days are not valid
            print("The date is invalid")
    if (month ==_31_days_month[0] and day > 31):
            print("The date is invalid")
    if (month == _31_days_month[1] and day > 31):
            print("The date is invalid")
    if (month ==_31_days_month[2] and day > 31):
            print("The date is invalid")
    if (month ==_31_days_month[3] and day > 31):
            print("The date is invalid")
    if (month ==_31_days_month[4] and day > 31):
            print("The date is invalid")
    if (month ==_31_days_month[5] and day > 31):
            print("The date is invalid")
    if (month ==_31_days_month[6] and day > 31):
            print("The date is invalid")

         #finding the invalid dates

    if(month == 2 and day >29 ):
            print("The date is invalid ")
    if(month == 4 and day > 30):
            print("The date is invalid ")
    if (month == 6 and day > 30):
            print("The date is invalid ")
    if (month == 9 and day > 30):
            print("The date is invalid ")
    if (month == 11 and day > 30):
            print("The date is invalid ")

    dayNum = 31 * (month - 1) + day #daynum calculations
    dayNum -= (4 * month + 23) // (10)
    if leap_year == True and month > 2:
        dayNum += 1


    print("The following day for the given input is", dayNum)

main()





