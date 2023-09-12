from typing import List  # imported typing to remove type warnings
import datetime

our_open_time = datetime.time(8, 0)  # Pet shelter open time
our_close_time = datetime.time(18, 0)  # Pet shelter close time


def available_booking_times(booked_times: list[tuple],
                            desired_duration_hours: int,
                            desired_duration_minutes: int):
    # create new list of free time periods
    free_time: List[List] = [[None] * 2 for _ in range(0, len(booked_times) + 1)]
    for i in range(0, len(booked_times)):
        free_time[i][1] = booked_times[i][0]
        free_time[i + 1][0] = booked_times[i][1]
    free_time[0][0] = datetime.datetime.combine(datetime.date.today(), our_open_time)
    free_time[-1][1] = datetime.datetime.combine(datetime.date.today(), our_close_time)

    # set desired duration to timedelta object
    duration = datetime.timedelta(hours=desired_duration_hours, minutes=desired_duration_minutes)

    # create new list of available times which meet requested duration
    available_times = []
    for period in free_time:
        current_time = period[0]
        while current_time < period[1]:
            if current_time + duration <= period[1]:
                available_times.append(current_time.strftime("%H:%M"))
            current_time = current_time + datetime.timedelta(minutes=15)
    return available_times


# a list of already booked times
booked = [(datetime.datetime(2023, 9, 12, 11, 0),
           datetime.datetime(2023, 9, 12, 12, 0)),
          (datetime.datetime(2023, 9, 12, 14, 0),
           datetime.datetime(2023, 9, 12, 16, 0))]

# set desired duration
input_hours = 1
input_minutes = 30

print(available_booking_times(booked, input_hours, input_minutes))
