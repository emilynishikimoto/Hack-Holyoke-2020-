
from django.shortcuts import render
from .forms import ModelForm
import datetime
from datetime import date

month = 0 
day = 0
year = 0
cases = 0 
def mainFunction(request):
    """Asks user for input and figures out the date in python datetime format
    Return: A date in python datetime format"""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModelForm(request.POST)
    
        global month
        global day
        global year
        global cases
        #get user input 
        print( "i am in main function")
        if form.is_valid():    
            print("I am in the if statement")
            #first two integers are month
            month = form.monthInput
            #integers after that is day 
            day = form.dayInput
            #integers after that is year 
            year = form.yearInput
            cases = form.currentCasesInput
            userDate = findDay()
            print("the user date is " + userDate)
            projected = growth(userDate)
            print("the projected is" + projected )
            deathRate = calculateDeathRate()
            print("the death rate is" + deathRate)
            return render(request, 'home.html', {'form': form, 'projected': projected, 'deathRate': deathRate})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModelForm()
        print("I am in the else statement")
    return render(request, 'home.html', {'form': form})

            
def getDate():
    """Asks user for input and figures out the date in python datetime format
    Return: A date in python datetime format"""
    global month
    global day
    global year
    return datetime.date(year, month, day)
def findDay():
    """Figure out the amount of days a given date is from current date
    Return: Number of days that date is from now (as an int)"""
    #projected future date
    projectDate = getDate()
    currentDate = date.today()
    daysDelta = projectDate - currentDate
    days = daysDelta.days
    return int(days)
def growth(amountOfDays):
    """ Takes the amount of days and current cases and returns the number of cases x days later using the R0
    Parameters: 
    amountOfDays(int): the amount of days you want to project for
    currentCases(int): the current number of cases in a given location

    Return: cases(int)"""
    #Current cases will start at current cases
    global cases
    days = int(amountOfDays)
    # for every day in amount of days calculate growth
    cases = cases*(1.05**days)
    return cases
def calculateDeathRate():
    """Takes in projected number of new cases and calculates how many would die"""
    global cases
    deaths = .024 * cases
    # print(f"It is projected that there will be {deaths} number of deaths from the current cases")
    # print("You can prevent these deaths ")
    return deaths

# def main():
#     userDate = findDay()
#     projected = growth(userDate)
#     calculateDeathRate(projected)
# if __name__ == "__main__":
#     main()