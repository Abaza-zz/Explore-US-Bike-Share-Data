import time
import pandas as pd
import numpy as np
import os
import sys

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city_selection = input('To view the available bikeshare data, type:\n Chicago\n New York City\n Washington\n  ').lower()
            # Terminate the loop once getting a right answer
            if city_selection in CITY_DATA.keys() :
                city=city_selection
                break 
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid City choice!!')

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            time_filter =input('\n Would you like to filter {}\'s data by month, day, or not at all? type month or day or none: \n'.format(city.title())).lower()
            # Terminate the loop once getting a right answer
            if time_filter in ['month','day','none'] :
                
                if time_filter == 'none':
                    print('\n Filtering for {} for the 6 months period \n'.format(city.title()))
                    month='all'
                    day='all'
                elif time_filter == 'month':
                    while True:
                        try:
                            month_selection=input("Choose month from ['january', 'february', 'march', 'april', 'may', 'june'] & type it \n ").lower()
                            if month_selection in ['january', 'february', 'march', 'april', 'may', 'june'] :
                                month=month_selection
                                day='all'
                                break 
                        except KeyboardInterrupt:
                            print('\nNO Input Taken!')
                        else:
                            print('Invalid month choice!!')
                    
                elif time_filter == 'day':
                    
                    while True:
                        try:
                            day_selection=input("Choose month from Sunday to Saturday & type it \n ").title()
                            if day_selection in ['Monday', 'Tuesday','Wednesday','Thursday', 'Friday', 'Saturday','Sunday'] :
                                day=day_selection
                                month='all'
                                break 
                        except KeyboardInterrupt:
                            print('\nNO Input Taken!')
                        else:
                            print('Invalid day choice!!')
                            
                
                break 
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid choice!!')

    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day, time_filter


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
    df = pd.read_csv(os.path.join(sys.path[0],CITY_DATA[city.lower()]))
    # convert the Start Time column to datetime
    df['Start Time'] = pd.DatetimeIndex(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #dayOfWeek={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    #df['day_of_week'] = df['Start Time'].dt.dayofweek.map(dayOfWeek)
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]
        print(df)
    # filter by day of week if applicable
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        #df = df.loc[df['day_of_week'] == day.title()]
        df= df[df['day_of_week'] == day.title()]
     
    return df



def time_stats(df,time_filter):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if time_filter =='none' or time_filter =='day' :
        df['month'] = df['Start Time'].dt.month

        print("The Most Common month is : {}".format((df['month']).mode()[0]))

    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
'''

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
'''

def main():
    while True:
        city, month, day,time_filter = get_filters()
        df = load_data(city, month, day)

        time_stats(df,time_filter)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
