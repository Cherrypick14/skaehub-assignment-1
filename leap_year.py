# a function that determines whether a given year is leap or not

def leap_year(year):
   if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print(f" {year} is a Leap Year") 
    return True
   else:
    print(f"{year} is not a Leap Year")
    return False
year = int(input("enter year: "))
leap_year(year)



