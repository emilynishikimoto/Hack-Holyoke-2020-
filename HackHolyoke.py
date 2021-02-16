import datetime
from datetime import date
print(date.today())
def findDay():
    """Figure out the amount of days a given date is from current date
    Return: Number of days that date is from now (as an int)"""
    #projected future date
    projectDate = getDate()
    currentDate = date.today()
    daysDelta = projectDate - currentDate
    days = daysDelta.days
    return int(days)
def getDate():
    """Asks user for input and figures out the date in python datetime format
    Return: A date in python datetime format"""
    month = 0
    day = 0
    year = 0
    #get user input 
    userInput = input("Please enter the date you want a projection for (MM/DD/YYYY)")    
    #first two integers are month
    month = int(userInput[0:2])
    #integers after that is day 
    day = int(userInput[3:5])
    #integers after that is year 
    year = int(userInput[6:10])
    return datetime.date(year,month,day)
def growth(amountOfDays):
    """ Takes the amount of days and current cases and returns the number of cases x days later using the R0
    Parameters: 
    amountOfDays(int): the amount of days you want to project for
    currentCases(int): the current number of cases in a given location

    Return: cases(int)"""
    #Current cases will start at current cases
    cases = int(input("Please enter the current number of cases: "))
    days = int(amountOfDays)
    # for every day in amount of days calculate growth
    cases = cases*(1.05**days)
    return print(f"The projected number of cases in {days} days is: {cases}")
def calculateDeathRate(cases):
    """Takes in projected number of new cases and calculates how many would die"""
    intCases = int(cases)
    deaths = .024 * intCases
    print(f"It is projected that there will be {deaths} number of deaths from the current cases")
    print("You can prevent these deaths ")

def main():
    userDate = findDay()
    projected = growth(userDate)
    # calculateDeathRate(projected)
    print("Prevent thes cases by wearing a mask, practicing social distancing, and limiting social interaction as per CDC guidelines")

if __name__ == "__main__":
    main()