import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    #list of the cities to be chosen
    cities =['chicago','new york city', 'washington']
    
   #Have user input which city to choose
    city = input("Which city would you like to choose: chicago, new york city or washington: ").lower()
    
    #Checking to see if proper city was selected if not, it will print an error message
    while True:
        if city in cities:
            print("you have selected: ", city)
            break
        else:
            print("Error: please select chicago, new york city or washington please...")
            city = input("Which city would you like to choose: chicago, new york or washington: ").lower()
    
            
    # TO DO: get user input for month (all, january, february, ... , june)
    
    #list of months to be chosen
    months = ['january','february','march','april','may','june']
    
    #have user input which month to choose
    month = input("Which month will you choose: janaury - june are the selections: ").lower()
    
    #check to see if user choose the correct month
    while True:
        if month in months:
            print("you have selected: " , month)
            break
        else:
            print("Error: please select from the months of january through june only please...")
            month = input("Which month will you choose: janaury - june are the selections: ").lower()
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    #list of days of the week to be chosen
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    
    #have user input a day of their choosing
    day = input("Which day would you like to choose: ").lower()
    
    #check to see if user choose a correct day
    while True:
        if day in days:
            print("you have selected: ", day)
            break
        else:
            print("Error: please select which day of the week please....")
            day = input("Which day would you like to choose: ").lower()
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #extract hour from Start Time to create a new column
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    
    print("The most common month is " , common_month)


    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    
    print("The most common day of the week is ", common_day_of_week)


    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    
    print("The most common star hour is ", common_start_hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    
    print("The most common start station is ", common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    
    print("The most common end station is ", common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    both_stations = df['Start Station'] + 'to' + df['End Station']
    
    print(both_stations.mode()[0], " is the most frequent combination of start and end stations")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    print('The total travel time is ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('The average travel time is ', mean_travel_time)
    
    #To Do: display most and least travel time
    max_time_travel = df['Trip Duration'].max()
    
    min_time_travel = df['Trip Duration'].min()
    
    print("The longest trip duration is ", max_time_travel)
    print("\nThe shortest trip duration is ", min_time_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type = df['User Type'].value_counts()
        print(pd.DataFrame(user_type))
    else:
        print("User Type does not exist" )                                      
          


    # TO DO: Display counts of gender
    
                                               
    if "Gender" in df.columns:
       gender_type = df['Gender'].value_counts()
       print(pd.DataFrame(gender_type))
    else:
        print("Gender does not exist")
                                
   


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("Years of birth\n")
        print("Earliest: ", earliest_year,"\nMost Recent: ", most_recent, "\nMost Common: ", most_common)
    else:
          print("Birth Year not found")            


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    i = 0
    while True:
        user_input = input('Would you like to see 5 rows of data? y/n: ').lower()
        if (user_input == 'y'):
            print(df.iloc[i:i+5])
            i+=5
            continue
        elif (user_input == 'n'):
              break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
