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
    print('안녕하세요. 미국 자전거 분석의 세계에 오신것을 환영합니다.')

    while True:
        city = input("Enter the city you want to analyze (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Please enter chicago, new york city, or washington.")

    while True:
        month = input("Enter the month you want to analyze (all, january, february, ... , june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        print("제대로 입력좀 해주세요. Please enter all, january, february, march, april, may, or june.")

    while True:
        day = input("Enter the day you want to analyze (all, monday, tuesday, ... sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        print("잘못된 입력 입니다. Please enter all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday.")

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

    # extract month, day of week, and hour from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # check df have month column
    if 'month' in df.columns:
        most_common_month = df['month'].mode()[0]
        print("The most common month is: ", most_common_month)
    else:
        print("The dataframe does not have a 'month' column.")

    # display the most common day of week
    if 'day_of_week' in df.columns:
        most_common_day = df['day_of_week'].mode()[0]
        print("The most common day of week is: ", most_common_day)
    else:
        print("The dataframe does not have a 'day_of_week' column.")

    # display the most common start hour
    if 'hour' in df.columns:
        most_common_hour = df['hour'].mode()[0]
        print("The most common start hour is: ", most_common_hour)
    else:
        print("The dataframe does not have a 'hour' column.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if 'Start Station' in df.columns:
        most_common_start_station = df['Start Station'].mode()[0]
        print("The most commonly used start station is: ", most_common_start_station)
    else:
        print("The dataframe does not have a 'Start Station' column.")

    # display most commonly used end station
    if 'End Station' in df.columns:
        most_common_end_station = df['End Station'].mode()[0]
        print("The most commonly used end station is: ", most_common_end_station)
    else:
        print("The dataframe does not have a 'End Station' column.")

    # display most frequent combination of start station and end station trip
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print("The most frequent combination of start station and end station trip is: ", most_common_trip)
    else:
        print("The dataframe does not have 'Start Station' and 'End Station' columns.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    if 'Trip Duration' in df.columns:
        total_travel_time = df['Trip Duration'].sum()
        print("The total travel time is: ", total_travel_time)
    else:
        print("The dataframe does not have a 'Trip Duration' column.")

    # display mean travel time
    if 'Trip Duration' in df.columns:
        mean_travel_time = df['Trip Duration'].mean()
        print("The mean travel time is: ", mean_travel_time)
    else:
        print("The dataframe does not have a 'Trip Duration' column.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        user_type_counts = df['User Type'].value_counts()
        print("Counts of each user type:\n", user_type_counts)
    else:
        print("The dataframe does not have a 'User Type' column.")


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of each gender:\n", gender_counts)
    else:
        print("The dataframe does not have a 'Gender' column.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("Earliest year of birth: ", earliest_year)
        print("Most recent year of birth: ", most_recent_year)
        print("Most common year of birth: ", most_common_year)
    else:
        print("The dataframe does not have a 'Birth Year' column.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Ask the user if they want to display the raw data and print 5 rows at a time."""
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue yes or no?: ").lower()
        while view_data not in ['yes', 'no']:
            print("Invalid input. Please enter yes or no.")
            view_data = input("Do you wish to continue yes or no?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        while restart not in ['yes', 'no']:
            print("Invalid input. Please enter yes or no.")
            restart = input("Do you wish to continue yes or no?: ").lower()

if __name__ == "__main__":
	main()

